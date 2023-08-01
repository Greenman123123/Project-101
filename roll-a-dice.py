import random

response = input("Roll the dice? ")

if(response == "y"):
  no = random.randint(1,6)
  print(no)
  response = input("Would you like to roll the dice again? ")
  if(response == "y"):
    no = random.randint(1,6)
    print(no)
elif(response == "n"):
  print("Ok")