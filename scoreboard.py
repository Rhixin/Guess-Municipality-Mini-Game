import turtle
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto((70,-200))
        self.score = 0
        self.hideturtle()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.write(f"Score: {self.score}\nHighscore: {self.highscore}", font=("Courier", 16, "normal"))
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}\nHighscore: {self.highscore}", font=("Courier", 16, "normal"))
        
    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        
        self.update_score()