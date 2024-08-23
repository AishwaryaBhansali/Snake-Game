from PIL import Image,ImageTk
from turtle import Turtle, Screen 
import time
from snake import Snake
from food import Food
from score import ScoreBoard


snake = Snake()
food = Food()
score = ScoreBoard()

#Resize image
img = Image.open("images/bg.gif")
img = img.resize((600,600))
img.save("images/bg.gif")

#screen commands
screen = Screen()
screen.title("Snake")
screen.setup(width=600,height=600)
screen.bgpic("images/bg.gif")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.bottom, "Down")
screen.onkey(snake.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    #Detect tail collision
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_on = False
            score.game_over()
    


screen.exitonclick()