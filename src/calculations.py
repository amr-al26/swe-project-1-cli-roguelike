import random
from interface import PHY_MOVES, MAGIC_MOVES


def attack(player, target, attack):
    if attack in PHY_MOVES:
        dmg = attack["dmg"] * (player["phy_dmg"] * (1 / 3)) - (
            target["phy_def"] * (1 / 3)
        )
        target["hp"] -= dmg
        return dmg

    if attack in MAGIC_MOVES:
        dmg = attack["dmg"] * (player["magic_dmg"] * (1 / 3)) - (
            target["magic_def"] * (1 / 3)
        )
        target["hp"] -= dmg
        return dmg


def defend(player, enemy, attack):
    if attack["type"] == "physical":
        dmg = attack["dmg"] * (enemy["phy_dmg"] * (1 / 3)) - (
            player["phy_def"] * (1 / 3)
        )
        player["hp"] -= dmg
        return dmg

    if attack["type"] == "magic":
        dmg = attack["dmg"] * (enemy["magic_dmg"] * (1 / 3)) - (
            player["magic_def"] * (1 / 3)
        )
        player["hp"] -= dmg
        return dmg
