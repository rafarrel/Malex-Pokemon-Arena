"""
    The Battle class runs the battle simulations for the arena.
"""
from copy import deepcopy
from random import randint


class Battle:

    def __init__(self, challenger, defender):
        self.SIM_CONST  = 5
        self.challenger = deepcopy(challenger)
        self.defender   = deepcopy(defender)
        self.c_stats    = None
        self.d_stats    = None
        self.winner     = None
        self.loser      = None
        self.mvp_name   = None

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
            self.c_stats[key] *= (randint(1, 5) / self.SIM_CONST)
            self.d_stats[key] *= (randint(1, 5) / self.SIM_CONST)

    def compare_stats(self):
        """
            Compare the simulated stat groups of each trainer to determine
            the winner of the battle.
        """
        c_points, d_points = self.add_points()

        if c_points > d_points:
            self.winner = self.challenger
            self.loser  = self.defender
        if c_points < d_points:
            self.winner = self.defender
            self.loser  = self.challenger

    def add_points(self):
        """
            Add points to trainer with higher simulated stat groups.
        """
        c_points = 0
        d_points = 0

        for key in self.c_stats:
            c_points += 1 if self.c_stats[key] > self.d_stats[key] else 0
            d_points += 1 if self.c_stats[key] < self.d_stats[key] else 0

        return c_points, d_points

    def determine_mvp(self):
        """
            Determine the most valuable pokemon for the trainer who won.
        """
        self.mvp_name = self.winner.calculate_team_mvp()

    def display_results(self):
        """
            Display the results to the console.
        """
        print('{} defeated {}! {} was the mvp'.format(
            self.winner.get_name(), self.loser.get_name(), self.mvp_name)
        )

    def get_winner(self):
        """
            Return name of winner of the battle.
        """
        return self.winner.get_name()
