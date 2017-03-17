'''
// Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
'''
'''
s = "azcbobobegghakl"
a = 0
n = 0

while a < len(s):
    if s[a] == ('a' or 'e' or 'i' or 'o' or 'u'):
        n += 1
    a += 1
print ("Number of Vowels", n)

'''
counter = 0

s = "azcbobobegghakl"
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        counter += 1
print ("Number of Vowels", counter)
