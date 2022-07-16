import turtle
from turtle import Screen,Turtle

screen = Screen()
screen.title('U.S States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

import pandas

data = pandas.read_csv("50_states.csv")
states = []
coordinates = []
for index in range(len(data)):
    if data.state[index] != 'state':
        states.append(data.state[index].lower())
        new_tuple = (data.x[index],data.y[index])
        coordinates.append(new_tuple)
print(states)

game_is_on = True
score = 0
while game_is_on:
    user_input = screen.textinput(title=f"{score}/50 States Guessed", prompt="What's another state name?").lower()
    if user_input in states:
        score += 1
        state = Turtle()
        state.penup()
        state.hideturtle()
        index = states.index(user_input.lower())
        state.goto(coordinates[index])
        state.write(user_input)
    screen.update()


screen.exitonclick()