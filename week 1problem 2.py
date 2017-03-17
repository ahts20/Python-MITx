# -*- coding: utf-8 -*-
"""
Problem 2
10.0 points possible (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
"""
s = 'abobobobegghakl'
k = 0
n = 0
for i in s:
     if s[k] == 'b' and s[k+1] == 'o' and s[k+2] == 'b':
         n += 1
     k += 1
print("Number of times bob occurs is:", n)