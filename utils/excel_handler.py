import pandas as pd

def read_excel(file_path):
    print("Reading from file: ", file_path)
    return pd.read_excel(file_path, na_filter=False)

def write_excel(file_path, data):
    print("Writing to file: ", file_path)
    data.to_excel(file_path, index=False)
