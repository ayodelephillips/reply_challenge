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
    player = file_import_df['Enemy'].loc[0]
    red_demon = file_import_df['Enemy'].loc[1]
    teal_demon = file_import_df['Enemy'].loc[2]
    orange_demon = file_import_df['Enemy'].loc[3]
    violet_demon = file_import_df['Enemy'].loc[4]
    brown_demon = file_import_df['Enemy'].loc[5]
    return print(player)
read_file()

def constraints_define():
    ##dictionaries for player and demon constraints.
    pass

