import pandas as pd 

def load_data(excel_path):
    sheet_names = pd.ExcelFile(excel_path).sheet_names

    df = {sheet: pd.read_excel(excel_path, sheet_name=sheet, header=1) for sheet in sheet_names if sheet != "TOPLAM"}

    df = pd.concat(df.values(), ignore_index = True)

    return df 