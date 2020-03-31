from malex.arena   import Arena
from malex.battle  import Battle
from malex.trainer import Trainer
from unittest.mock import Mock
import unittest
import io
import sys


class TestArena(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.alex            = Mock(Trainer)
        cls.mario           = Mock(Trainer)
        cls.jhibby          = Mock(Trainer)
        cls.jeff_pesos      = Mock(Trainer)
        cls.bill_negates    = Mock(Trainer)
        cls.elon_memelord   = Mock(Trainer)
        cls.battle          = Battle

    def setUp(self):
        self.TRAINERS = [
                            self.alex, self.mario, self.jhibby, self.jeff_pesos,
                            self.bill_negates, self.elon_memelord
                        ]

        self.arena = Arena('The Pwn Zone')

    # ------------------------------------------------------------

    def test_run_arena(self):
        ## Ensure battle_defender called an amount of times  ##
        ## equal to the number of defenders in the arena.    ##

        for trainer in self.TRAINERS:
            self.arena.battle_defender = Mock()
            self.arena.defenders.append(trainer)
            self.arena.run_arena()
            self.assertEqual(len(self.arena.defenders), self.arena.battle_defender.call_count)

    def test_set_challenger(self):
        ## Ensure set challenger references same object as   ##
        ## original challenger.                              ##
        for trainer in self.TRAINERS:
            self.arena.set_challenger(trainer)
            self.assertIs(self.arena.challenger, trainer)

    def test_add_defender(self):
        ## Ensure each defender is added to the list of      ##
        ## defenders.                                        ##
        for trainer in self.TRAINERS:
            self.arena.add_defender(trainer)
            self.assertIn(trainer, self.arena.defenders)

    def test_battle_defender(self):
        ## Ensure arena_conquered is False and arena is      ##
        ## exited if the challenger loses.                   ##
        self.arena.exit_arena = Mock()
        self.battle.battle    = Mock(return_value='JHibby')
        self.alex.get_name    = Mock(return_value='Alex')
        self.arena.challenger = self.alex

        self.arena.battle_defender(self.jhibby)
        self.assertFalse(self.arena.arena_conquered)
        self.assertTrue (self.arena.exit_arena.called)

    def test_exit_arena(self):
        ## Ensure sys.exit and display_results are called    ##
        with self.assertRaises(SystemExit):
            self.arena.display_results = Mock()
            self.arena.exit_arena()
            self.assertTrue(self.arena.display_results.called)

    def test_display_results(self):
        ## Ensure correct message is displayed.              ##
        print('--------------------------------------------------')
        print('Display Results:')
        print()

        output      = io.StringIO()
        sys.stdout  = output
        exp_display = 'Mario test The Pwn Zone.'

        self.arena.challenger        = self.mario
        self.mario.get_name          = Mock(return_value='Mario')
        self.arena.determine_results = Mock(return_value='test')
        self.arena.display_results()
        self.assertEqual(exp_display, output.getvalue().rstrip('\n'))

        sys.stdout = sys.__stdout__
        print(output.getvalue())

    def test_determine_results(self):
        ## Ensure correct result is returned                 ##
        NUM_OPTIONS   = 2
        result_ops    = ['conquered', 'did not conquer']
        conquered_ops = [True, False]

        for option in range(NUM_OPTIONS):
            self.arena.arena_conquered = conquered_ops[option]
            result                     = self.arena.determine_results()

            exp_result = result_ops[option]
            self.assertEqual(result, exp_result)


if __name__ == '__main__':
    unittest.main()
