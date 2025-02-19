''' QUESTION
Create a program that prompts the user to enter a number and then calculates and prints its
factorial using a while loop.
'''

def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

n = int(input("Number: "))
print(f"{n}! = {factorial(n)}")

''' OUTPUT
$ python3 f_factorial.py 
Number: 5
5! = 120

$ python3 f_factorial.py 
Number: 0
0! = 1
'''
