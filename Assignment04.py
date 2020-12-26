# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:49:12 2020

@author: Anudeep
"""

"""
1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below  formula. 
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 

Function to take the length of the sides of triangle from user should be defined in the parent  class and function to calculate the area should be defined in subclass. 
"""
import math
class shape:    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class triangle(shape):
    def __init__(self,*args):
        super().__init__(*args)
        self.s = 0.5 * (self.a+self.b+self.c)
    
    def area(self):
        return 'The area of the triangle is %0.2f' %(math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c)))

t1 = triangle(89,85,25)
print(t1.area())

"""
1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns  the list of words that are longer than n. 
"""

def filter_long_words(lst, n):
    return list(filter(lambda x: len(x) > n, lst))

print(filter_long_words(['a','aa','aaa','aaaa','aaaaa'], 3))

"""
2.1 Write a Python program using function concept that maps list of words into a list of integers  representing the lengths of the corresponding words. 
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list. 
"""
def get_len(lst):
    return list(map(lambda x:len(x), lst))

print(get_len(['a','aa','aaa','aaaa','aaaaa']))
"""
2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if  it is a vowel, False otherwise.
"""
def is_vowel(char):
    return True if char in ['a','e','i','o','u'] else False

print(is_vowel('z'))