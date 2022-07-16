import pandas
import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.title('U.S States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")

game_is_on = True
score = 0
unknown_states = data.state.to_list()
while game_is_on:
    user_input = screen.textinput(title=f"{score}/50 States Guessed", prompt="What's another state name?").lower()
    if user_input == 'exit':
        break
    if user_input.title() in data.state.to_list():
        score += 1
        state = Turtle()
        state.penup()
        state.hideturtle()
        state_row = data[data.state == user_input.title()]
        state.goto(int(state_row.x), int(state_row.y))
        state.write(user_input)
        unknown_states.remove(user_input.title())
    screen.update()

unknown_states_csv =pandas.DataFrame(unknown_states)
unknown_states_csv.to_csv('states_to_learn.csv')
