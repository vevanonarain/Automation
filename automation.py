def add (x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

print("Select Operation: \n 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division \n 5) Modulo")
choice = input("\nEnter choice 1/2/3/4/5: ")

number1 = int(input("\nEnter first number: "))
number2 = int(input("Enter second number: "))

if choice == "1":
    print("\nSum is --> " + str(add(number1, number2)))
elif choice == "2":
    print("\nDifference is --> " + str(subtract(number1, number2)))
elif choice == "3":
    print("\nProduct is --> " + str(multiply(number1, number2)))
elif choice == "4":
    print("\nQuotient is --> " + str(divide(number1, number2)))
elif choice == "5":
    print("\nRemainder is --> " + str(modulo(number1, number2)))
else:
    print("Invalid input")