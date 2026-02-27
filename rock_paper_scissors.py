import random


# define a function for rock,paper, scisssors


def rock_paper_scissor():
    global rock, paper, scissor
    rock = "r"
    paper = "p"
    scissor = "s"
    global choices
    choices = (rock, paper, scissor)
    spin = random.choice(choices)
    return spin


# dictionary
emojis = {"r": "🪨", "p": "📃", "s": "✂️"}

while True:
    option = input("Rock, paper, or scissors? (r/p/s): ").lower()
    answer = rock_paper_scissor()
    if option not in choices:
        print(f"Invalid choice")
        continue
    if option == answer:
        print(f"It's a draw")
    elif (
        (option == scissor and answer == paper) or
        (option == paper and answer == rock) or
            (option == rock and answer == scissor)):
        print(f"You chose {emojis[option]}")
        print(f"Computer chose {emojis[answer]}")
        print(f"You won")
    else:
        print(f"You chose {emojis[option]}")
        print(f"Computer chose {emojis[answer]}")
        print(f"You lost")

    should_continue = input("Do you want to  continue? (y/n)").lower()
    if should_continue == "n":
        break
