name = input("What is your name? ")
print(f"Welcome, {name}! to this adventure!")

answer = input("You are in a dark forest. Do you want to go left or right? (left/right): ").lower().strip()
if answer == "left":
    answer = input("You come to a river, you can walk around or you can swim to cross. So Choose walk/swim")
    if answer == "swim":
        print("You swam accross and were eaten by an alligator")
        
    elif answer == "walk":
            print("You walked for many miles, ran out of water and loss the game")
    
    else:
        print("Not a valid option. You lose")
            
elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross or not?")
    if answer == "back":
            print("You lost now")
            
    elif answer == "cross":
            answer = input("You cross the bridge and meet a stranger, Do you talk to them or not? Yes/No")
            if answer == "yes":
                print("He looted you and you loose")
            else:
                print("You won")
        
    else:
            print("Not a valid option. You lose")
        
    
    
else:
    print("Not a valid option, You loose.")
    