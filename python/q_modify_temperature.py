''' QUESTION
Given the following code for a simple temperature converter, modify it to handle both Celsius
to Fahrenheit and Fahrenheit to Celsius conversions based on user input.
c h o i c e = i n p u t ( ‘ E n t e r ’C’ f o r C e l s i u s t o F a h r e n h e i t o r ’ F ’ f o r F a h r e n h e i t t o C e l s i u s : ’ )
i f c h o i c e == ’C ’ :
c e l s i u s = f l o a t ( i n p u t ( ‘ E n t e r t e m p e r a t u r e i n C e l s i u s : ’ ) )
f a h r e n h e i t = # E n t e r t h e e q u a t i o n
p r i n t ( f ‘ The t e m p e r a t u r e i n F a h r e n h e i t i s : {f a h r e n h e i t }’ )
e l i f c h o i c e == ’ F ’ :
# Do same f o r f a h r e n h e i t t o c e l s i u s c o n v e r s i o n
e l s e :
p r i n t ( ‘ I n v a l i d c h o i c e . P l e a s e e n t e r ’C’ o r ’ F ’ . ’ )
'''

choice = input("Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ")

if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 9/5 * celsius + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}")

elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = 5/9 * (fahrenheit - 32)
    print(f"The temperature in Celsius is: {celsius}")

else:
    print("Invalid choice. Please enter 'C' or 'F'.")

''' OUTPUT
$ python3 q_modify_temperature.py 
Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: f
Invalid choice. Please enter 'C' or 'F'.

$ python3 q_modify_temperature.py 
Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: C
Enter temperature in Celsius: 20
The temperature in Fahrenheit is: 68.0
'''
