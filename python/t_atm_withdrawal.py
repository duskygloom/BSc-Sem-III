''' QUESTION
Write a program that simulates an ATM withdrawal. Ask them to modify the code to include
a maximum withdrawal limit of 2000 rupees per transaction.
a c c o u n t b a l a n c e = 10 000 # Assuming i n i t i a l a c c o u n t b a l a n c e i s 1 000 0 r u p e e s
w i t h d r a w a l a m o u n t = i n t ( i n p u t ( ‘ E n t e r t h e amount you want t o withdraw : ’ ) )
# Modify t h e c o d e t o i n c l u d e a maximum w i t h d r a w a l l i m i t
m a x w i t h d r a w a l = 2000
i f w i t h d r a w a l a m o u n t % 100 == 0 :
a c c o u n t b a l a n c e −= w i t h d r a w a l a m o u n t
p r i n t ( f ‘ Withdrawal s u c c e s s f u l . Remaining b a l a n c e : ${a c c o u n t b a l a n c e }’ )
e l s e :
p r i n t ( ‘ Withdrawal amount must be d i v i s i b l e by 1 0 0 . ’ )
'''

account_balance = 10000

withdrawal_amount = int(input("Enter the amount you want to withdraw: "))

max_withdrawal = 2000

if withdrawal_amount > max_withdrawal:
    print(f"Withdrawal amount must be less than {max_withdrawal}.")

elif withdrawal_amount % 100 == 0:
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful. Remaining balance: {account_balance}")

else:
    print("Withdrawal amount must be divisible by 100.")

''' OUTPUT
$ python3 t_atm_withdrawal.py 
Enter the amount you want to withdraw: 2500
Withdrawal amount must be less than 2000.

$ python3 t_atm_withdrawal.py 
Enter the amount you want to withdraw: 2000
Withdrawal successful. Remaining balance: 8000
'''
