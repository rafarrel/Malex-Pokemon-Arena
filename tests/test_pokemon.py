import unittest
from malex.pokemon import Pokemon


class TestPokemon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print('setUpClass()')
        pass

    @classmethod
    def tearDownClass(cls):
        # print('tearDownClass()')
        pass

    def setUp(self):
        # print('setUp()')
        pass

    def tearDown(self):
        # print('tearDown()')
        pass

    # ------------------------------------------------------------

    def test_calculate_stat_groups(self):
        # test works!
        name = "Charizard"
        hp = 55
        level = 15
        attack = 65
        sp_attack = 88
        speed = 30
        defense = 120
        sp_defense = 75
        expected_value = (hp + speed) / 2
        pokemon = Pokemon(name, level, hp, sp_defense, sp_attack, speed, attack, defense)
        pokemon.calculate_stat_groups()

        self.assertEqual(pokemon.stat_groups['Physical'], expected_value)


if __name__ == '__main__':
    unittest.main()
