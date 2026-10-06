import random


def main():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Guess the Number between 1 to 100")

    while True:
        try:
            guess = int(input("Enter your Number: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low")
            elif guess > secret_number:
                print("Too High")
            else:
                print(
                    f"Congrats! You guessed the right number in {attempts} attempts."
                )
                break 

        except ValueError:
            print("Enter a valid integer")


if __name__ == "__main__":
    main()