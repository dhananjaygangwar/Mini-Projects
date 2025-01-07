
def add():
    result = value1 + value2
    print(result)
def sub():
    result = value1 - value2
    print(result)
def mul():
    result = value1*value2
    print(result)
def div():
    result = value1/value2
    print(result)

value1 = input("Enter the value 1: ")
value1 = int(value1)
value2 = input("Enter the value 2: ")
value2 = int(value2)

print("Enter the Operation You want to perform: \n \
      Type + for Addition\n \
      Type - for Subtraction\n \
      Type * for Multiplication\n \
      Type / for Division")
operation = input("Enter the operator: ")



if operation == "+":
    add()
elif operation == "-":
    sub()
elif operation == "*":
    mul()
elif operation == "/":
    div()


