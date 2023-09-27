from turtle import Turtle
import turtle
import pandas

data = pandas.read_csv("municipalities_of_cebu.csv")
x_cor_data = data["x"].to_list()
y_cor_data = data["y"].to_list()
names = data["state"].to_list()

coordinates_tuples = []

for i in range(0,52):
    coordinates_tuples.append((x_cor_data[i],y_cor_data[i]))
    

class Mapgame(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(270)
        self.color("black")
        self.shapesize(1.5)
        self.current = 0
        self.point = 0
        self.current_answer = names[self.current]
    
    def next(self):
        self.penup()
        self.goto(coordinates_tuples[self.point])
        self.point += 1
        self.current_answer = names[self.current]
        
    def write_muni(self):
        self.pendown()
        self.write(names[self.current])
        self.current += 1
        
        
    
        