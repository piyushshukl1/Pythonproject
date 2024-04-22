import random

def hangman(life):
    print("+---------")
    print("|", end="")
    for i in range(5):
        print(" ", end="")
    print("|")
    print("|", end="")
    for i in range(5):
        print(" ", end="")
    print("|")
    print("|", end="")
    for i in range(5):
        print(" ", end="")
    if life < 7:
        print("0")
    else:
        print()
    print("|", end="")
    for i in range(4):
        print(" ", end="")
    if life < 6:
        print("/", end="")

    if life < 5:
        print("|", end="")

    if life < 4:
        print("\\")
    else:
        print()

    print("|", end="")
    for i in range(5):
        print(" ", end="")
    if life < 3:
        print("|")
    else:
        print()
    print("|", end="")
    for i in range(4):
        print(" ", end="")
    if life < 2:
        print("/", end="")

    if life < 1:
        print(" ", end="")
        print("\\")
    else:
        print()

    print("|")
    print("+-------------------")


def game():
    words = ["hello", "dog", "cat", "kite", "ball", "class", "laptop"]
    computer = ()
    computer = random.choice(words)
    life = 7
    found = []
    for i in computer:
        found += "_"
    while found != computer:
        hangman(life)
        print(f"You have {life} left")
        print(found)
        if life < 1:
            print("you lost")
            a = input("y to play again n to exit :- ")
            if a=='y':
                return True
            else:
                return False
        elif "_" not in found:
            print("You win")
            a = input("y to play again n to exit :- ")
            if a == 'y':
                return True
            else:
                return False
        u = input("enter letter :-")
        if u not in computer:
            life -= 1
        for i in range(len(computer)):
            if u == computer[i]:
                found[i] = u


if game():
    game()
else:
    exit()
