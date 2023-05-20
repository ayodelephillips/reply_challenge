import pandas as pd
import itertools
import os


def read_file():
    base_path = f"{os.path.normpath(os.getcwd() + os.sep + os.pardir)}"
    input_file = f"{base_path}/reply_challenge/input_File.txt"
    return pd.read_csv(input_file, header=None, names=['Enemy'])


def extract_game_enemy_detail(data: pd.DataFrame):
    """
    extract game details from enemy details
    :param data:
    :return: the game details, alongside a  dataframe of enemy players
    """
    game_detail = data['Enemy'].loc[0]
    enemies_detail = data.drop([0])
    return game_detail, enemies_detail


def get_possible_enemy_sequence(list_of_enemy):
    """
    :param list_of_enemy: A list containing the indexes of enemies
    :return:
    """
    return list(itertools.permutations(list_of_enemy))


if __name__ == "__main__":
    read_file()