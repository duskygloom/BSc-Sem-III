''' QUESTION
Create a basic calculator program that takes two numbers and an operation (addition, sub-
traction, multiplication, or division) as input. Perform the calculation and display the result.
'''

def menu() -> int:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    return int(input("Response: "))

a = float(input("Operator A: "))
b = float(input("Operator B: "))
print()

result = 0
response = menu()
print()

if response == 1:
    result = a + b

elif response == 2:
    result = a - b

elif response == 3:
    result = a * b

elif response == 4:
    result = a / b

print(f"Result: {result:.4f}")

''' OUTPUT
$ python3 c_basic_calculator.py 
Operator A: 12
Operator B: 19

1. Add
2. Subtract
3. Multiplication
4. Division
Response: 1

Result: 31.0

$ python3 c_basic_calculator.py 
Operator A: 20
Operator B: 3

1. Add
2. Subtract
3. Multiplication
4. Division
Response: 4

Result: 6.6667
'''
