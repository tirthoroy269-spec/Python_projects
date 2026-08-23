import random
while True:
  ans=input("Roll a dice (y/n) ")
  if(ans.lower() == "y"):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print("(",dice1,",",dice2,")")
  elif (ans.lower()=="n"):
    print("Thanks for playing!")
    break
  else:
    print("Invalid Input")