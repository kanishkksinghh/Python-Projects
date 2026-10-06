import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <4:
            print("Password should be more than 4 characters long")
            return
        print(f"Generated password: {generate_password(length)}")
    except ValueError:
        print("Please enter a valid number.")
        
if __name__ == "__main__":
    main()
    