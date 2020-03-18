"""

    The arena class runs the arena.

"""
from malex.battle import Battle
import sys


class Arena:

    def __init__(self, name):
        self.MAX_DEFENDERS    = 6
        self.name             = name
        self.challenger       = None
        self.defenders        = []
        self.arena_conquered  = True

    #-------------------------------------------------------------------------

    def run_arena(self):
        """
            Run the arena simulation.
        """
        for defender in self.defenders:
            self.battle_defender(defender)

            if not self.arena_conquered:
                break

        self.exit_arena()

    #-------------------------------------------------------------------------

    def set_challenger(self, challenger):
        """
            Set the trainer to challenge the arena.
        """
        self.challenger = challenger

    def add_defender(self, defender):
        """
            Add trainers to defend the arena.
        """
        if len(self.defenders) < self.MAX_DEFENDERS:
            self.defenders.append(defender)
        else:
            print('Defender could not be added.')

    #-------------------------------------------------------------------------

    def battle_defender(self, defender):
        """
            Initiate a battle between the challenger and the next
            defender in the arena.
        """
        battle = Battle(self.challenger, self.defenders.pop(defender))
        winner = battle.battle()

        if winner != self.challenger.get_name():
            self.arena_conquered = False

    #-------------------------------------------------------------------------

    def exit_arena(self):
        """
            Exit the arena.
        """
        self.display_results()
        sys.exit()

    def display_results(self):
        """
            Display if challenger conquered or was defeated by the
            arena.
        """
        conquered = ""
        if self.arena_conquered:
            conquered = 'conquered'
        else:
            conquered = 'did not conquer'

        print('{} {} the arena.'.format(self.challenger.get_name(), self))
