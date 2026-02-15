int1 = int(input("Enter the first number:"))
int2 = int(input("Enter the second number:"))

operator = input("enter the preferred operation:")
try:
    if(operator == '*'):
        print("You chose to multiply.")
        print(int1*int2)
    elif(operator == '+'):
        print("You chose to add.")
        print(int1+int2)
    elif(operator == '-'):
        print("You chose to subtract.")
        print(int1 - int2)
    elif(operator == '/'):
        print("You chose to divide.")
        print(int1 / int2)
    else:
        print("Invalid operation.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Please enter an integer!")
