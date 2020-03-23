"""

    The arena class runs the arena.

"""
import sys
from queue        import Queue
from malex.battle import Battle


class Arena:

    def __init__(self, name):
        self.MAX_DEFENDERS    = 6
        self.INFINITE         = 0
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
        message       = 'Defender could not be added.'
        num_defenders =  len(self.defenders)

        assert num_defenders < self.MAX_DEFENDERS, message
        self.defenders.append(defender)

    #-------------------------------------------------------------------------

    def battle_defender(self, defender):
        """
            Initiate a battle between the challenger and the next
            defender in the arena.
        """
        battle = Battle(self.challenger, defender)
        winner = battle.battle()

        if winner != self.challenger.get_name():
            self.exit_arena()

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
        print('{} {} the arena.'.format(
            self.challenger.get_name(), self.determine_results())
        )

    def determine_results(self):
        """
            Determine if challenger conquered the arena or not.
        """
        return 'conquered' if self.arena_conquered else 'did not conquer'
