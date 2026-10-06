def main():
    quiz = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What language is used for web scripts? (Python/JavaScript)", "answer": "JavaScript"},
        {"question": "Which integer equals 2 + 2 * 2?", "answer": "6"}
    ]
    
    score = 0
    for item in quiz:
        user_ans = input(f"{item['question']}").strip()
        if user_ans.lower() == item['answer'].lower():
            print("Wow your Answer is correct")
            score += 1
        elif user_ans.lower() != item['answer'].lower():
                print("Ops wrong Answer")
                score -= 1
        else:
            print("Play again or quit")
            user_in2 = input("Do you wanna play again or Quit?")
            if user_in2 == 'quit':
                break
            else:
                continue
    percentage = (score /len(quiz))*100
    print(f"Quiz finished! Final Score: {percentage}")
    
if __name__ == "__main__":
    main()
                

        
    