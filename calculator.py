print("NKK Calculator!")

while "naren":  
    a = eval(input("Enter 1st number: "))
    b = eval(input("Enter 2nd number: "))
    c = input("Tell me which operator (+,-,*,/,**,//): ")

    if c == "+":
        print("Answer is:", a + b)
    elif c == "-":
        print("Answer is:", a - b)
    elif c == "*":
        print("Answer is:", a * b)
    elif c == "/":
        print("Answer is:", a / b)
    elif c == "**":
        print("Answer is:", a ** b)
    elif c == "//":
        print("Answer is:", a // b)
    else:
        print("Invalid operator! Kindly use a valid operator.")

    s = input("Type 'stop' to exit or press Enter to continue: ")
    if s.lower() == "stop":
        break
