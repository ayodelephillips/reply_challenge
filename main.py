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

    def stamina_rule_set(self):
        """
        Demon is defeated by deducting stamina
        Stamina is deducted each turn then added back after
        defeating the enemy
         """
        p_stamina = int(self.starting_stamina_pt)
        e_stamina = self.enemies_details.iloc[0,0].astype('int')

        if p_stamina >= e_stamina:
           p_stamina -= e_stamina
           stamina_recovery_turns = self.enemies_details.iloc[0,1]
           stamina_recovery = self.enemies_details.iloc[0,2]
        else:
            # return turns_rule_set()
            pass


    def turns_rule_set(self, p_turns, e_turns_to_beat):
        """"
         Max turns = 10
        1 enemy per turn
        after turn 'stamina_recovery_turns' stamina increase by 'stamina_recovery'
        in turn collect stamina, then face enemy, then collect fragment
        in each turn you can revoer all stamina from defested demons
        fragment collecting will last a maximum of t runs
        A variable is stored to count total turns"""


        pass


    def enemy_details(self, e_defeatturns, e_defeatstamina):
        pass

    def run_simulation(self, sequence):
        """
        run the simulations
        :return:
        """
        pass

if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()
    # simulation.stamina_rule_set()
