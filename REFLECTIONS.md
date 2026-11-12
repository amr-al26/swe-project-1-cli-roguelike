1. Share one aspect of building this project you found challenging and how you
   overcame it.


An aspect of building this project that I found challenging was creating and storing data for the different aspects of the game. For example, the data for the starting classes, enemies, items, moves, etc. When starting my project, I knew I was going to use dictionaries to store all the data, but figuring out what exact values needed to be stored for every single thing was what I struggled with. To overcome this, I decided to just start off with a rough idea of what I needed, before any of the program was actually functional. As I worked on the program, I would change the way the data was stored, add more keys, or remove unused keys to fit what I needed. For example, all the moves are stored in two lists, "PHY_MOVES" and "MAGIC_MOVES"; originally, all the moves were stored in one list but had a key that would tell you the type of move. However, I found it tedious since it complicated differentiating between moves and decided to just put them in separate lists. Another example of changing the way I stored data is in "STARTING_MOVE_SET," which stores the starting move sets of the different classes. Originally, the moves were stored in four different keys, which were move_1, move_2, move_3, move_4, after working on the rest of the program I found this to not be the best way to store the starting move set so I decided to put them in a list stored in a key. Other sets of data that changed over time were "STARTING_CLASSES", "ITEMS", all the enemies, and more.


2. Share one technical concept that you gained a deeper understanding of
   through building this project. Explain that concept in simple terms and
   explain how it is used in your project.


One technical concept that I gained a deeper understanding of through building this project is helper functions. Helper functions are functions that do part of a bigger task. It is used all throughout my project through functions that print menus onto the screen for other functions to then process the input or have multiple functions contribute to one action by each function doing a part. Examples of this are how the "new_game" and "menu" functions work together: the menu function uses a helper function that prints a menu, and then the function itself takes input; one of the options is starting a new game, and if the user picks it, the new_game function runs. The function asks the user what starting class they would like to pick and sends their response back to menu, which returns that input for other functions to use.



