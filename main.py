import pandas as pd
import os as os

from utility import read_file, get_possible_enemy_sequence, extract_game_enemy_detail


class Simulation:
    def __init__(self):
        """ pass in the 4 constraints here"""
        self.starting_stamina_pt = None
        self.max_stamina_pt = None
        self.max_turns = None
        self.num_of_enemies = None
        self.game_details = None
        self.enemies_details = None

        # scoring
        self.turns_and_rewards_details: pd.DataFrame = None # table in the reply sheet; add in column for sequences

    def run_simulation(self):
        """
        run the simulations
        :return:
        """

    def run(self):
        # read file
        data = read_file()

        # extract game details, and enemy details
        game_details, enemies = extract_game_enemy_detail(data)

        # set the important aspects of the game
        self.starting_stamina_pt, self.max_stamina_pt = game_details.split()[0], game_details.split()[1]
        self.max_turns, self.num_of_enemies = game_details.split()[2], game_details.split()[3]
        self.game_details, self.enemies_details = game_details, enemies

        # get enemy sequence
        simulation_sequence = get_possible_enemy_sequence(list(enemies.index))

        for sequence in simulation_sequence:
            self.run_simulation(sequence)


if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()
