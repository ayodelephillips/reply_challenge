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
        global stamina_recovery_turns
        global stamina_recovery

        p_stamina = int(self.starting_stamina_pt)
        e_details = self.enemies_details.iloc[0].to_frame()
        e_stamina = int(e_details.iloc[0,0][0:2])

        # print(e_stamina)
        # print(len(self.enemies_details))

        for x in self.enemies_details:
            enemy_faced = 0
            stamina_recovery = 0
            stamina_recovery_turns = 0

            if p_stamina <= e_stamina:
                p_stamina -= e_stamina
                stamina_recovery_turns += int(self.enemies_details.iloc[0][0][4:])
                stamina_recovery += int(self.enemies_details.iloc[0][0][0])
                enemy_faced += 1

                print('hi')
                print(stamina_recovery)
                print(stamina_recovery_turns)
            else:
                print('hello')
                print(e_stamina)
                print(p_stamina)
                print(stamina_recovery)
                print(stamina_recovery_turns)
                return self.enemies_details

            return stamina_recovery_turns, stamina_recovery
            print('hey')
            # print(stamina_recovery)
            # print(stamina_recovery_turns)


    def turns_rule_set(self, p_turns, e_turns_to_beat):
        """"
         Max turns = 10
        1 enemy per turn
        after turn 'stamina_recovery_turns' stamina increase by 'stamina_recovery'
        in turn collect stamina, then face enemy, then collect fragment
        in each turn you can revoer all stamina from defested demons
        fragment collecting will last a maximum of t runs
        A variable is stored to count total turns"""

        # for x in range(p_turns):
        #     if stamina_recovery_turns ==


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
    simulation.stamina_rule_set()
    # simulation.turns_rule_set()
