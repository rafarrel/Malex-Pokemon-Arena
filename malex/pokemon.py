# this program will initialize the pokemon class witH MAX_LEVEL , NAME , LEVEL STAT_GROUPS AND TOTAL_STATS
class Pokemon:
    # init method to set the objects attributes
    def __init__(self, name, level, hp, sp_defense, sp_attack, speed, attack, defense):
        self.MAX_LEVEL   = 100
        self.GROUP_TOTAL = 2
        self.hp          = hp
        self.sp_defense  = sp_defense
        self.defense     = defense
        self.sp_attack   = sp_attack
        self.speed       = speed
        self.attack      = attack
        self.name        = name
        self.level       = level
        self.stat_groups = {}
        self.total_stat  = None
        self.setup()

    def setup(self):
        self.calculate_stat_groups()
        self.stat_group_multiplier()
        self.calculate_total_stat()

    def calculate_stat_groups(self):
        self.stat_groups['Physical'] = (self.hp + self.speed) / self.GROUP_TOTAL
        self.stat_groups['Attack']   = (self.attack + self.sp_attack) / self.GROUP_TOTAL
        self.stat_groups['Defense']  = (self.defense + self.sp_defense) / self.GROUP_TOTAL

    def stat_group_multiplier(self):
        for key in self.stat_groups:
            self.stat_groups[key] *= (self.level / self.MAX_LEVEL)

    def calculate_total_stat(self):
        self.total_stat = 0
        for key in self.stat_groups:
            self.total_stat += self.stat_groups[key]

    # getters
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_stat_groups(self):
        return self.stat_groups

    def get_total_stat(self):
        return self.total_stat
