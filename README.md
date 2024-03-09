# Snake-Game-
# Snake game in Python


This code is for a basic snake game where the player controls a snake that grows in length each time it eats food. The objective is to eat as much food as possible without crashing into the walls or the snake's own body.

**Import Tkinter and Random:**
The code begins by importing the Tkinter module, which is used for creating the game's graphical user interface (GUI). It also imports the random module, which is used for generating random numbers to place the food in random positions within the game window.

**Game Constants:**
The next section defines several constants that set up the game's environment:

GAME_WIDTH and GAME_HEIGHT set the size of the game window.
SPEED defines how fast the game updates.
SPACE_SIZE is the size of each space in the grid, which is also the size of the snake's body parts and food.
BODY_PARTS sets the initial number of body parts the snake has.
SNAKE_COLOR, FOOD_COLOR, and BACKGROUND_COLOR set the colors for the snake, food, and background.
HIGH_SCORE_FILE is the name of a file used to store the high score.

**Snake Class:**
The Snake class defines the snake in the game:

It initializes the snake with a body of size BODY_PARTS.
coordinates is a list that stores the positions of the snake's body parts.
squares is a list of rectangle objects that represent the snake on the canvas.

**Food Class:**
The Food class is responsible for creating food in the game:

It has a method generate_food() which randomly places food in the game area, ensuring it doesn't spawn where the snake currently is.

**Game Functions:**
Several functions control the game's logic:

next_turn() handles the snake's movement and checks if the snake has eaten food or collided with walls or itself.
change_direction() changes the snake's direction based on user input.
check_collisions() checks if the snake has collided with the game boundaries or itself.
game_over() ends the game and updates the high score if necessary.
show_game_over() displays the game over screen with the player's score and high score.
update_high_score() updates the high score in the file.
get_high_score() retrieves the high score from the file.

**Tkinter Window Setup:**
The code then sets up the Tkinter window:

window is the main Tkinter window.
score is initialized to 0 and direction is set to 'down'.
A label is created to display the current score.
A canvas is created to draw the game elements like the snake and food.
The window's position is centered on the screen.

**Key Bindings:**
The arrow keys are bound to functions that change the direction of the snake.

**Game Initialization:**
A Snake object and a Food object are created, and the first next_turn() is called to start the game.

**Mainloop:**
Finally, window.mainloop() is called to start the Tkinter event loop, which keeps the window open and listens for events like key presses.

The game runs by repeatedly calling next_turn(), which moves the snake and checks for events like eating food or collisions. When the snake eats food, it grows in length, and the score increases. If the snake collides with the wall or itself, the game ends. The high score is read from and written to a file named "high_score.txt".

Each part of the code contributes to creating an interactive snake game with a graphical user interface, responding to user input, and keeping track of scores across games.




<img width="525" alt="image" src="https://github.com/Subhadip7/Snake-Game-/assets/95004440/6fded002-8ec5-4dff-abfd-2580e8fdade2">







<img width="526" alt="image" src="https://github.com/Subhadip7/Snake-Game-/assets/95004440/d649c8f4-8ccb-49e3-bc30-452959ebb724">





