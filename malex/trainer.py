# create the trainer class with attributes of max_skill, mvp_variability , max_pokemon , name , skill_level pokemon ,
# and team_stat_groups

class Trainer :
    def __init__(self, name , skill_level , pokemon , team_stat_groups):
        self.MAX_SKILL = 10
        self.MVP_VARIABILITY = 10
        self.MAX_POKEMON = 6
        self.name = name
        self.skill_level = skill_level
        self.pokemon = pokemon
        self.team_stat_group = team_stat_groups


    def get_name(self):
        return self.name

    def get_skill_level(self):
        return self.skill_level

    def get_pokemon(self):
        return self.pokemon

    def get_team_stat_group(self):
        return self.team_stat_group
