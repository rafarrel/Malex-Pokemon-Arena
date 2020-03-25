from malex.battle import Battle
from random       import randint
from math         import fabs
import unittest


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
        c_att = randint(1, 200)
        c_dfn = randint(1, 200)

        d_phys = randint(1, 200)
        d_att = randint(1, 200)
        d_dfn = randint(1, 200)

        cls.challenger = TestingTrainer(c_phys, c_att, c_dfn)
        cls.defender = TestingTrainer(d_phys, d_att, d_dfn)
        cls.battle = Battle(cls.challenger, cls.defender)

    #------------------------------------------------------------

    def test_simulation(self):
        ## Ensure simulation favors stronger trainer to win  ##
        ## between 60%-70% of the time                       ##
        pass

    def test_var_generation(self):
        ## Ensure variability is generated so that the       ##
        ## new stat is outside desired quartiles +- (old     ##
        ## stat divided by four) a minimum of 5% and         ##
        # maximum of 10% of all generations.                 ##
        FREQ_L_BOUND = 0.05
        FREQ_U_BOUND = 0.1
        SD_DIV       = 4
        NUM_TESTS    = 10000

        print('--------------------------------------------------')
        print('Var Generation:\n')
        for key in self.challenger.team_stat_groups:
            c_orig = self.challenger.team_stat_groups[key]
            d_orig = self.defender.team_stat_groups[key]

            c_exp_diff = c_orig / SD_DIV
            d_exp_diff = d_orig / SD_DIV

            c_diff_greater_freq = 0
            d_diff_greater_freq = 0
            num_tests           = 0

            for test in range(NUM_TESTS):
                c_obs = self.battle.generate_variability(self.challenger.team_stat_groups, key)
                d_obs = self.battle.generate_variability(self.defender.team_stat_groups, key)

                c_diff = fabs(c_orig - c_obs)
                d_diff = fabs(d_orig - d_obs)

                if c_diff > c_exp_diff:
                    c_diff_greater_freq += 1
                if d_diff > d_exp_diff:
                    d_diff_greater_freq += 1

                num_tests += 1

            c_diff_greater_freq /= num_tests
            d_diff_greater_freq /= num_tests
            print(key)
            print('cdgf:', c_diff_greater_freq)
            print('ddgf:', d_diff_greater_freq)
            print()
            self.assertTrue(FREQ_L_BOUND <= c_diff_greater_freq <= FREQ_U_BOUND)
            self.assertTrue(FREQ_L_BOUND <= d_diff_greater_freq <= FREQ_U_BOUND)

        print('--------------------------------------------------')

    def test_compare(self):
        ## Ensure comparison gives points to the trainer   ##
        ## with the higher result for each stat group and  ##
        ## the trainer with the most points is the winner  ##
        pass

    def test_mvp(self):
        ## Ensure mvp gets the mvp calculation result from ##
        ## the trainer                                     ##
        pass

    def test_display(self):
        ## Ensure displays the winner of the battle and    ##
        ## their most valuable pokemon                     ##
        pass

    #------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
