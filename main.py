import pandas as pd
import os as os

def read_file():
    base_path = f"{os.path.normpath(os.getcwd() + os.sep + os.pardir)}"
    input_file = f"{base_path}/reply_challenge/input_File.txt"
    colnames = ['Enemy']
    file_import_df = pd.read_csv(input_file
                             ,header = None
                            , names = colnames
                             )
    # print(file_import_df['Enemy'].loc[])
    # print(file_import_df[2])
    return file_import_df
read_file()
# print(file_import_df.head(9))
# file_import_df = file_import_df.replace(' ',',', regex = True)
# print(file_import_df.head(10))


