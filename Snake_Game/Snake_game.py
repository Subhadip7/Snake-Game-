
from tkinter import*
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 600
SPACE_SIZE = 50
BODY_PARTS = 1
SNAKE_COLOR = "#34eba8"
FOOD_COLOR = "#eb3434"
BACKGROUND_COLOR = "#000000"
HIGH_SCORE_FILE = "high_score.txt"  # File to store and retrieve high score

class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        self.generate_food()

    def generate_food(self):
        while True:
            x = random.randint(1, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
            y = random.randint(1, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

            # Check if the generated coordinates overlap with the snake
            if (x, y) not in snake.coordinates:
                break

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food.generate_food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    global score
    update_high_score(score)
    high_score = get_high_score()
    canvas.delete(ALL)
    show_game_over(score, high_score)


def show_game_over(score, high_score):
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2 - 50,
                       font=('consolas', 40), text="GAME OVER", fill="red", tag="gameover")
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 30), text="Your Score: {}".format(score), fill="white", tag="gameover")
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2 + 50,
                       font=('consolas', 30), text="High Score: {}".format(high_score), fill="white", tag="gameover")

    
    
    
def update_high_score(current_score):
    try:
        with open(HIGH_SCORE_FILE, 'r') as file:
            content = file.read().strip()
            high_score = int(content) if content.isdigit() else 0
    except FileNotFoundError:
        high_score = 0

    if current_score > high_score:
        with open(HIGH_SCORE_FILE, 'w') as file:
            file.write(str(current_score))



def get_high_score():
    try:
        with open(HIGH_SCORE_FILE, 'r') as file:
            content = file.read().strip()
            if content.isdigit():
                return int(content)
            else:
                return 0
    except FileNotFoundError:
        return 0



window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()

