from calculations import healing, enemy_attack
from data import ITEMS

test_player1 = {"max_hp": 100, "hp": 0}


def test_healing():
    assert healing(dict(test_player1), ITEMS[0]) == 50
    assert healing(dict(test_player1), ITEMS[1]) == 100


test_player2 = {"max_hp": 100, "hp": 25}


def test_healing_stops_at_max_hp():
    assert healing(dict(test_player2), ITEMS[1]) == 75


test_player3 = {"hp": 50, "phy_def": 5, "magic_def": 5}
test_enemy1 = {
    "name": "goblin",
    "attack": {"name": "swipe", "dmg": 20, "type": "physical"},
}

test_enemy2 = {
    "name": "ghost",
    "attack": {"name": "haunt", "dmg": 30, "type": "magic"},
}


def test_enemy_attack():
    assert enemy_attack(test_enemy1, dict(test_player3), False) == (
        15,
        {"name": "swipe", "dmg": 20, "type": "physical"},
    )

    assert enemy_attack(test_enemy2, dict(test_player3), False) == (
        25,
        {"name": "haunt", "dmg": 30, "type": "magic"},
    )


def test_enemy_attack_with_defend():
    assert enemy_attack(test_enemy1, dict(test_player3), True) == (
        7,
        {"name": "swipe", "dmg": 20, "type": "physical"},
    )

    assert enemy_attack(test_enemy2, dict(test_player3), True) == (
        12,
        {"name": "haunt", "dmg": 30, "type": "magic"},
    )
