import random
i=random.randint(1,100)
while True:
    a=int(input("Guess a number from 1 to 100 "))
    if(a>i):
        print("Too High!")
        continue
    elif (a<i):
        print("Too Low!")
        continue
    else:
        print("Congratulations ypu guessed the number")
        break
