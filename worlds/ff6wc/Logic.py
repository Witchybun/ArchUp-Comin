from worlds.AutoWorld import LogicMixin, World
from worlds.ff6wc import Locations
from worlds.ff6wc.Locations import dragons


class LogicFunctions(LogicMixin):
    def _ff6wc_has_enough_characters(self, world, player):
        return self.has_group("characters", player, world.CharacterCount[player])

    def _ff6wc_has_enough_espers(self, world, player):
        return self.has_group("espers", player, world.EsperCount[player])

    def _ff6wc_has_enough_dragons(self, world, player):
        return self.has_group("dragons", player, world.DragonCount[player])