from math import *

name = 'Tom'
print(name + ' Hello world', 100)
age = 18
print(name + ' Hello\n world', age)

# Get data from file but you must close the file
file = ('file.txt', 'a') 
file.close()
## use with to auto close
with open('file.txt', 'a') as f:
    pass
# STIRNGS
# Part of var
print(name[1])
# uppercase
print(name.upper())
# is upper case or lower case
print(name.islower())
print(name.isupper())
# conver to lower case and check
print(name.lower().islower())
## LENGTH
print(len(name))
## Find letter 
print(name.index('o'))
## Find letter and replace
print(name.replace('m', 'x'))
# Remove carridge return
print('xxx'.rstrip()) 
# break things down into separate lines when you find a character
'data'.split("|")


# NUMBERS
number = 79
print(number)
print(number + 3)
print(number + 2.345)
print(number * 88)
print(20/6)
# Remainder
print(20%6)
number2 = str(number)
print('numis ' + number2)
print(-5)
# absolute value
print(abs(-5))
## Higher numbers
print(max(4, 2))
## Lower numbers
print(min(8, 3))
## Roundeding
print(round(3.4))
## Binary string
print(bin(255))
## square
print(sqrt(100))

import random
print(random.randrange(-1, 11))
print(random.randint(-1, 11)) # shows 11

# USER INPUT
# username = input('Input your name: ')
# userAge = int(input('Input your age: '))
# print(username)
# print('Your name is: ' + username + 'and you are' + str(userAge) + ' years old')

# LISTS
countries = [
    'uk', 'france', 'italy', 'greenland'
]
print(countries)
print(countries[1])
print(countries[1][0])
## from x to end
print(countries[1:])
## from x to y
print(countries[1:3])
## last entry
print(countries[-1])
## length of array
print(len(countries))

# get types
print(type(countries))
print(type(name))
print(type(age))

## Change value
countries[0] = 'denmark'
print(countries)

## list constructor
newList = list(('place', 23, False))
print(newList)

list1 = [1, 2, 3, 4, 5]
list2 = ['banana', 'apple', 'mango', 'orange']

list1.extend(list2)
print(list1)

# add to end
list2.append('cherry')
print(list2)

## add to index
list2.insert(1, 'dicks')
print(list2)

## remove from list
list2.remove('banana')
print(list2)

## clear list
# list2.clear()
# print(list2)

## get index of element
print(list2.index('orange')) 
print(list2.count('orange')) 

# SORT
randomList = [4, 3, 66, 33, 12]
randomList.sort()
print(randomList)

## reverse
randomList.reverse()
print(randomList)

## copy 
randomList2 = randomList.copy()
print(randomList2)

## pop
randomList2.pop()
print(randomList2)

# # remove from list
# randomList2.remove(3)
# print(randomList2)

del randomList2[1]
print(randomList2)

# TUPLES
three__numbers = (1,2,3)
print(three__numbers)
print(type(three__numbers))

# FUNCTIONS 

def greetings(name):
    print("Hello " + name)

greetings('chap')

def passing_tuples(*names):
    print("Passing " + names[0])

passing_tuples('chap', 'tim', 'house')

# 1

# def add_num(num1, num2):
#     return num1 + num2

# num1 = int(input('enter num1 '))
# num2 = int(input('enter num2 '))
# print(add_num(num1, num2))

# IF
a = 4
b = 3

if a>b: 
    print(str(a) + ' is igger ' + str(b) + ' dur')

if a == b: 
    print('a = b')

c = 'z'
d = 5

if c == True:
    print('A is true')
elif c == False:
    print('A is false')
else:
    print('A is nont there')

boy = True
short = True

if boy == True or short == False:
    print('aaaaaaaaa')
elif boy == False:
    print('false')
else:
    print('esle')

boy2 = True
short2 = False

if boy2 == True and short2 == False:
    print('truuw')
else:
    print('esle')

# testValue = input('enter a value: ')

# if type(testValue) == str:
#     print(testValue + 'is a string')
# else: 
#     print('nah')

# DICTIONARY
my_dict = {
    'name': 'tom',
    'age': 'ten',
    'size': 'large',
    'pleh': 55,
    'magic': True,
    'freinds': ['jack', 'james']
}

print(my_dict)
print(my_dict['magic']) # true
print(len(my_dict))
print(my_dict['freinds']) 

x = my_dict['freinds']
print(x)

# WHILE LOOP