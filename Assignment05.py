# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:56:25 2020

@author: Anudeep
"""

"""
1. Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
def compute():
    5/0
    
try:
    compute()
except ArithmeticError as e:
    print("exception :: " + str(e))

"""
2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
"""
subjects=["Americans ","Indians"]
verbs=["play","watch"]
oobjects=["Baseball","Cricket"]
for subject in subjects:
    for verb in verbs:
        for oobject in oobjects:
            print(subject +" "+verb +" "+ oobject)