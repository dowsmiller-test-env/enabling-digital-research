import os
import pandas as pd
from functools import reduce

def load_and_merge(files_with_columns, merge_keys, upload_dir):
    dfs = []
    for file_name, columns in files_with_columns.items():
        file_path = os.path.join(upload_dir, file_name)
        df = pd.read_csv(file_path, low_memory=False)

        merge_key = merge_keys.get(file_name)
        if not merge_key or merge_key not in df.columns:
            raise ValueError(f"Merge key '{merge_key}' not found in {file_name}.")

        if merge_key not in columns:
            columns.append(merge_key)

        df = df[columns]
        df = df.rename(columns={merge_key: 'metadata: part ID'})

        prefix = os.path.splitext(os.path.basename(file_name))[0]
        df = df.rename(columns={col: f"{prefix}: {col}" for col in df.columns if col != 'metadata: part ID'})

        dfs.append(df)

    if not dfs:
        raise ValueError("No dataframes to merge. Check that at least one file was processed.")

    merged_df = reduce(lambda l, r: pd.merge(l, r, on='metadata: part ID', how='outer'), dfs)

    cols = merged_df.columns.tolist()
    if 'metadata: part ID' in cols:
        cols.insert(0, cols.pop(cols.index('metadata: part ID')))
    return merged_df[cols]
