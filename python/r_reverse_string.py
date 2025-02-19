''' QUESTION
The following code is supposed to take a string as input and print the reversed string. How-
ever, it has some mistakes. Fix the code.
t e x t = i n p u t ( ” E n t e r a s t r i n g : ” )
r e v e r s e d t e x t = t e x t [ : : − 1 ]
p r i n t ( ” The r e v e r s e d s t r i n g i s : ” r e v e r s e d t e x t )
'''

text = input("Enter a string: ")

reversed_text = text[::-1]

print("The reversed string is:", reversed_text)

''' OUTPUT
$ python3 r_reverse_string.py 
Enter a string: kurkure
The reversed string is: erukruk

$ python3 r_reverse_string.py 
Enter a string: madam
The reversed string is: madam
'''
