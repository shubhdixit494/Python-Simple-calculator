# Simple Calculator - bilkul basic

num1 = float(input("Pehla number dalo: "))
num2 = float(input("Dusra number dalo: "))

print("\nKya karna hai?")
print("+ jodna")
print("- ghatana")
print("* guna karna")
print("/ bhag karna")

operation = input("Symbol dalo (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"Answer: {num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"Answer: {num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"Answer: {num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Answer: {num1} / {num2} = {result}")
    else:
        print("0 se bhag nahi kar sakte!")

else:
    print("Galat symbol dala!")