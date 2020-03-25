from malex.battle  import Battle
from random        import randint
from math          import fabs
from unittest.mock import Mock
import unittest
import sys
import io


class TestingTrainer:
    ## Fake trainer class for testing                      ##

    def __init__(self, phys, att, dfn):
        self.team_stat_groups = {
            'Physical': phys, 'Attack': att, 'Defense': dfn
        }

    def get_team_stat_groups(self):
        return self.team_stat_groups


class TestBattle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        c_phys = randint(1, 200)
        c_att  = randint(1, 200)
        c_dfn  = randint(1, 200)

        d_phys = randint(1, 200)
        d_att  = randint(1, 200)
        d_dfn  = randint(1, 200)

        cls.challenger = TestingTrainer(c_phys, c_att, c_dfn)
        cls.defender   = TestingTrainer(d_phys, d_att, d_dfn)

    def setUp(self):
        self.battle = Battle(self.challenger, self.defender)

    #------------------------------------------------------------

    def test_add_variability(self):
        ## Ensure at least one stat is changed after         ##
        ## variability is generated for each trainer.        ##
        print('--------------------------------------------------')
        print('Add Var:')
        print()

        c_chng_count = 0
        d_chng_count = 0
        c_old_stats  = self.challenger.team_stat_groups
        d_old_stats  = self.defender.team_stat_groups

        self.battle.add_variability()
        c_new_stats = self.battle.c_stats
        d_new_stats = self.battle.d_stats

        for key in self.battle.c_stats:
            c_chng_count += 1 if c_old_stats[key] != c_new_stats[key] else 0
            d_chng_count += 1 if d_old_stats[key] != d_new_stats[key] else 0

        self.assertFalse(c_chng_count == 0)
        self.assertFalse(d_chng_count == 0)

        print('Old c:', c_old_stats)
        print('New c:', c_new_stats)
        print()
        print('Old d:', d_old_stats)
        print('New d:', d_new_stats)
        print()

    def test_genrate_variability(self):
        ## Ensure variability is generated so that the       ##
        ## new stat is outside desired quartiles +- (old     ##
        ## stat divided by four) a minimum of 5% and         ##
        ## maximum of 10% of all generations.                ##
        print('--------------------------------------------------')
        print('Var Generation:')
        print()

        FREQ_L_BOUND = 0.05
        FREQ_U_BOUND = 0.1
        SD_DIV       = 4
        NUM_TESTS    = 10000

        for key in self.challenger.team_stat_groups:
            c_orig = self.challenger.team_stat_groups[key]
            d_orig = self.defender.team_stat_groups[key]

            # Calculate expected differences
            c_exp_diff = c_orig / SD_DIV
            d_exp_diff = d_orig / SD_DIV

            c_diff_greater_freq = 0
            d_diff_greater_freq = 0
            num_tests           = 0

            for test in range(NUM_TESTS):
                c_obs = self.battle.generate_variability(self.challenger.team_stat_groups, key)
                d_obs = self.battle.generate_variability(self.defender.team_stat_groups, key)

                # Calculate differences
                c_diff = fabs(c_orig - c_obs)
                d_diff = fabs(d_orig - d_obs)

                # Add to frequencies for differences greater than expected difference
                c_diff_greater_freq += 1 if c_diff > c_exp_diff else 0
                d_diff_greater_freq += 1 if d_diff > d_exp_diff else 0
                num_tests += 1

            # Calculate frequencies
            c_diff_greater_freq /= num_tests
            d_diff_greater_freq /= num_tests

            self.assertTrue(FREQ_L_BOUND <= c_diff_greater_freq <= FREQ_U_BOUND)
            self.assertTrue(FREQ_L_BOUND <= d_diff_greater_freq <= FREQ_U_BOUND)

            print(key)
            print('cdgf:', c_diff_greater_freq)
            print('ddgf:', d_diff_greater_freq)
            print()

    def test_determine_winner(self):
        ## Ensure winner and loser reference the correct   ##
        ## trainers based on which has higher points.      ##
        print('--------------------------------------------------')
        print('Determine Winner:')
        print()

        battle_mock = Battle

        # Challenger is winner
        battle_mock.compare_stats = Mock(return_value=(2, 0))
        self.battle.determine_winner()
        self.assertIs(self.battle.challenger, self.battle.winner)
        self.assertIs(self.battle.defender, self.battle.loser)

        print('Challenger wins:')
        print(self.battle.challenger)
        print(self.battle.winner)
        print()

        # Defender is winner
        battle_mock.compare_stats = Mock(return_value=(0, 2))
        self.battle.determine_winner()
        self.assertIs(self.battle.defender, self.battle.winner)
        self.assertIs(self.battle.challenger, self.battle.loser)

        print('Defender wins:')
        print(self.battle.defender)
        print(self.battle.winner)
        print()

    def test_compare_stats(self):
        ## Ensure comparison gives points to the trainer   ##
        ## with the higher result for each stat group and  ##
        ## the trainer with the most points is the winner  ##
        NUM_TESTS = 100

        for test in range(NUM_TESTS):
            self.battle.c_stats = {0: test+1, 1: test+1, 2: test}
            self.battle.d_stats = {0: test,   1: test,   2: test+1}

            c_exp_points = 2
            d_exp_points = 1

            c_points, d_points = self.battle.compare_stats()
            self.assertEqual(c_exp_points, c_points)
            self.assertEqual(d_exp_points, d_points)

    def test_determine_mvp(self):
        ## Ensure mvp gets the mvp calculation result from ##
        ## the trainer                                     ##
        trainer_mock = TestingTrainer
        trainer_mock.calculate_team_mvp = Mock()
        self.battle.winner = trainer_mock

        self.battle.determine_mvp()
        self.assertTrue(trainer_mock.calculate_team_mvp.called)

    def test_display_results(self):
        ## Ensure displays the winner of the battle and    ##
        ## their most valuable pokemon                     ##
        print('--------------------------------------------------')
        print('Display Results:')
        print()
      
        exp_display = 'JHibby defeated Amazon! Agile was the mvp.'

        challenger_mock = Mock(TestingTrainer)
        defender_mock   = Mock(TestingTrainer)
        challenger_mock.get_name = Mock(return_value='JHibby')
        defender_mock.get_name   = Mock(return_value='Amazon')

        self.battle.winner   = challenger_mock
        self.battle.loser    = defender_mock
        self.battle.mvp_name = 'Agile'

        # Direct console output for testing
        output = io.StringIO()
        sys.stdout = output

        self.battle.display_results()
        self.assertEqual(exp_display, output.getvalue().rstrip('\n'))

        # Reset console output
        sys.stdout = sys.__stdout__
        print(output.getvalue())

    def test_get_winner(self):
        ## Ensure displays the winner of the battle and    ##
        ## their most valuable pokemon                     ##
        trainer_mock          = TestingTrainer
        trainer_mock.get_name = Mock()
        self.battle.winner    = trainer_mock

        self.battle.get_winner()
        self.assertTrue(trainer_mock.get_name.called)

    #------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
