# create the trainer class with attributes of max_skill, mvp_variability , max_pokemon , name , skill_level pokemon ,
# and team_stat_groups
from malex import pokemon
import random
class Trainer:
    def __init__(self, name, skill_level, pokemon):
        self.MAX_SKILL = 10
        self.MVP_VARIABILITY = 10
        self.MAX_POKEMON = 6
        self.name = name
        self.skill_level = skill_level
        self.team = []
        self.team_stat_group = {}
        self.pokemon = pokemon

    def add_pokemon(self, pokemon):
        if len(self.team) < self.MAX_POKEMON:
            self.team.append(pokemon)
        else:
            print("pokemon can't be added.")

    def calculate_team_stat_groups(self):
        for x in self.team:
            for key in self.pokemon.stat_groups:
                self.team_stat_group[key] += self.pokemon.stat_groups[key]

    def stat_group_divisor(self):
        for key in self.team_stat_group:
            self.team_stat_group[key] /= (self.MAX_SKILL - self.skill_level + 1)

    @property
    def get_calculate_team_mvp(self):
        max_num = 0
        index   = 0
        for x in self.team:
            r1 = random.randint(1, 100)
            new_total_stat = self.pokemon.get_total_stat()*(r1/self.MVP_VARIABILITY)
            if max_num < new_total_stat:
                max_num = new_total_stat
                index += 1
        return self.team[index]

    def get_name(self):
        return self.name

    def get_skill_level(self):
        return self.skill_level

    def get_pokemon(self):
        return self.pokemon

    def get_team_stat_group(self):
        return self.team_stat_group
