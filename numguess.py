import random as rd

print("===================================================")
print("    🎯 Welcome to the number guessing game 🎯")
print("===================================================")
print()
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is ?")
print()

def game ():

    rnum = rd.randint(1, 100)
    attempts = 0

    while True:

        guess = int(input("Enter your guess : "))
        if guess < rnum :
            print("Too low! Try again.")
            attempts +=1
            continue
        elif guess > rnum :
            print("Too high! Try again.")
            attempts +=1
            continue
        elif guess == rnum :
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            print()
            playagain = input("Would you like to play again? (y/n) : ")
            def plag():
                if playagain == "y":
                    game()
                elif playagain == "n":
                    return
                else:
                    print("Invalid input !")
                    plag()
            plag()




game()