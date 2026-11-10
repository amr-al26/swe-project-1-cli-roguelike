import random
from data import PHY_MOVES, MAGIC_MOVES


def attack(attacker, target, attack):
    if attack in PHY_MOVES:
        dmg = attack["dmg"] * (attacker["phy_dmg"]) - (target["phy_def"])

    if attack in MAGIC_MOVES:
        dmg = attack["dmg"] * (attacker["magic_dmg"]) - (target["magic_def"])

    if target["hp"] - int(dmg) < 0:
        target["hp"] = 0
        return dmg, "dead"
    else:
        target["hp"] -= int(dmg)

    return dmg, "alive"


def enemy_attack(attacker, target):
    if attacker["name"] != "Dragon":
        move = attacker["attack"]
    else:
        move = attacker[f"attack{random.randint(1, 2)}"]

    dmg = move["dmg"]
    target["hp"] -= (
        dmg - target[f"{'phy' if move['type'] == 'physical' else 'magic'}_def"]
    )
    return dmg


def healing(player, potion):
    if player["hp"] + potion["healing"] > player["max_hp"]:
        health_gained = player["max_hp"] - player["hp"]
        player["hp"] = int(player["max_hp"])
        return health_gained
    else:
        player["hp"] += potion["healing"]
        return potion["healing"]
