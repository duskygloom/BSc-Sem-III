''' QUESTION
Write a program that prints a pattern using nested loops to create a triangle of numbers.
Ask them to modify the code to print a square pattern.
rows = i n t ( i n p u t ( ” E n t e r t h e number o f rows f o r t h e p a t t e r n : ” ) )
# Modify t h e c o d e t o p r i n t a d i f f e r e n t p a t t e r n
f o r i i n r a n g e ( 1 , rows + 1 ) :
f o r j i n r a n g e ( 1 , i + 1 ) :
p r i n t ( j , end=” ” )
p r i n t ( )
'''

rows = int(input("Enter the number of rows for the pattern: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print()
confirm = input("Press 'Y' to print a square: ").lower()

if confirm == 'y':
    for i in range(1, rows+1):
        for j in range(1, rows+1):
            print(j, end=" ")
        print()

''' OUTPUT
$ python3 v_square_pattern.py 
Enter the number of rows for the pattern: 5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

Press 'Y' to print a square: y
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 

$ python3 v_square_pattern.py 
Enter the number of rows for the pattern: 4
1 
1 2 
1 2 3 
1 2 3 4 

Press 'Y' to print a square: n
'''
