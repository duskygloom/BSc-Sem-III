''' QUESTION
The following code contains an error related to division by zero. Modify the code to handle
this error gracefully.
n u m e ra t o r = i n t ( i n p u t ( ‘ E n t e r t h e n um e r a t o r : ’ ) )
d e n o m i n a t o r = i n t ( i n p u t ( ‘ E n t e r t h e d e n o m i n a t o r : ’ ) )
r e s u l t = n u m e r a t o r / d e n o m i n a t o r
p r i n t ( ‘ The r e s u l t o f t h e d i v i s i o n i s : ’ , r e s u l t )
'''

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

try:
    result = numerator / denominator
    print("The result of the division:", result)
except ZeroDivisionError as e:
    print("Encountered zero division error.")
    print("The result of the division: undefined")

''' OUTPUT
$ python3 k_division_by_zero.py 
Enter the numerator: 20
Enter the denominator: 0
Encountered zero division error.
The result of the division: undefined

$ python3 k_division_by_zero.py 
Enter the numerator: 20
Enter the denominator: 2
The result of the division: 10.0
'''
