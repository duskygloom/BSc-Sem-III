''' QUESTION
Create a function that takes a list of numbers as input and returns the sum of all the elements.
'''

def sum_elements() -> int:
    numbers = [float(i) for i in input("Numbers: ").split()]
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(f"Sum: {sum_elements():.4f}")

''' OUTPUT
$ python3 i_sum_of_numbers.py 
Numbers: 12 16 9 20
Sum: 57.0

$ python3 i_sum_of_numbers.py 
Numbers: 12.2 16.9 20
Sum: 49.1000
'''
