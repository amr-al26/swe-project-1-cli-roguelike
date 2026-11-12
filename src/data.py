import art

PHY_MOVES = [
    # Targets One
    {"name": "Kick", "dmg": 20, "target": "single"},
    {"name": "Headbutt", "dmg": 30, "target": "single"},
    {"name": "Bow Shot", "dmg": 40, "target": "single"},
    {"name": "Lunge", "dmg": 55, "target": "single"},
    {"name": "Giant Slash", "dmg": 70, "target": "single"},
    {"name": "Knockout", "dmg": 90, "target": "single"},
    # Targets All
    {"name": "Rampage", "dmg": 35, "target": "all"},
    {"name": "Rapid Slashes", "dmg": 55, "target": "all"},
]

MAGIC_MOVES = [
    # Targets One
    {"name": "Agi", "dmg": 20, "target": "single"},
    {"name": "Bufu", "dmg": 30, "target": "single"},
    {"name": "Zio", "dmg": 40, "target": "single"},
    {"name": "Garu", "dmg": 55, "target": "single"},
    {"name": "Psyo", "dmg": 70, "target": "single"},
    {"name": "Freila", "dmg": 90, "target": "single"},
    # Targets All
    {"name": "Maeiha", "dmg": 35, "target": "all"},
    {"name": "Megido", "dmg": 55, "target": "all"},
]

BUFFS = [
    {"name": "Tarukaja", "effect": "increase phy dmg"},
    {"name": "Makakaja", "effect": "increase magic dmg"},
]

STARTING_MOVE_SET = [
    {
        "name": "Wizard",
        "moves": [PHY_MOVES[0], MAGIC_MOVES[1]],
    },
    {
        "name": "Magic Knight",
        "moves": [PHY_MOVES[0], MAGIC_MOVES[0]],
    },
    {
        "name": "Warrior",
        "moves": [PHY_MOVES[1], MAGIC_MOVES[0]],
    },
]

STARTING_CLASSES = [
    {
        "class_name": "Wizard",
        "hp": 75,
        "max_hp": 75,
        "phy_dmg": 5,
        "phy_def": 10,
        "magic_dmg": 18,
        "magic_def": 18,
        "move_set": STARTING_MOVE_SET[0]["moves"],
        "art": art.WIZARD,
        "dead": False,
    },
    {
        "class_name": "Magic Knight",
        "hp": 80,
        "max_hp": 80,
        "phy_dmg": 10,
        "phy_def": 12,
        "magic_dmg": 10,
        "magic_def": 12,
        "move_set": STARTING_MOVE_SET[1]["moves"],
        "art": art.KNIGHT,
        "dead": False,
    },
    {
        "class_name": "Warrior",
        "hp": 90,
        "max_hp": 90,
        "phy_dmg": 16,
        "phy_def": 18,
        "magic_dmg": 5,
        "magic_def": 10,
        "move_set": STARTING_MOVE_SET[2]["moves"],
        "art": art.WARRIOR,
        "dead": False,
    },
]

ITEMS = [
    {"name": "Health Potion", "healing": 50, "lvl": 1},
    {"name": "Health Potion", "healing": 100, "lvl": 2},
]

# ENEMIES
GOBLIN = {
    "name": "Goblin",
    "hp": 50,
    "attack": {"name": "swipe", "dmg": 10, "type": "physical"},
    "phy_def": 8,
    "magic_def": 8,
    "art": art.GOBLIN,
}
SKELETON = {
    "name": "Skeleton",
    "hp": 70,
    "attack": {"name": "bow shot", "dmg": 15, "type": "physical"},
    "phy_def": 5,
    "magic_def": 10,
    "art": art.SKELETON,
}
ZOMBIE = {
    "name": "Zombie",
    "hp": 75,
    "attack": {"name": "bite", "dmg": 20, "type": "physical"},
    "phy_def": 10,
    "magic_def": 5,
    "art": art.ZOMBIE,
}
GHOST = {
    "name": "Ghost",
    "hp": 75,
    "attack": {"name": "haunt", "dmg": 20, "type": "magic"},
    "phy_def": 30,
    "magic_def": 10,
    "art": art.GHOST,
}
WITCH = {
    "name": "Witch",
    "hp": 80,
    "attack": {"name": "curse", "dmg": 30, "type": "magic"},
    "phy_def": 10,
    "magic_def": 30,
    "art": art.WITCH,
}
# Bosses
CENTAUR = {
    "name": "Centaur",
    "hp": 200,
    "attack": {"name": "kick", "dmg": 25, "type": "physical"},
    "phy_def": 20,
    "magic_def": 10,
    "art": art.CENTAUR,
}
GRIM_REAPER = {
    "name": "The Grim Reaper",
    "hp": 125,
    "attack": {"name": "soul harvest", "dmg": 35, "type": "magic"},
    "phy_def": 20,
    "magic_def": 25,
    "art": art.GRIM_REAPER,
}
DRAGON = {
    "name": "Dragon",
    "hp": 250,
    "attack1": {"name": "fire breath", "dmg": 40, "type": "magic"},
    "attack2": {"name": "tail whip", "dmg": 40, "type": "physical"},
    "phy_def": 30,
    "magic_def": 30,
    "art": art.DRAGON,
}

ROUNDS = [
    {
        "index": 1,
        "enemies": [dict(GOBLIN), dict(GOBLIN)],
        "rewards": {
            "points": 3,
            "items": ITEMS[0],
            "moves": [PHY_MOVES[2], MAGIC_MOVES[2]],
        },
    },
    {
        "index": 2,
        "enemies": [dict(SKELETON), dict(SKELETON)],
        "rewards": {
            "points": 3,
            "items": ITEMS[0],
            "moves": [PHY_MOVES[6], MAGIC_MOVES[6]],
        },
    },
    {
        "index": 3,
        "enemies": [dict(GOBLIN), dict(ZOMBIE), dict(ZOMBIE)],
        "rewards": {"points": 5, "items": ITEMS[0]},
    },
    {
        "index": 4,
        "enemies": [dict(CENTAUR)],
        "rewards": {
            "points": 10,
            "items": ITEMS[1],
            "moves": [PHY_MOVES[3], MAGIC_MOVES[3]],
        },
    },
    {
        "index": 5,
        "enemies": [dict(GHOST), dict(GHOST), dict(GHOST)],
        "rewards": {"points": 5, "items": ITEMS[0]},
    },
    {
        "index": 6,
        "enemies": [dict(WITCH), dict(WITCH)],
        "rewards": {"points": 3, "items": ITEMS[0]},
    },
    {
        "index": 7,
        "enemies": [dict(GRIM_REAPER)],
        "rewards": {
            "points": 8,
            "items": ITEMS[1],
            "moves": [PHY_MOVES[7], MAGIC_MOVES[7]],
        },
    },
    {
        "index": 8,
        "enemies": [dict(SKELETON), dict(SKELETON), dict(ZOMBIE), dict(ZOMBIE)],
        "rewards": {
            "points": 5,
            "items": ITEMS[1],
            "moves": [PHY_MOVES[4], MAGIC_MOVES[4]],
        },
    },
    {
        "index": 9,
        "enemies": [dict(CENTAUR), dict(ZOMBIE), dict(GOBLIN)],
        "rewards": {"points": 8, "items": ITEMS[1]},
    },
    {"index": 10, "enemies": [dict(DRAGON)]},
]

runs = []
