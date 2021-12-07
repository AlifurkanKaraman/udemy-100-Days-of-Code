import turtle
import pandas


data = pandas.read_csv("81_states.csv")
states = data["state"].to_list()
x_coord = data["x"].to_list()
y_coord = data["y"].to_list()

screen = turtle.Screen()
text = turtle.Turtle()
screen.title("Turkey States Game")
image = "blank_states.gif"
screen.addshape(image)
turtle.shape(image)

# Record the correct guesses in a list
correct_guesses = []

# Keep track of the score
score = 0

# Use a loop to allow the user to keep guessing
while score < 81:
    # Convert the guess to Title case
    answer_state = screen.textinput(title=f"{score}/81 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    # Check if the guess is among the 81 states
    if answer_state in states and answer_state not in correct_guesses:
        correct_index = states.index(answer_state)
        correct_x_coord = x_coord[correct_index]
        correct_y_coord = y_coord[correct_index]

        # Write correct guesses onto the map
        text.hideturtle()
        text.penup()
        text.goto(correct_x_coord, correct_y_coord)
        text.write(arg=f"{answer_state}")

        correct_guesses.append(answer_state)
        score += 1


not_guessed_states = []
for state in states:
    if state not in correct_guesses:
        not_guessed_states.append(state)

states_data = pandas.DataFrame(not_guessed_states)
states_data.to_csv("not_guessed_states.csv")
