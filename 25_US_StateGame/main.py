import turtle
import pandas as pd


FONT = ("Arial", 8, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"      # path to image
screen.addshape(image)
turtle.shape(image)

# writer turtle
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

df = pd.read_csv("50_states.csv")

correct_user_guess = []
score = 0

state_list = df.state.to_list()

while len(correct_user_guess) < 50:

    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []

        for state in state_list:
            if state not in correct_user_guess:
                missing_states.append(state)

        # now state_list only contains the unknown state names
        new_df = pd.DataFrame(missing_states, columns=["state"])
        new_df.to_csv("missed_states.csv")

        break
    if answer_state in state_list:
        state_data = df[df.state == answer_state]
        x_cor = state_data.x.values[0]
        y_cor = state_data.y.values[0]

        writer.goto(x_cor, y_cor)
        writer.write(f"{answer_state}", align="center", font=FONT)

        score += 1
        correct_user_guess.append(answer_state)


# delete the writer object
del writer

# to find the coordinate in the turtle picture
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
