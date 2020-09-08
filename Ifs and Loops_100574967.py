# Name : Osama Shaikh
# Student Number : 100574967
import sys

x = "Welcome to my Calculator"
print(x)
Name = input("What is your name?")


answer = False
while True:

    sign = input("Which Functions do you want to use Add(+), Subtract(-), Multiply(*) And Divide(/) and Raise(^):")
    if sign == "Stop" or sign == "Exit":
        print:sys.exit("Thankyou for using Osama Shaikh Calculator, Its time for GoodBye")

    while (not (sign == "+" or
                sign == "Add" or
                sign == "-" or
                sign == "Subtract" or
                sign == "*"or
                sign == "Multiply" or
                sign == "Divide" or
                sign == "/" or
                sign == "Raise" or
                sign == "^")):
            print("error")
            sign = input("Which Functions do you want to use Add(+), Subtract(-), Multiply(*) And Divide(/) and Raise(^):")
            if sign == "Stop" or sign == "Exit":
             print: sys.exit("Thankyou for using Osama Shaikh Calculator, Its time for GoodBye")

    if not answer:
        num1 = input("What is your First Number:")
        if sign == "Stop" or sign == "Exit":
            print: sys.exit("Thankyou for using Osama Shaikh Calculator, Its time for GoodBye")

    else:
        num1 = input("Enter a number or leave blank to use previous answer:")
        if sign == "Stop" or sign == "Exit":
            print: sys.exit("Thankyou for using Osama Shaikh Calculator, Its time for GoodBye")
        if num1 == "":
            num1 = answer
    num2 = input("What is another Number:")
    if sign == "Stop" or sign == "Exit":
        print: sys.exit("Thankyou for using Osama Shaikh Calculator, Its time for GoodBye")

    num1 = float(num1)
    num2 = float(num2)


    if (sign == "+" or sign == "add"):
        answer = num1 + num2
    if (sign == "-" or sign == "Substract"):
        answer = num1 - num2
    if (sign == "*" or sign == "Multiply"):
        answer = num1 * num2
    if (sign == "/" or sign == "Divide"):
        answer = num1 / num2
        print("adding values...")
    elif (sign == "^" or sign == "raise"):
        answer = 1
        for i in range(0, int(num2)):
            answer = answer * num1
    print("answer:" + str(answer))
    print("Your answer is ", answer)
    num8 = input("If you want to Continue with Calculator press Yes or else No:")
    if num8 =="No":
        if sign == "Stop" or sign == "Exit":
            print: sys.exit("Thankyou for using Osama Shaikh Calculator, Its time for GoodBye")
        break






