import random
from data import PHY_MOVES, MAGIC_MOVES


K = 50


def attack(attacker, target, attack):
    if attack in PHY_MOVES:
        atk, df = attacker["phy_dmg"], target["phy_def"]

    if attack in MAGIC_MOVES:
        atk, df = attacker["magic_dmg"], target["magic_def"]

    dmg = int(attack["dmg"] * (1 + atk / K) * (K / (K + df)))

    if target["hp"] - dmg < 0:
        target["hp"] = 0
        return dmg, "dead"
    else:
        target["hp"] -= dmg

    return dmg, "alive"


def enemy_attack(attacker, target, defend):
    if attacker["name"] != "Dragon":
        move = attacker["attack"]
    else:
        move = attacker[f"attack{random.randint(1, 2)}"]

    df = target[f"{'phy' if move['type'] == 'physical' else 'magic'}_def"]
    dmg = int(move["dmg"] * (K / (K + df)))

    if defend:
        dmg //= 2

    if target["hp"] - dmg <= 0:
        target["hp"] = 0
    else:
        target["hp"] -= dmg

    return dmg, move


def healing(player, potion):
    if player["hp"] + potion["healing"] > player["max_hp"]:
        health_gained = player["max_hp"] - player["hp"]
        player["hp"] = int(player["max_hp"])
        return health_gained
    else:
        player["hp"] += potion["healing"]
        return potion["healing"]
