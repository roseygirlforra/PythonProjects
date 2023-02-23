

def main(): 


    while True:
        userChoice = input ("Please choose an operator: +,*,-,/ or if you want to quit, type exit\n")
        print (userChoice)

        if userChoice == "exit": 
            break

        if userChoice == "+":
            num1 = float(input ("Choose the first number: "))
            num2 = float(input ("Choose the second number: "))

            print (sum(num1, num2))

        if userChoice == "*":
            num1 = float(input ("Choose the first number: "))
            num2 = float(input ("Choose the second number: "))

            print (multiply(num1, num2))


        if userChoice == "-": 
            num1 = float(input ("Choose the first number: "))
            num2 = float(input ("Choose the second number: "))

            print (subtract(num1, num2))


        if userChoice == "/":
            num1 = float(input ("Choose the first number: "))
            num2 = float(input ("Choose the second number: "))

            print (divide(num1, num2))
       

def sum(a, b):
    return  a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

main()