"""
Regular Expression 2中包含使用Regex101来进行regular expression查询
"""
import re

string = "this is a really cool string really!"
print('search' in string)    #This print will get you a True bool. 

a = re.search('really',string)   # Over here you wanna search is if 'really' is in string.
print(a)

# the below 4 commands will give error if the searching string does not exist.
print(a.span())     # will tells you where the strings are as tuple, eg. (10, 16)
print(a.start())    # will show where the string starts: 10
print(a.end())
print(a.group())    # will show you if the search appears in the string. Very useful if you wanna search to if a word exist and where it exists. 

pattern = re.compile('really')

b = pattern.search(string)
c = pattern.findall(string)

pattern = re.compile('this is a really cool string really!')
d = pattern.fullmatch('this is a really cool string really!')
e = pattern.fullmatch('hello this is a really cool string really!')    # this should be exact match, otherwise returns none

pattern = re.compile('really')
f = pattern.match('really cool feature')    # it starts matching from the first character otherwise returns none
g = pattern.match('yo really')

print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print(f"g: {g}")
