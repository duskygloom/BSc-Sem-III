''' QUESTION
Write a program that determines if a given character is a vowel or a consonant. Ask them to
modify the code to handle both uppercase and lowercase letters.
c h a r = i n p u t ( ” E n t e r a s i n g l e c h a r a c t e r : ” )
# Modify t h e c o d e t o h a n d l e both u p p e r c a s e and l o w e r c a s e l e t t e r s
i f c h a r . l o w e r ( ) i n ’ a e i o u ’ :
p r i n t ( ‘ Vowel ’ )
e l s e :
p r i n t ( ‘ Consonant ’ )
'''

char = input("Enter a single character: ")

if char.lower() in "aeiou":
    print("Vowel")

else:
    print("Consonant")
    
''' OUTPUT
$ python3 u_vowels.py 
Enter a single character: I
Vowel

$ python3 u_vowels.py 
Enter a single character: a
Vowel
'''