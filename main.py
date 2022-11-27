import random


Play = True
PlayerName = input("What Is Your name? : ")
print("Okay! Hello "+PlayerName + " Welcome To Number Game 😀 ")
print("You have three chances to guess the number we want, so be careful")

while Play:
    ComputerNumber = random.randint(1, 20)
    PlayerChance = 0

    while PlayerChance == 0:
        Chance = int(input("Enter Your Number:"))
        PlayerChance += 1
        if Chance == ComputerNumber:
            print("You win ")
            break
        if Chance < ComputerNumber:
            print("It's wrong! Your Guess Is Too Low (Number of chances left 2)")
        elif Chance > ComputerNumber:
            print("It's wrong!Your Guess Is Too High (Number of chances left 2) ")

    while PlayerChance == 1:
        Chance = int(input("Enter Your Number:"))
        PlayerChance += 1
        if Chance == ComputerNumber:
            print("You win ")
            break
        if ComputerNumber % 2 == 0:
            print("It's wrong!The desired number is even (Number of chances left 1)")
        elif ComputerNumber % 2 != 0:
            print("It's wrong! The desired number is odd (Number of chances left 1)")

    while PlayerChance == 2:
        Chance = int(input("Enter Your Number:"))
        PlayerChance += 1
        if Chance == ComputerNumber:
            print("You win ")
            break
        else:
            print(
                f"It's wrong!(You could not guess the desired number. The desired number is {ComputerNumber})")
            Again = input(f"{PlayerName} Are you playing again yes or no?")
        if Again == "no":
            print(f"Goodbye! {PlayerName}")
            Play = False
