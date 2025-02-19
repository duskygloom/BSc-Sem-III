''' QUESTION
Write a program that takes a number as input from the user and prints its multiplication
table up to 10.
'''

n = int(input("Number: "))
print()

for i in range(10):
    print(f"{n} x {i+1:2} = {n*(i+1)}")

''' OUTPUT
$ python3 d_multiplication_table.py 
Number: 16

16 x  1 = 16
16 x  2 = 32
16 x  3 = 48
16 x  4 = 64
16 x  5 = 80
16 x  6 = 96
16 x  7 = 112
16 x  8 = 128
16 x  9 = 144
16 x 10 = 160

$ python3 d_multiplication_table.py 
Number: -7

-7 x  1 = -7
-7 x  2 = -14
-7 x  3 = -21
-7 x  4 = -28
-7 x  5 = -35
-7 x  6 = -42
-7 x  7 = -49
-7 x  8 = -56
-7 x  9 = -63
-7 x 10 = -70
'''
