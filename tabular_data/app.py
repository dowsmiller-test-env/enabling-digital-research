from flask import Flask, render_template, request, redirect, make_response
import pandas as pd
import os
from werkzeug.utils import secure_filename
from app_helpers import load_and_merge

template_dir = os.path.join(os.path.dirname(__file__), 'app', 'templates')
upload_folder = os.path.join(os.path.dirname(__file__), 'app', 'uploads')
static_folder = os.path.join(os.path.dirname(__file__), 'app', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_folder)
app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('files')
        file_paths = []
        for file in files:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            file_paths.append(path)
        return redirect('/select?files=' + ','.join(file_paths))
    return render_template('index.html')

@app.route('/select')
def select():
    # Read column names from uploaded files
    file_paths = request.args.get('files').split(',')
    all_columns = {fp: pd.read_csv(fp, nrows=5).columns.tolist() for fp in file_paths}
    return render_template('select_columns.html', files=all_columns)

merged_csv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged_output.csv')

@app.route('/merge', methods=['POST'])
def merge():
    global merged_df
    form_data = request.form.to_dict(flat=False)

    exclude_empty = form_data.pop('exclude_empty_rows', ['false'])[0] == 'true'

    merged_df = load_and_merge(form_data)

    if exclude_empty:
        part_id_col = 'metadata: part ID'
        cols_except_part_id = [col for col in merged_df.columns if col != part_id_col]
        merged_df = merged_df[merged_df[cols_except_part_id].notna().any(axis=1)]

    merged_df.to_csv(merged_csv_path, index=False, encoding='utf-8-sig')

    html_table = merged_df.fillna('').to_html(classes='data-table', index=False)
    return render_template('result.html', table=html_table)



@app.route("/download")
def download():
    global merged_df
    response = make_response(merged_df.fillna('').to_csv(index=False))
    response.headers["Content-Disposition"] = "attachment; filename=merged.csv"
    response.headers["Content-Type"] = "text/csv"
    return response

if __name__ == '__main__':
    app.run(debug=True)
