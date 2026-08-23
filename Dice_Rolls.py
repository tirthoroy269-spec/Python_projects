import numpy as np
while True:
  ans=input("Roll a dice (y/n) ")
  if(ans.lower() == "y"):
    dice1=np.random.randint(1,7)
    dice2=np.random.randint(1,7)
    print("(",dice1,",",dice2,")")
  elif (ans.lower()=="n"):
    print("Thanks for playing!")
    break
  else:
    print("Invalid Input")
    continue