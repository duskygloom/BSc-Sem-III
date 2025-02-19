''' QUESTION
Write a program that calculates ticket prices based on age. Ask them to modify the code to
include a discount of 10% for students (ages 13-18) and seniors (ages 61 and above).
a g e = i n t ( i n p u t ( ‘ E n t e r y o u r a g e : ’ ) )
i f 0 <= a g e <= 5 :
t i c k e t p r i c e = 0 # F r e e f o r a g e s 0−5
e l i f 6 <= a g e <= 1 2 :
t i c k e t p r i c e = 5
e l i f 13 <= a g e <= 1 8 :
t i c k e t p r i c e = 10 # Modify t h i s t o i n c l u d e a 10% d i s c o u n t
e l i f 19 <= a g e <= 6 0 :
t i c k e t p r i c e = 15
e l s e :
t i c k e t p r i c e = 10 # D i s c o u n t f o r s e n i o r s ( 6 1 and above )
p r i n t ( f ‘ The t i c k e t p r i c e f o r a {a g e}−y e a r −o l d i s : ${t i c k e t p r i c e }’ )
'''

age = int(input("Enter your age: "))

if 0 <= age <= 5:
    ticket_price = 0

elif 6 <= age <= 12:
    ticket_price = 5

elif 13 <= age <= 18:
    ticket_price = 10
    ticket_price *= 0.9

elif 19 <= age <= 60:
    ticket_price = 15

else:
    ticket_price = 10
    ticket_price *= 0.9

print(f"The ticket price for a {age}-year old is: {ticket_price}")

''' OUTPUT
$ python3 s_price_per_age.py 
Enter your age: 10
The ticket price for a 10-year old is: 5

$ python3 s_price_per_age.py 
Enter your age: 20
The ticket price for a 20-year old is: 15
'''
