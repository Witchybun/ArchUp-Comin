from BaseClasses import MultiWorld


def link_undertale_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))
    link_randomized_undertale_areas(world, player)


def link_randomized_undertale_areas(world: MultiWorld, player: int):
    if world.rando_area[player]:
        randomized_exits = []
        randomized_regions = []
        pairs = {}
        for (exits, region) in randomized_connections:
            randomized_exits.append(exits)
            randomized_regions.append(region)
        world.random.shuffle(randomized_regions)
        exits = "Old Home Exit"
        while len(randomized_regions) > 0:
            chosen_region = world.random.randrange(0, len(randomized_regions))
            start_chosen = chosen_region
            while banned_connections[exits] == randomized_regions[chosen_region] or (
                    len(randomized_regions) > 1 and randomized_regions[chosen_region] == "Core"):
                chosen_region += 1
                if chosen_region >= len(randomized_regions):
                    chosen_region = 0
                if start_chosen == chosen_region:
                    link_randomized_undertale_areas(world, player)
                    return False
            pairs[exits] = randomized_regions[chosen_region]
            exits = region_area_exit[randomized_regions[chosen_region]]
            randomized_regions.remove(randomized_regions[chosen_region])
        for exits in randomized_exits:
            world.get_entrance(exits, player).connect(world.get_region(pairs[exits], player))
            world.spoiler.set_entrance(exits, pairs[exits], "entrance", player)
    else:
        for (exit, region) in randomized_connections:
            world.get_entrance(exit, player).connect(world.get_region(region, player))
            world.spoiler.set_entrance(exit, region, "entrance", player)


# (Region name, list of exits)
undertale_regions = [
    ("Menu", ["New Game", "??? Exit"]),
    ("???", []),
    ("Ruins", ["Ruins Exit"]),
    ("Old Home", ["Old Home Exit"]),
    ("Snowdin Forest", ["Snowdin Forest Exit"]),
    ("Snowdin Town", ["Snowdin Town Exit", "Papyrus\" Home Entrance"]),
    ("Papyrus\" Home", []),
    ("Waterfall", ["Waterfall Exit", "Undyne\"s Home Entrance"]),
    ("Undyne\"s Home", []),
    ("Hotland", ["Cooking Show Entrance", "Lab Elevator"]),
    ("Cooking Show", ["News Show Entrance"]),
    ("News Show", ["Hotland Exit"]),
    ("True Lab", []),
    ("Core", ["Core Exit"]),
    ("New Home", ["New Home Exit"]),
    ("Barrier", []),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("??? Exit", "???"),
    ("New Game", "Ruins"),
    ("Ruins Exit", "Old Home"),
    ("Snowdin Forest Exit", "Snowdin Town"),
    ("Papyrus\" Home Entrance", "Papyrus\" Home"),
    ("Undyne\"s Home Entrance", "Undyne\"s Home"),
    ("Cooking Show Entrance", "Cooking Show"),
    ("News Show Entrance", "News Show"),
    ("Lab Elevator", "True Lab"),
    ("Core Exit", "New Home"),
    ("New Home Exit", "Barrier"),
]

randomized_connections = [
    ("Old Home Exit", "Snowdin Forest"),
    ("Snowdin Town Exit", "Waterfall"),
    ("Waterfall Exit", "Hotland"),
    ("Hotland Exit", "Core"),
]

banned_connections = {
    "Old Home Exit": "Ruins",
    "Snowdin Town Exit": "Snowdin Forest",
    "Waterfall Exit": "Waterfall",
    "Hotland Exit": "Hotland",
    "Core Exit": "Core",
}

region_area_exit = {
    "Ruins": "Old Home Exit",
    "Snowdin Forest": "Snowdin Town Exit",
    "Waterfall": "Waterfall Exit",
    "Hotland": "Hotland Exit",
    "Core": "Core Exit",
}
