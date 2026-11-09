import random
from interface import PHY_MOVES, MAGIC_MOVES


def attack(attacker, target, attack, defend):
    if attack in PHY_MOVES:
        dmg = attack["dmg"] * (attacker["phy_dmg"] * (1 / 3)) - (
            target["phy_def"] * (1 / 3)
        )

    if attack in MAGIC_MOVES:
        dmg = attack["dmg"] * (attacker["magic_dmg"] * (1 / 3)) - (
            target["magic_def"] * (1 / 3)
        )

    if defend:
        dmg *= 1 / 3
        defend = False

    target["hp"] -= dmg
    return dmg
