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

    #------------------------------------------------------------

    def test_simulation(self):
        ## Ensure simulation favors stronger trainer to win  ##
        ## between 60%-70% of the time                       ##
        pass

    def test_var_generation(self):
        ## Ensure simulation generates variability so that   ##
        ## stronger stat is still higher than lower stat     ##
        ## between -5 and +5 of its probability of being     ##
        ## higher                                            ##
        for test in range(100):
            stat = randint(1, 200)

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
