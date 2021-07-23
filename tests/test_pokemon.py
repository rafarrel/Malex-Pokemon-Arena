# Pokemon Tests
# @author Mario Vega
import unittest
from unittest import TestCase

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

    def test_calculate_total_stat(self):
        name = "Charizard"
        hp = 55
        level = 15
        attack = 65
        sp_attack = 88
        speed = 30
        defense = 120
        sp_defense = 75
        expected_p_value = (hp + speed) / 2
        expected_a_value = (attack + sp_attack) / 2
        expected_d_value = (defense + sp_defense) / 2
        total_expected = expected_a_value + expected_d_value + expected_p_value
        pokemon = Pokemon(name, level, hp, sp_defense, sp_attack, speed, attack, defense)
        pokemon.calculate_stat_groups()
        pokemon.calculate_total_stat()
        self.assertEqual(pokemon.get_total_stat(), total_expected)

    def test_get_name(self):
        name = "Squirtle"
        hp = 22
        level = 10
        attack = 25
        sp_attack = 55
        speed = 15
        defense = 170
        sp_defense = 175
        pokemon = Pokemon(name, level, hp, sp_defense, sp_attack, speed, attack, defense)
        self.assertEqual(pokemon.get_name(), name)

    def test_get_level(self):
        name = "Pikachu"
        hp = 30
        level = 20
        attack = 33
        sp_attack = 45
        speed = 77
        defense = 90
        sp_defense = 110
        pokemon = Pokemon(name, level, hp, sp_defense, sp_attack, speed, attack, defense)
        self.assertEqual(pokemon.get_level(), level)


if __name__ == '__main__':
    unittest.main()
