from malex.battle import Battle
from unittest.mock import Mock
from random import randint
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
        #print('setUpClass()')
        pass

    @classmethod
    def tearDownClass(cls):
        #print('tearDownClass()')
        pass

    def setUp(self):
        #print('setUp()')
        pass

    def tearDown(self):
        #print('tearDown()')
        pass

    #------------------------------------------------------------

    def test_simulation(self):
        ## Ensure simulation is randomized and the stats   ##
        ## change                                          ##
        pass

        """
        # Generate values and run multiple tests for each
        # to ensure the stats are changing
        for sample in range(1):
            changed = False
            ch_phys = randint(1, 200)
            ch_att  = randint(1, 200)
            ch_dfn  = randint(1, 200)

            d_phys  = randint(1, 200)
            d_att   = randint(1, 200)
            d_dfn   = randint(1, 200)

            for test in range(2):
                challenger  = TestingTrainer(ch_phys, ch_att, ch_dfn)
                defender    = TestingTrainer(d_phys, d_att, d_dfn)
                test_battle = Battle(challenger, defender)

                test_battle.simulate()
                c_stats     = test_battle.c_stats
                d_stats     = test_battle.d_stats

                for key in c_stats:
                    if c_stats[key] > challenger.team_stat_groups[key]:
                        changed = True
                    if c_stats[key] < challenger.team_stat_groups[key]:
                        changed = True
                    if d_stats[key] > defender.team_stat_groups[key]:
                        changed = True
                    if d_stats[key] < defender.team_stat_groups[key]:
                        changed = True

            self.assertTrue(changed)
        """

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
