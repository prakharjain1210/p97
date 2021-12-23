import random
number=random.randint(1,9)
chances=0
while(chances<=5):
    guess=int(input("enter you number"))
    if(guess==number):
        print("congratulations you won")
        break
    elif(guess<number):
        print("enter a higher number")
    else:
        print("enter a lower number")
    chances+=1
if(not chances<5):
    print("you lose")


