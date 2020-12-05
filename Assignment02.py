# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:38:07 2020

@author: Anudeep
"""
"""
1. Create the below pattern using nested for loop in Python. 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""

bool = False
i = 1
while (0 < i < 6):
    print("*"*i)
    if(bool):
        i = i - 1
    else:
        i = i + 1
    
    if(i == 5):
        bool = True
        
"""
2. Write a Python program to reverse a word after accepting the input from the user. Sample Output: 

"""       
name = input("Enter a Name ::")
print(name[::-1])