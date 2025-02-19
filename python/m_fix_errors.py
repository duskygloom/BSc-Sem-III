''' QUESTION
Consider the following Python code. Identify and fix the errors to make it run correctly.
num = i n p u t ( ‘ ‘ E n t e r a number : ” )
r e s u l t = num ∗ 2
p r i n t ( ‘ The r e s u l t i s : ’ + r e s u l t )
'''

num = input("Enter a number: ")
result = int(num) * 2
print("The result is: " + str(result))

''' OUTPUT
$ python3 m_fix_errors.py 
Enter a number: 20
The result is: 40

$ python3 m_fix_errors.py 
Enter a number: 3
The result is: 6
'''
