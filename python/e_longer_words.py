''' QUESTION
Modify the code to create a new list containing only the words longer than 3 characters.
words = [ ’ a p p l e ’ , ’ banana ’ , ’ k i w i ’ , ’ o r a n g e ’ , ’ g r a p e ’ ]
# Modify t h e c o d e h e r e
p r i n t ( ” Long words : ” , l o n g w o r d s )
'''

words = ["apple", "banana", "kiwi", "orange", "grape"]

longwords = []

for word in words:
    if len(word) > 3:
        longwords.append(word)

print("Long words:", longwords)

''' OUTPUT
$ python3 e_longer_words.py 
Long words: ['apple', 'banana', 'kiwi', 'orange', 'grape']
'''
