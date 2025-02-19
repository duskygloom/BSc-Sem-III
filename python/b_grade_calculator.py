''' QUESTION
Develop a program that prompts the user to enter a numerical grade. Classify the grade into
categories (A, B, C, D, F) and print the corresponding classification.
'''

''' GRADE SYSTEM
A   > 90
B   [90, 70)
C   [70, 50)
D   [50, 30)
F   < 30
'''

score = float(input("Marks: "))
grade = ""

if score > 90   : grade = "A"
elif score > 70 : grade = "B"
elif score > 50 : grade = "C"
elif score > 30 : grade = "D"
else            : grade = "F"

print(f"Grade: {grade}")

''' OUTPUT
$ python3 b_grade_calculator.py 
Marks: 81
Grade: B

$ python3 b_grade_calculator.py 
Marks: 90
Grade: B

$ python3 b_grade_calculator.py 
Marks: 91 
Grade: A
'''
