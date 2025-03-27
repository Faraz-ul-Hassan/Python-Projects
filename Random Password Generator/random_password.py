import random as rd
import string as str
print("""
<---- Welcome to Password Generator ---->
Here you can generate password in an easy
      and efficient way.Just enter
       your requirtments.
""")
def password():
    print("""
    What type of password Do You Want?
          1. Randomly
          2. Or By Your special thing like (Your name)
    """)
    choice = int(input("Enter Your choice 1 or 2: "))
    if choice == 1:
        length = int(input("Enter the length for your password: "))
        numbers = input("Randomly numbers (y(For Yes) or n(For No)): ").lower() == 'y'
        symbols = input("Special characters (y(For Yes) or n(For No)): ").lower() == 'y'
        char = str.ascii_letters

        if numbers:
            char += str.digits
        if symbols:
            char += str.punctuation

        password = ''.join(rd.choice(char) for _ in range(length))
        # print()
        print(f"Your Generated Password is: -->{password}<--")
    elif choice == 2:
        length = int(input("Enter the length for your password: "))
        special = input("Enter the name of your favourite thing: ")
        password = ''.join(rd.choice(special) for _ in range(length))
        print(f"Your Generated Password is: -->{password}<--")
    else:
        print("Please enter the right choice.")
        password()
password()

while True:
    print("""
Do you want to generate password again:
          1. Yes
          2. No
""")
    choice = input("Enter 1 for Yes or Another character for No: ")
    if choice == "1":
        password()
    else:
        break