# file: main.py
# project: State Guessing Game
# purpose: An educational exercise where we use an image and csv file to create a game in which the user
#          attempts to name each of the fifty US States from memory
# credits: Thomas Franz wrote this instance of the program
#          This project is part of Dr Angela Yu's "100 Days of Code" python boot camp course on udemy
#          The image and csv were provided as course materials

import turtle   # for image libraries
import pandas   # for csv libraries

screen = turtle.Screen()
screen.title("U.S. States : Gotta Name 'em All!")

image = "blank_states_img.gif"              # Read and set up our image in the window
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")     # Read the names and coordinates from our csv file
all_states = data.state.to_list()           # Extract a list of state names from the csv data
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                    prompt="Name a State!").title()  # this applies proper capitalization

    # If the state guessed is valid and not already guessed, label it and keep track of it
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x) - 10, int(state_data.y - 2))   # write state name adjusted left a little
            t.write(answer_state)

    # If user writes Exit, we will write a list of states that were not guessed, then end execution
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

screen.exitonclick()
