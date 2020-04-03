"""

    Simulation for the arena.

"""
from malex.pokemon import Pokemon
from malex.trainer import Trainer
from malex.arena   import Arena


class Simulation:

    def __init__(self, name):
        self.arena = Arena(name)

    def run(self):

        # Setup pokemon
        peakatchu         = Pokemon('Peakatchu'       ,  72, 105, 110, 140, 160,  90, 120)
        loud_meowth       = Pokemon('Loudmeowth'      ,  42,  80,  60, 110,  95,  82, 115)
        staryu_wars       = Pokemon('StaryuWars'      , 100, 185, 160, 200, 200, 210, 190)
        electrode_js      = Pokemon('ElectrodeJS'     ,  56, 155,  97, 124, 105, 110,  85)
        drago_fortnite    = Pokemon('DragoFortnite'   ,  75, 110, 120, 132, 145, 105, 110)
        zaptos_intolerant = Pokemon('ZaptosIntolerant', 100, 200, 210, 240, 225, 180, 195)

        # Setup trainers
        ash_ketchup = Trainer('Ash Ketchup', 10)
        ash_ketchup.add_pokemon(peakatchu)
        ash_ketchup.add_pokemon(zaptos_intolerant)
        ash_ketchup.calculate_team_stat_groups()

        jhibby = Trainer('JHibbsThaaaSteezWizard', 10)
        jhibby.add_pokemon(drago_fortnite)
        jhibby.add_pokemon(staryu_wars)
        jhibby.calculate_team_stat_groups()

        third = Trainer('ThirdRateTrainerNoOneCaresAbout', 2)
        third.add_pokemon(loud_meowth)
        third.add_pokemon(electrode_js)
        third.calculate_team_stat_groups()

        # Setup arena
        self.arena.set_challenger(ash_ketchup)
        self.arena.add_defender(jhibby)
        self.arena.add_defender(third)

        # Run arena
        self.arena.run_arena()

        # Exit arena
        self.arena.exit_arena()
