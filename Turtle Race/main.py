from turtle import Turtle, Screen
import random
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

is_race_on = False
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=800, height=400)
player_number = int(screen.textinput(title="Numbers of players", prompt="How many player are there in this run? "))
players = [item for item in screen.textinput(title="Names of players", prompt="Please list the names of players:").split()]

random_colors = []
for n in range(player_number):
    new_color = random.choice(colors)
    if new_color not in random_colors:
        random_colors.append(new_color)

print("Here the list of name and color matches!")
for n in range(player_number):
    print(players[n], "=", random_colors[n])

playing = True

def game():
    screen.clear()
    y_positions = [20, -10, 50, -40, 80, -70, 110, -100, 140]
    all_turtles = []

    for turtle_index in range(0, player_number):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(random_colors[turtle_index])
        new_turtle.goto(x=-380, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    are_you_ready = str(screen.textinput(title="Status", prompt="Are you ready?"))

    if are_you_ready == "yes":
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            #230 is 250 - half the width of the turtle.
            if turtle.xcor() > 370:
                is_race_on = False
                winning_color = turtle.pencolor()
                index = random_colors.index(winning_color)
                winner = players[index]

                print(f"\nThe winner is {winning_color}, congrats {winner}")


            #Make each turtle move a random amount.
            rand_distance = random.randint(0, 15)
            turtle.forward(rand_distance)

while playing:
    game()
    game_again = screen.textinput(title="One more turn?", prompt="Do you want to play again?")
    if game_again == "yes":
        playing = True



screen.exitonclick()