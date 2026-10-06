print("Welcome to my computer Quiz!")

playing = input("Do you want to play the game?")

if playing == "yes".strip().lower():
    quit()
    
print("Okay! Let's play:) ")
score = 0

answer = input("What does CPU stand for? ")
if answer == "central proceessing unit":
    print('Correct!')
    score +=1
else: 
    print("Incorret!")
    score -=1
    

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
    score +=1
else: 
    print("Incorret!")
    
answer = input("What does PSU stand for? ")
if answer == "power supply":
    print('Correct!')
    score +=1
else: 
    print("Incorret!")
    score -=1
    
print("You got " +str(score) + "question correct!")
print("You got " +str((score/3)*100) + "%")