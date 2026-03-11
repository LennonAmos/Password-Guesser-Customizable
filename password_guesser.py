#Variables
secret_password = "WordGuessing69"
guess = input("Enter your guess to begin:")
attempts = 0

#Main
if guess == secret_password:
    print("You are correct!")
elif guess != secret_password:
    attempts += 1
    print(f"Wrong! You have {3 - attempts} attempts left.")
    guess = input("Try again: ")