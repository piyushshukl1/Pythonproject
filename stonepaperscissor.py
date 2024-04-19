import random
print("Welcome to Stone Paper Scissor")
def game():
    a=0
    b=0
    while True:
        user = int(input("Press: 1:Stone 2:Paper 3:Scissor 4:exit\n:-"))
        system = random.randint(1, 3)
        if user == 4:
            print("!!Bye!!")
            exit()
        elif system == user:
            print("Draw")
        elif system == 1 and user == 2:
            a +=1
            print("Computer choose Stone \n You Win")

        elif system == 1 and user == 3:
            b +=1
            print("Computer choose Stone \n You Lose")

        elif system == 2 and user == 1:
            b +=1
            print("Computer choose Paper \n You Lose")
        elif system == 2 and user == 3:
            a +=1
            print("Computer choose Paper \n You Win")
        elif system == 3 and user == 1:
            a +=1
            print("Computer choose Scissor \n You Win")
        elif system == 3 and user == 2:
            b +=1
            print("Computer choose Scissor \n You Lose")
        print(f"System win = {b} User win = {a}")
game()
