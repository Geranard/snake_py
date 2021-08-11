from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Right", fun=snake.right)
screen.onkeypress(key="Escape", fun=screen.exitonclick)

def update_screen():
    screen.update()
    time.sleep(0.05)

is_game_on = True

while is_game_on:
    # Update screen dan pergerakan ular
    update_screen()
    scoreboard.view()
    snake.move()

    # Detect makanan
    if snake.segment[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.refresh()
    
    x_curr = snake.segment[0].xcor()
    y_curr = snake.segment[0].ycor()

    # Detect collision sama tembok
    if x_curr>495 or x_curr<-495 or y_curr>395 or y_curr<-395:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision sama dirinya sendiri
    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment)<10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()