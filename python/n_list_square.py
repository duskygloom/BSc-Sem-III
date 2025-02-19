''' QUESTION
Given a list of numbers, modify the code to create a new list containing the squares of the
numbers.
o r i g i n a l n u m b e r s = [ 2 , 4 , 6 , 8 , 1 0 ]
# Modify t h e c o d e h e r e
p r i n t ( ‘ S qu a re d numbers : ’ , s q u a r e d n u m b e r s )
'''

original_numbers = [2, 4, 6, 8, 10]

squared_numbers = [i*i for i in original_numbers]

print("Squared numbers:", squared_numbers)

''' OUTPUT
python3 n_list_square.py 
Squared numbers: [4, 16, 36, 64, 100]
'''
