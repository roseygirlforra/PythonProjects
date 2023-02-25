# Fenix Kanat
class Calculator():
    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    def subtract(a, b):
        return a - b

    def divide(a, b):
        return a / b

  

def main(): 
    while True:
        userChoice = input ("Please choose an operator: +,*,-,/ or if you want to quit, type exit\n")
        print(userChoice)

        if userChoice == "exit": 
            break

        if userChoice == "+":
            num1 = int(input ("Choose the first number: "))
            num2 = int(input ("Choose the second number: "))

            print(Calculator.add(num1, num2))

        if userChoice == "*":
            num1 = int(input ("Choose the first number: "))
            num2 = int(input ("Choose the second number: "))

            print(Calculator.multiply(num1, num2))


        if userChoice == "-": 
            num1 = int(input ("Choose the first number: "))
            num2 = int(input ("Choose the second number: "))

            print(Calculator.subtract(num1, num2))


        if userChoice == "/":
            num1 = int(input ("Choose the first number: "))
            num2 = int(input ("Choose the second number: "))

            print(Calculator.divide(num1, num2))
       
main()