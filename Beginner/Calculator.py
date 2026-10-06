def main():
    print("Simple Calculator: +, -, *, /")
    
    try:
        int1 = int(input("Input the first number"))
        Operation = input("Enter your operation: +, -, *, / ")
        int2 = int(input("Input the second number"))
        
        if Operation == "+":
            res = int1 + int2
        elif Operation == "-":
            res = int1 - int2
        elif Operation == "*":
            res = int1 * int2
        elif Operation == "/": 
            if int2 == 0:
                print("Invalid Request")
                return
            res = int1/int2
        else:
            print("Invalid Operator!")
            return
        print(f"Result: {res}")
    except ValueError:
        print("Invalid numerical Input")
        
if __name__ == "__main__":
    main()
        
            