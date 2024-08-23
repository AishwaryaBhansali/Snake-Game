from turtle import Turtle
ALIGNMENT = "center"
FONT = "times new roman",24,"normal"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-60,260)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score : {self.score}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align = ALIGNMENT, font=FONT)

        
    def increment(self):
        self.score += 10
        self.clear()
        self.update()
        

        