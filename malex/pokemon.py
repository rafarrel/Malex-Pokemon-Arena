# this program will initialize the pokemon class witg MAX_LEVEL , NAME , LEVEL STAT_GROUPS AND TOTAL_STATS

class Pokemon:
    # init method to set the objects attributes
    def __init__(self):
        self.__max_level = self
        self.__name = self
        self.__level = self
        self.__stat_groups = self
        self.__total_stat = self

    # getters
    def get_max_level(self):
        if self.__max_level > 100:
            print("Max level has been reached !")
        else:
            return self.__max_level

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_stat_groups(self):
        return self.__stat_groups

    def get_total_stat(self):
        return self.__stat_groups
