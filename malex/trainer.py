# create the trainer class with attributes of max_skill, mvp_variability , max_pokemon , name , skill_level pokemon ,
# and team_stat_groups

class Trainer :
    def __init__(self, max_skill , mvp_variability , max_pokemon , name , skill_level , pokemon , team_stat_groups):
        self.__max_skill = max_skill
        self.__mvp_variability = mvp_variability
        self.__max_pokemon = max_pokemon
        self.__name = name
        self.__skill_level = skill_level
        self.__pokemon = pokemon
        self.__team_stat_group = team_stat_groups

    def set_max_skill(self,max_skill):
        self.__max_skill=max_skill

    def set_mvp_variability(self, mvp_variability):
        self.__mvp_variability = mvp_variability

    def set_max_pokemon(self, max_pokemon):
        self.__max_pokemon = max_pokemon

    def set_name(self, name):
        self.__name = name

    def set_skill_level(self,skill_level):
        self.__skill_level = skill_level

    def set_pokemon(self,pokemon):
        self.__pokemon = pokemon

    def set_team_stat_group(self,team_stat_group):
        self.__team_stat_group = team_stat_group

    def get_max_skill(self):
        return self.__max_skill

    def get_mvp_variability(self):
        return self.__mvp_variability

    def get_max_pokemon(self):
        return self.__max_pokemon

    def get_name(self):
        return self.__name

    def get_skill_level(self):
        return self.__skill_level

    def get_pokemon(self):
        return self.__pokemon

    def get_team_stat_group(self):
        return self.__team_stat_group
