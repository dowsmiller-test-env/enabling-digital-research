from flask import Flask, jsonify, render_template, request, redirect, make_response
import pandas as pd
from pandas.errors import MergeError
import os
from waitress import serve
from werkzeug.utils import secure_filename
from column_merge_helpers import load_and_merge
import json
import traceback

template_dir = os.path.join(os.path.dirname(__file__), 'column_merge', 'templates')
upload_folder = os.path.join(os.path.dirname(__file__), 'column_merge', 'uploads')
static_folder = os.path.join(os.path.dirname(__file__), 'column_merge', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_folder)
app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('files')
        file_paths = []
        for file in files:
            filename = secure_filename(file.filename) if file.filename is not None else ""
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            file_paths.append(path)
        return redirect('/select?files=' + ','.join(file_paths))
    instructions = (
        "Step 1: Upload one or more CSV files. "
        "Click 'Select files' to choose files, then 'Continue' to proceed."
    )
    return render_template('index.html', instructions=instructions)

@app.route('/select')
def select():
    file_paths_param = request.args.get('files')
    if not file_paths_param:
        return redirect('/')

    file_paths = file_paths_param.split(',')
    all_columns = {}
    for fp in file_paths:
        df = pd.read_csv(fp, nrows=5)
        df.columns = df.columns.str.strip()
        filename = os.path.basename(fp)
        all_columns[filename] = df.columns.tolist()

    safe_keys = {
        filename: filename.replace('.', '_').replace(' ', '_').replace(':', '_').replace('/', '_')
        for filename in all_columns.keys()
    }

    instructions = (
        "Step 2: Select the columns to include from each file. "
        "Choose a merge key (the column used to combine files) for each file. "
        "The default is the 'Part ID' column, if found."
    )

    return render_template(
        'select_columns.html',
        files=all_columns,
        safe_keys=safe_keys,
        instructions=instructions
    )

@app.route('/require_values', methods=['GET', 'POST'])
def require_values():
    if request.method == 'POST':
        form = request.form.to_dict(flat=False)

        merge_keys = {}
        files_with_columns = {}
        for key, values in form.items():
            if key == 'files':
                continue
            if key.endswith('_merge_key'):
                file = os.path.basename(key.rsplit('_merge_key', 1)[0])
                merge_keys[file] = values[0]
            else:
                files_with_columns[key] = values

            for file, merge_key in merge_keys.items():
                if file not in files_with_columns:
                    files_with_columns[file] = []
                if merge_key not in files_with_columns[file]:
                    files_with_columns[file].append(merge_key)

        instructions = (
            "Step 3: Choose which columns must contain data, and optionally exclude empty rows. "
        )

        return render_template('require_values.html', files=files_with_columns,
                               files_json=json.dumps(files_with_columns),
                               merge_keys=merge_keys,
                               instructions=instructions)
    return redirect('/select')

@app.route('/merge', methods=['POST'])
def merge():
    form = request.form.to_dict(flat=False)

    exclude_empty = form.pop('exclude_empty_rows', ['false'])[0] == 'true'
    required_columns = form.pop('required_columns', [])
    files_with_columns = json.loads(form['files'][0])

    merge_keys = {key.rsplit('_merge_key', 1)[0]: val[0] for key, val in form.items() if key.endswith('_merge_key')}

    try:
        merged_df = load_and_merge(files_with_columns, merge_keys, upload_dir=app.config['UPLOAD_FOLDER'])

        if exclude_empty or required_columns:
            cols_to_check = required_columns if required_columns else [col for col in merged_df.columns if col != 'metadata: part ID']
            merged_df = merged_df.dropna(subset=cols_to_check, how='any')

        merged_csv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.csv')
        merged_df.to_csv(merged_csv_path, index=False, encoding='utf-8-sig')
        html_table = merged_df.fillna('').to_html(classes='data-table', index=False)
        return render_template('result.html', table=html_table)

    except (KeyError, MergeError) as e:
        error_msg = (
            "Merge failed: The selected merge keys have no matching values or columns are missing.<br>"
            "Please check your selections and try again."
        )
        return render_template('error.html', error_message=error_msg), 400

@app.route("/download_csv")
def download_csv():
    merged_csv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.csv')

    if not os.path.exists(merged_csv_path):
        return render_template('error.html', error_message="No merged file found to download."), 404

    with open(merged_csv_path, 'r', encoding='utf-8-sig') as f:
        csv_data = f.read()

    response = make_response(csv_data)
    response.headers["Content-Disposition"] = "attachment; filename=merged.csv"
    response.headers["Content-Type"] = "text/csv"
    return response

@app.route("/download_json")
def download_json():
    merged_csv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.csv')

    if not os.path.exists(merged_csv_path):
        return render_template('error.html', error_message="No merged file found to download."), 404

    df = pd.read_csv(merged_csv_path)

    response = make_response(df.fillna('').to_json(orient='records', force_ascii=False))
    response.headers["Content-Disposition"] = "attachment; filename=merged.json"
    response.headers["Content-Type"] = "application/json"
    return response

@app.errorhandler(Exception)
def handle_all_exceptions(e):
    # Log the full traceback (for debugging)
    tb = traceback.format_exc()
    app.logger.error(f"Unhandled Exception: {tb}")

    error_msg = (
        "An unexpected error occurred. "
        "Please try again."
    )

    # Include error details (only in debug mode):
    if app.debug:
        error_msg += f"<pre>{tb}</pre>"

    return render_template('error.html', error_message=error_msg), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_message="404 Not Found: The requested page does not exist."), 404

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000

    print(f"Starting server at http://{host}:{port}/")
    print("Press CTRL+C to quit.")

    serve(app, host=host, port=port)