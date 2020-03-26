from malex.arena import Arena
from unittest.mock import Mock
import unittest


class TestBattle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.arena = Arena('The Pwn Zone')
        

    def setUp(self):

    # ------------------------------------------------------------

    def test_run_arena(self):
        ## Ensure battle_defender called the expected amount ##
        ## of times.                                         ##
        print('--------------------------------------------------')
        EXPECTED_1 = 1
        EXPECTED_2 = 6


    def test_set_challenger(self):
        ## Ensure set challenger references same object as   ##
        ## original challenger.                              ##
        pass

    def test_add_defender(self):
        ## Ensure the length of the list of defenders grows  ##
        ## as defenders are added and that each defender     ##
        ## references the same objects as the original       ##
        ## defenders.                                        ##
        pass

    def test_battle_defender(self):
        ## Ensure arena_conquered is False and arena is      ##
        ## exited if the challenger loses.                   ##
        pass

    def test_exit_arena(self):
        ## Ensure sys.exit() is called.                      ##
        pass

    def test_display_results(self):
        ## Ensure correct message is displayed.              ##
        pass


if __name__ == '__main__':
    unittest.main()
