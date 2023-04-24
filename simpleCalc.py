# Simple calculator to perform basic operations (addition, subtraction, multiplication, division)

def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    oper = input("Enter operation sign: \n+ for addition\n- for subtraction\nx for multiplication\n\ for division\n")

    if oper == '+':
        result = num1 + num2
        print(num1, " + ", num2, " = ", result)
    elif oper == '-':
        result = num1 - num2
        print(num1, " - ", num2, " = ", result)
    elif oper == 'x':
        result = num1 * num2
        print(num1, " x ", num2, " = ", result)
    elif oper == '/':
        if num2 == 0:
            print("Math Error")
        else:
            result = num1 / num2
            print(num1, " / ", num2, " = ", result)
    else:
        print("Enter a valid operation sign")


# calling the function

calculator()
