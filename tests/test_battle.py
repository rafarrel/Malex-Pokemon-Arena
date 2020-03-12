from malex.battle import Battle
from unittest.mock import Mock
from random import randint
import unittest


class TestBattle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass()')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass()')

    def setUp(self):
        print('setUp()')

    def tearDown(self):
        print('tearDown()')

    #------------------------------------------------------------

    def test_simulation(self):
        ## Ensure simulation is randomized and the stats   ##
        ## change                                          ##
        pass

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

    def test_battle(self):
        ## Ensure battle results are different with the    ##
        ## same stats.
        pass

    #------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
