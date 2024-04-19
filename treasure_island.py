import time
import os
a=True
while a:
  os.system('clear')
  print("welcome to Treasure island ")
  print("you are at cross road ")
  choice1 = input("where do you want to go ? left or right ")
  if choice1 == "left":
    choice2 = input("you have come to lake. there is an island in the middle of the lake. type wait to wait for a boat. type swim to swim across ")
    if choice2 == "wait":
      choice3 = input("you arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue. which colour do you choose? ")
      if choice3 == "red":
        print("it is a room full of fire. game over")
        time.sleep(2)
        b=input("\'y\' want to play again \'n\' to exit: ")
        if b=="n":
                a=False
                print("!!!!bye!!!!")
      elif choice3 == "yellow":
        print("you found the treasure! you win!")
      elif choice3 == "blue":
        print("you enter a room of beasts. game over")
        time.sleep(2)
        b=input("\'y\' want to play again \'n\' to exit: ")
        if b=="n":
                a=False
                print("!!!!bye!!!!")
      else:
        print("you chose a door that does not exist. game over")
    else:
      print("you got attacked by an angry fishes. game over")
      time.sleep(2)
      b=input("\'y\' want to play again \'n\' to exit: ")
      if b=="n":
              a=False
              print("!!!!bye!!!!")
  else:
    print("you are lost in forest. Game Over!!!")
    time.sleep(2)
    b=input("\'y\' want to play again \'n\' to exit: ")
    if b=="n":
            a=False
            print("!!!!bye!!!!")
  
