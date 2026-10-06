import random

def main():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    while True:
       user_choice = input("Choose rock, paper or scissors or ('quit): ").lower().strip()
       if user_choice == "quit":
           break
       
       if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue
       
       computer_choice = random.choice(choices)
       print(f"Computer Score: {computer_choice}")
       
       if user_choice == computer_choice:
           print("Tie")
        
       elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissor" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
                print("You won this round")
                user_score += 1
       else:
           print("Computer won this round")
           computer_score +=1
    print(f"Score - You: {user_score} | Score - Computer: {computer_score}")
    
if __name__ == "__main__":
    main()
