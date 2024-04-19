import random
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
total_len=int(input("Enter the total lenght of password :-"))
total_number=int(input("enter the total number you want in password:- "))
total_symbol=int(input("enter the total symbol you want in password:- "))
total_len = total_len - total_number - total_symbol
password=""
for char in range(1,total_number+1):
  password+=str(random.randint(0,9))
for char in range(1,total_symbol+1):
  password+=random.choice(symbols)
for char in range(1,total_len+1):
  password+=random.choice(letter)
print(f'Your generator password is :- {"".join(random.sample(password, len(password)))}')
