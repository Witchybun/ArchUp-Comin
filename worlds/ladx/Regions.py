from BaseClasses import Region, MultiWorld



def create_regions(world: MultiWorld, player: int) -> None:
    class LARegion(Region):
        def __init__(self, name, player, world):
            super().__init__(self, name, player, world)

    class OverworldRegion(LARegion):
        def __init__(self, name: str, hint: str = None):
            super().__init__(self, name, player, world)
    
    class DungeonRegion(LARegion):
        def __init__(self, name: str, hint: str = None):
            super().__init__(self, name, player, world)
    
    class InteriorRegion(LARegion):
        def __init__(self, name: str, hint: str = None):
            super().__init__(self, name, player, world)
    
    class ItemRegion(LARegion):
        def __init__(self, name: str, item_required):
            super().__init__(self, name, player, world)

    dungeon1 = DungeonRegion('Dungeon 1')
    dungeon2 = DungeonRegion('Dungeon 2')
    dungeon3 = DungeonRegion('Dungeon 3')
    dungeon4 = DungeonRegion('Dungeon 4')
    dungeon5 = DungeonRegion('Dungeon 5')
    dungeon6 = DungeonRegion('Dungeon 6')
    dungeon7 = DungeonRegion('Dungeon 7')
    dungeon8 = DungeonRegion('Dungeon 8')
    dungeon9 = DungeonRegion('Dungeon 9')

    # Mabe Village
    mabe_village = OverworldRegion("Mabe Village")
    papahl_hoise = InteriorRegion("Papahl House")
    rooster_grave = InteriorRegion("Rooster Grave")
    madam_bowwow = InteriorRegion("Madam Bowwow")
    ulrira = InteriorRegion("Ulrira")
    mabe_phone = InteriorRegion("Mabe Phone")
    library = InteriorRegion("Library")
    trendy_shop = InteriorRegion("Trendy Shop")
    start_house = InteriorRegion("Start House") # hmmm
    dream_hut = InteriorRegion("Dream Hut")
    kennel = InteriorRegion("Kennel")

    # Sword Beach
    sword_beach = OverworldRegion("Sword Beach")
    banana_seller = InteriorRegion("Banana Seller")
    boomerang_cave = InteriorRegion("Boomerage Cave")
    ghost_house = InteriorRegion("Ghost House")

    # Forest
    forest = OverworldRegion("Forest")
    forest_heartpiece = OverworldRegion("Forest Heartpiece")
    # This is a check, not a Region
    # WITCH_HUT = InteriorRegion("Witch's Hut")
    crazy_tracy_hut_outside = OverworldRegion("Outside Crazy Tracy's Hut")
    crazy_tracy_hut = InteriorRegion("Crazy Tracy's Hut")
    forest_madbatter = InteriorRegion("Forest Madbatter")
    forest_cave = InteriorRegion("Forest Cave")
    forest_toadstool = InteriorRegion("Forest Toadstool")
    hookshot_cave = InteriorRegion("Hookshot Cave")

    # Swamp
    swamp = OverworldRegion("Swamp")
    outside_writes_house = OverworldRegion("Outside Write's House")
    writes_house = InteriorRegion("Write's House")
    writes_cave = InteriorRegion("Write's Cave")

    # Swamp
    graveyard = OverworldRegion("Graveyard")
    graveyard_photo = InteriorRegion("Graveyard Photo House")
    graveyard_cave = InteriorRegion("Graveyard Cave")
    moblin_cave = InteriorRegion("Moblin Cave")

    # Ukuku Prairie
    ukuku_prarie = OverworldRegion("Moblin Cave")
    ukuku_prarie_left_phone = InteriorRegion("Ukuku Left Phone")
    ukuku_prarie_right_phone = InteriorRegion("Ukuku Right Phone")
    ukuku_prarie_left_fairy = InteriorRegion("Ukuku Left Fairy")
    ukuku_prarie_left_cave_2 = InteriorRegion("Ukuku Left Cave 2")
    mamu = InteriorRegion("Mamu")
    prairie_island_seashell = OverworldRegion("Prarie_Island_Seashell")
    # I suspect this is a connection and not a region
    # castle_jump_cave = InteriorRegion("Castle Jump Cave")

    left_bay = OverworldRegion("Left Bay")
    tiny_island = OverworldRegion("Tiny Island")
    prarie_plateau = OverworldRegion("Prarie Plateau")

    prairie_cave = InteriorRegion("Prarie Cave")
    
    bay_madhatter_connector = InteriorRegion("Bay Madbatter Connector")
    bay_madhatter = InteriorRegion("Bay Madbatter")

    seashell_mansion = InteriorRegion("Seashell Mansion")
    bay_water = OverworldRegion("Bay Water")
    fisherman = OverworldRegion("Fisherman")

    # Castle
    richards_house = InteriorRegion("Richard's House")
    richards_cave = InteriorRegion("Richard's Cave")
    richards_maze = OverworldRegion("Richard's Maze")
    castle_outside_gate = OverworldRegion("Outside the Castle Gate")
    castle_phone = InteriorRegion("Castle Phone")
    castle_courtyard = OverworldRegion("Castle Courtyard")
    castle_front_door = OverworldRegion("Castle Front Door")
    castle_moat = OverworldRegion("Castle Moat")
    castle_top_outside = OverworldRegion("Castle Top Outside")
    castle_top_inside = InteriorRegion("Castle Top Inside")

    # Animal Village
    animal_village = OverworldRegion("Animal Village")
    cook_house = InteriorRegion("Cook House")
    goat_house = InteriorRegion("Goat House")

    mermaid_statue = OverworldRegion("Mermaid Statue")
    
    animal_phone = InteriorRegion("Animal Phone")
    animal_house1 = InteriorRegion("Animal House 1")
    animal_house2 = InteriorRegion("Animal House 2")
    animal_house3 = InteriorRegion("Animal House 3")
    animal_house4 = InteriorRegion("Animal House 4")
    animal_house5 = InteriorRegion("Animal House 5")

    animal_village_bomb_cave = InteriorRegion("Animal Village Bomb Cave")
    animal_village_bomb_cave_heartpiece = InteriorRegion("Animal Village Bomb Cave Heartpiece")

    # Desert
    desert = OverworldRegion("Desert")    
    lanmolas = InteriorRegion("Lanmolas")
    desert_cave = InteriorRegion("Desert Cave")

    armos_maze = OverworldRegion("Armos Cave")
    armos_temple = InteriorRegion("Armos Temple")
    armos_fairy = InteriorRegion("Armos Fairy")

    # Taltal
    egg = OverworldRegion("Windfish Egg")
    obstacle_cave = InteriorRegion("Obstacle Cave")
    lower_right_taltal = OverworldRegion("Lower Right Taltal")
    papahl_cave = InteriorRegion("Papahl Cave")
    
    below_right_taltal = OverworldRegion("Below Right Taltal")
    heartpiece_swim_cave = InteriorRegion("Heartpiece Swim Cave")
    mambo = InteriorRegion("Mambo")

    # Raft Game
    raft_house = InteriorRegion("Raft Game")
    raft_return_upper = OverworldRegion("Raft Return Upper")
    raft_return_lower = OverworldRegion("Raft Return Lower")
    outside_raft_house = OverworldRegion("Outside Raft House")
    raft_exit = OverworldRegion("Raft Exit")

    outside_rooster_house = OverworldRegion("Outside Rooster House")
    bird_cave = InteriorRegion("Bird Cave")
    multichest_cave = InteriorRegion("Chest Puzzle Cave")
    water_cave_hole = InteriorRegion("Water Cave Hole")
    multichest_cave_outside = OverworldRegion("Outside Chest Puzzle Game")
    right_taltal_connector1 = InteriorRegion("Right Taltal Connector 1")
    right_taltal_connector_outside1 = OverworldRegion("Right Taltal Connector Outside 1")
    right_taltal_connector2 = InteriorRegion("Right Taltal Connector 2")
    right_taltal_connector3 = InteriorRegion("Right Taltal Connector 3")
    right_taltal_connector_outside2 = OverworldRegion("Right Taltal Connector Outside 2")
    right_taltal_connector4 = InteriorRegion("Right Taltal Connector 4")
    d7_plataeu = OverworldRegion("D7 Plataeu")
    d7_tower = OverworldRegion("D7 Tower")

    mountain_bridge_staircase = OverworldRegion("Mountain Bridge Staircase")
    # I think
    left_right_connector_cave_right = InteriorRegion("Left Right Connector Cave (Right)")
    left_right_connector_cave_left = InteriorRegion("Left Right Connector Cave (Left)")

    taltal_boulder_zone = OverworldRegion("Taltal Boulder Zone")
    taltal_madbatter6  = InteriorRegion("Taltal Mad Batter")
