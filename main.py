import random

ComputerNumber = random.randint(1, 20)

PlayerName = input("Hello, What Is Your name? : ")
PlayerChance = 0
print("Okay! "+PlayerName +" Welcome To Number Game 😀 ")


while PlayerChance <= 5:
    Chance = (input("Enter Your Number:"))
    PlayerChance += 1
    if Chance < ComputerNumber:
        print("Your Guess Is Too Low")
    elif Chance > ComputerNumber:
        print("Your Guess Is Too High")
    if Chance == ComputerNumber:
        print("You Win ")
        break
    else:
        ("You could not guess the desired number. The desired number is "+ComputerNumber+" ")
