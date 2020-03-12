"""
    The Battle class runs the battle simulations for the arena.
"""
from copy import deepcopy
from random import randint


class Battle:

    def __init__(self, challenger, defender):
        self.SIM_DIVIDER = 5
        self.challenger  = deepcopy(challenger)
        self.defender    = deepcopy(defender)
        self.c_stats     = None
        self.d_stats     = None
        self.battle_won  = None
        self.mvp_name    = None

    def battle(self):
        """
            Run the battle simulation.
        """
        pass

    def simulate(self):
        """
            Add variability to each trainer's team stat groups to
            simulate the battle.
        """
        self.c_stats = self.challenger.get_team_stat_groups()
        self.d_stats = self.defender.get_team_stat_groups()

        for key in self.c_stats:
            self.c_stats[key] *= (randint(1, 5) / self.SIM_DIVIDER)
            self.d_stats[key] *= (randint(1, 5) / self.SIM_DIVIDER)

    def compare(self):
        """
            Compare the simulated stat groups of each trainer to determine
            the winner of the battle.
        """
        c_points = 0
        d_points = 0

        for key in self.c_stats:
            if self.c_stats[key] > self.d_stats[key]:
                c_points += 1
            elif self.c_stats[key] < self.d_stats[key]:
                d_points += 1
            else:
                print('Tie group')

        if c_points > d_points:
            self.battle_won = True
        elif c_points < d_points:
            self.battle_won = False
        else:
            print('Tie battle')

    def mvp(self):
        """
            Determine the most valuable pokemon for the trainer who won.
        """
        if self.battle_won:
            self.mvp_name = self.challenger.calculate_team_mvp()
        if not self.battle_won:
            self.mvp_name = self.defender.calculate_team_mvp()

    def display(self):
        """
            Display the results to the console.
        """
        if self.battle_won:
            print('{} defeated {}! {} was the mvp'.format(
                self.challenger.get_name(), self.defender.get_name(),
                self.mvp_name
            ))
        if not self.battle_won:
            print('{} defeated {}! {} was the mvp'.format(
                self.defender.get_name(), self.challenger.get_name(),
                self.mvp_name
            ))

    def get_result(self):
        """
            Return the result of the battle.
        """
        return self.battle_won
