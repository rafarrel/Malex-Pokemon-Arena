# this program will initialize the pokemon class witg MAX_LEVEL , NAME , LEVEL STAT_GROUPS AND TOTAL_STATS

class Pokemon:
    # init method to set the objects attributes
    def __init__(self, max_level, name, level, stat_groups, total_stat):
        self.__max_level = max_level
        self.__name = name
        self.__level = level
        self.__stat_groups = stat_groups
        self.__total_stat = total_stat

    # setters
    def set_max_level(self, max_level):
        self.__max_level = max_level

    def set_name(self, name):
        self.__name = name

    def set_level(self, level):
        self.__level = level

    def set_stat_groups(self, stat_groups):
        self.__stat_groups = stat_groups

    def set_total_stats(self, total_stats):
        self.__total_stat = total_stats

    # getters
    def get_max_level(self):
        return self.__max_level

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_stat_groups(self):
        return self.__stat_groups

    def get_total_stat(self):
        return self.__stat_groups
