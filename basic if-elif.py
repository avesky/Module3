"""
Program: basic if-elif.py
Author: Andy Volesky
Last date modified: 09/13/2021

The purpose of this program: Write a program that asks for
the user to sign up for Programmer's Toolkit Monthly Subscription Box.
They must select level of membership they want. Each month is something different,
t-shirts, stickers, figurines, even programming books!

The levels are the following:

Platinum
Gold
Silver
Bronze
Free Trial

Write an if statement that prints the cost for each of the level.
Platinum is $60, each level below is 10 dollars cheaper, and the free trial is free.
"""

#ask for Name Input
first_name = input('First Name? ')
first_name = first_name.capitalize()
last_name = input('Last Name? ')
last_name = last_name.capitalize()

#Explain membership levels, ask for membership input
print(f"Hello {first_name} {last_name}!!  Welcome to the Programmer's Toolkit Monthly Subscription Box")
print("You may select from the following subscription level by entering the corresponding number")
print("1: Platinum")
print("2: Gold")
print("3: Silver")
print("4: Bronze")
print("5: Free Trial")
choice = int(input('What level do you choose? '))

#display price for membership
cost = 60

if choice == 1 or 2 or 3 or 4 or 5:
    if choice == 1:
        print(f"You have selected Platinum.  The price is ${cost}.  Please make payment in Bezos Bucks.")
    elif choice == 2:
        print(f"You have selected Gold.  The price is ${cost-10}.  Please make payment in Bezos Bucks.")
    elif choice == 3:
        print(f"You have selected Silver.  The price is ${cost-20}.  Please make payment in Bezos Bucks.")
    elif choice == 4:
        print(f"You have selected Bronze.  The price is ${cost-30}.  Please make payment in Bezos Bucks.")
    elif choice == 5:
        print(f"You have selected Free Trial. We require no Bezos Bucks, but we will fill your mailbox with spam.")
    # Display thank you message
    print(f"Thank you for your order {first_name} {last_name}!!")

else:
    print("Please make a valid choice next time.")

