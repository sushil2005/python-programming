#this is a simple randomisation game
import random
number=int(input("enter a number between 1 to 20:"))
print(random.randint(1,20))
if number==random.randint(1,20):
    print("congratulatios your guess is correct")
else:
    print("sorry your guess is wrong")
    