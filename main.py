import turtle
from turtle import Turtle, Screen
import pandas
t = Turtle()
screen = turtle.Screen()
screen.title("NIGERIAN MAP GAME")
image = "Nigeria_map.gif"
screen.addshape(image)
screen.setup(width=1000, height=600)
turtle.shape(image)
SCORE = 0

data = pandas.read_csv("states.csv")
states = data.states.to_list()
#
# def mouse_click_coor(x, y):
#     print(x, y)

guessed_state = []
end_of_game = False
while len(guessed_state) < 38:
    users_answer = screen.textinput(f"{len(guessed_state)}/{len(states)} states correct",
                                    prompt="Whats another states name?").title()

    if users_answer == "Exit":
        break
    if users_answer in states:
        t.hideturtle()
        t.penup()
        state_data = data[data.states == users_answer]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(state_data.states.item())
        guessed_state.append(users_answer)




# turtle.onscreenclick(mouse_click_coor)

turtle.mainloop()
