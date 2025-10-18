import random

def guess_number():
    
    number_to_guess = random.randint(1, 20)
    attempts = 0
    print("Welcome to the number guessing game!")
    print("I've chosen a number between 1 and 20. Can you guess it?")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            
            if 1 <= user_guess <= 20:
                attempts += 1

                if user_guess < number_to_guess:
                    print("Too low! Try again.")
                elif user_guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                    break
            else:
                print("Please enter a valid number between 1 and 20.")
        except ValueError:
            print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    guess_number()
