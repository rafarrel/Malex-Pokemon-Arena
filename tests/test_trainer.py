import unittest
from malex.trainer import Trainer
from unittest import TestCase
from malex.pokemon import Pokemon


class TestTrainer(unittest.TestCase):

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
    def test_add_pokemon(self):
        # init the trainer constructor
        name = "Mario"
        skill_level = 6
        MAX_POKEMON = 6
        trainer = Trainer(name, skill_level)
        trainer.team.append(Pokemon)
        # test to see if a pokemon can be added if less than MAX_POKEMON
        if len(trainer.team) >= MAX_POKEMON:
            self.assertTrue(trainer.add_pokemon(), MAX_POKEMON)

    def test_calculate_team_stat_groups(self):
        name = "Mario"
        skill_level = 6
        trainer = Trainer(name, skill_level)
        # create pokemon one
        char_name = "Charizard"
        char_hp = 55
        char_level = 15
        char_attack = 65
        char_sp_attack = 88
        char_speed = 30
        char_defense = 120
        char_sp_defense = 75
        pokemon_one = Pokemon(char_name, char_level, char_hp, char_sp_defense,
                              char_sp_attack, char_speed, char_attack, char_defense)
        pokemon_one.calculate_stat_groups()
        pokemon_one.calculate_total_stat()
        trainer.team.append(pokemon_one)



        # create pokemon two
        squ_name = "Squirtle"
        squ_hp = 22
        squ_level = 10
        squ_attack = 25
        squ_sp_attack = 55
        squ_speed = 15
        squ_defense = 170
        squ_sp_defense = 175
        pokemon_two = Pokemon(squ_name, squ_level, squ_hp, squ_sp_defense,
                              squ_sp_attack, squ_speed, squ_attack, squ_defense)
        pokemon_two.calculate_stat_groups()
        pokemon_two.calculate_total_stat()
        trainer.team.append(pokemon_two)

    def test_get_name(self):
        name = "Lucid"
        skill_level = 4
        trainer = Trainer(name, skill_level)
        self.assertTrue(trainer.get_name(), name)

    def test_get_level(self):
        name = "kancor"
        skill_level = 9
        trainer = Trainer(name, skill_level)
        self.assertTrue(trainer.get_skill_level(), skill_level)


if __name__ == '__main__':
    unittest.main()
