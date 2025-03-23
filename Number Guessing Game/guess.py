import random as rd
print("""
Hi! Welcome to the Mini Number Guessing Game!
Think a number b/w 1 to 100.
You have chances according the difficulty level.
    
Please select the difficulty:
    1. Easy (12 Chances)
    2. Medium (8 Chances)
    3. Hard (4 Chances)
""")
def game():
    chances = 0
    level = int(input("Enter Your Comfortable Level 1/2/3:  "))
    print()
    counter = 0
    if level == 1:
        chances += 12
        print("Now you have 12 Chances.")
    elif level == 2:
        chances += 8
        print("Now you have 8 Chances.")
    elif level == 3:
        chances += 4
        print("Now you have 4 Chances.")
    else:
        print("Enter the number between 1 and 3.") 

    number = rd.randrange(100)
    while counter < chances:
        counter += 1
        guess = int(input("Enter your Guess:"))
        print()
        if guess == number:
            print(f"Congratulations! You got it in {counter} Chances.")
            break
        elif counter >= chances and guess != number:
            print(f"Oops you lost. The number is {number}. Better Luck next time.")
            print()
        elif guess > number:
            print(f'Your guess is higher          ({counter} Chance lost.)')
            print()
        elif guess < number:
            print(f'Your guess is lesser           ({counter} Chance lost.)')
            print() 
game()
while True:
    
    print("""
Dou You Want to Play Again?
1. Yes
2. No
    """) 
    opinion = int(input("Enter Your Opinion 1 or 2:   "))   
    print()   
    if opinion == 1:
        game()
    elif opinion == 2:
        print("Hope You enjoyed this Game. Try my another Games also.")
        break
    else:
        print("Enter Right Opinion.")