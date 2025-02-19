''' QUESTION
Write a function that generates the Fibonacci series up to a specified number of terms.
'''

def fibonacci(n: int) -> list[int]:
    series = []
    if n < 1:
        return series
    elif n == 1:
        series.append(0)
    else:
        series.append(0)
        series.append(1)
        while len(series) < n:
            series.append(series[-1]+series[-2])
    return series

n = int(input("Number of terms: "))
print(f"Fibonacci series: {fibonacci(n)}")

''' OUTPUT
$ python3 h_fibonacci.py 
Number of terms: 4
Fibonacci series: [0, 1, 1, 2]

$ python3 h_fibonacci.py 
Number of terms: 14
Fibonacci series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
'''