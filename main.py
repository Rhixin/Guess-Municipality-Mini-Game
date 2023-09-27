#import csv
#
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    
#    for i in data:
#        if i[1] != "temp":
#            temperatures.append(int(i[1]))
#        
#    print(temperatures)

#import pandas
#
#data = pandas.read_csv("weather_data.csv")
#
##get max temp row data
#max_temp = data.temp.max()
#print(data[data.temp == max_temp])
#
##getmonday temp
#monday_data = data[data.day == "Monday"]
#print(monday_data.temp)
#
##create data frame
#data_dict = {
#    "students":["Amy","James","Angela"],
#    "scores":[76,75,89]
#}
#
#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")

#import pandas

#data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
#gray_squi = data[data["Primary Fur Color"] == "Gray"]
#red_squi = data[data["Primary Fur Color"] == "Cinnamon"]
#black_squi = data[data["Primary Fur Color"] == "Black"]
#
#
#gray_len = len(gray_squi)
#red_len = len(red_squi)
#black_len = len(black_squi)
#
#data_dict = {
#    "Fur Color":["Gray","Red","Black"],
#    "Count":[gray_len,red_len,black_len]
#}
#
#df = pandas.DataFrame(data_dict)
#df.to_csv("New_Data_Central_Park.csv")

import turtle
from turtle import Turtle,Screen
from Map_game import Mapgame
import time
from scoreboard import Scoreboard
import winsound

sc = Screen()
sc.title("CEBUANO LEGIT CHECK")
sc.bgpic("cebu_map.gif")
sc.setup(width=650,height=750)
sc.tracer(0)


icon = Mapgame()

score = Scoreboard()
score.update_score()

for i in range(1,53):
    icon.next()
    icon.color("black")
    sc.update()
    user_answer = sc.textinput(title= f"Number {i} out of 52", prompt="Guess what Municipality or City is pointed out?")
    
    if icon.current_answer == user_answer:
        winsound.PlaySound("eat_food.wav", winsound.SND_ASYNC)
        icon.color("black")
        score.score += 1
        score.update_score()
    else:
        winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)
        icon.color("red")
    
        
    icon.write_muni()     
    sc.update()
    
score.game_over()

icon.hideturtle()
sc.update()


turtle.mainloop()
