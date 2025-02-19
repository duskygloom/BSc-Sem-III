''' QUESTION
Given a dictionary representing a book, modify the code to add a new key-value pair for the
publication year.
b o o k i n f o = {’ t i t l e ’ : ’ The Great Gatsby ’ , ’ a u t h o r ’ : ’F . S c o t t F i t z g e r a l d ’ }
# Add t h e p u b l i c a t i o n y e a r t o t h e d i c t i o n a r y
p r i n t ( ‘ Updated Book I n f o r m a t i o n : ’ , b o o k i n f o )
'''

bookinfo = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
bookinfo["publication_year"] = 1925

print("Updated book information:", bookinfo)

''' OUTPUT
$ python3 o_book_info.py 
Updated book information: {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'publication_year': 1925}
'''
