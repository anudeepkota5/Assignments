# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:09:44 2020

@author: Anudeep
"""
"""
1. Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line.
"""

squ_num = ""
for num in range(2000, 3201):
    if((num % 7 == 0) and (num % 5 != 0)):
        squ_num = squ_num + str(num) + ","

print(squ_num)

"""
2. Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
"""

first_name = input("Enter First Name :")
last_name = input("Enter Last Name :")

print(first_name[::-1] +" "+last_name[::-1])

"""
3. Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3
"""

diameter = 12
print((4/3)*(22/7)*((diameter/2)**3))