import random
moves = {
    "r": r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

    "p": r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",

    "s": r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}
while True:
    user=input("Choose from r(rock)/p(paper)/s(scissors) ")
    comp=random.choice(list(moves.keys()))
    print("You choose ",moves[user])
    print("Computer Choose ",moves[comp])
    if user not in moves:
      print("Invalid Input")
      continue
    elif   (user=="r" and comp=="s") or (user=="s" and comp=="p") or (user=="p" and comp=="r") :
           print("You won")
    elif (user=="r" and comp=="r") or (user=="s" and comp=="s") or (user=="p" and comp=="p") :
           print("Draw")
    elif (user=="r" and comp=="p") or (user=="s" and comp=="r") or (user=="p" and comp=="s") :
           print("You Lost")
    
    y=input("Do you want to continue (y/n)?\t")
    if(y.lower()=="y"):
            continue
    elif(y.lower()=="n"):
            print("Thank you for playing")
            break
    else:
            print("Invalid Input")