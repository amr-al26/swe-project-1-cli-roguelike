# CLI App

### Set Up
```
cd swe-project-1-cli-app
python3 -m venv .venv
source .venv/bin/activate
```

### Brief Description

- This CLI App is a turn based RPG Roguelike where you get to go round after round battling enemies until you lose to make it to the end.
- The game consists of 10 rounds of enemies and features varies ways of progression as you go through the waves of enemies
- The end goal is to beat the final boss in the last round

### Game Loop

- The app opens up to a menu of choosing between starting a new game, looking through records of already played runs, and quitting the program.
- Starting a new game prompts the user with the choice of 3 starting classes, each with unique starting moves and stats
- After picking a starting class the program asks for a name and then gives a brief message
- After the message you are dropped into the actual gameplay where you start the first round
- When beating a round you gain stat points that can be used to upgrade your character, healing potions to use in the middle of battle, and sometimes unlock new moves to add to your move set
- If the player drops to 0 hp they die and are given a summary of their run, the summary can be viewed again in the records option in the main menu
- Going through all 10 rounds and beating the final boss is the only way to win a run, the user is shown a summary which can be viewed in records