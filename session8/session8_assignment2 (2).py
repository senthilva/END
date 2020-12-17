# -*- coding: utf-8 -*-
"""session8_assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11PiOF9_n9_z7t9C1xJT-93cqN6XKn0BF
"""

# write a python program to subtract two numbers 
 num1 = 1.5
 num2 = 6.3
 sum = num1 - num2
 print(f' Diff: {sum}')

#write a python program to print first 10 natural numbers
i = 0
while i <= 10:
    print(i)
    i += 1

#write a python program to  and print the total number of digits in a number
num = 75869
count = 0
while num != 0:
    num //= 10
    count+= 1
print("Total digits are: ", count)

#write a python function to  take a list and return the reverse of it
def rev_list(in_list):
  start = len(in_list) - 1
  stop = -1
  step = -1
  for i in range(start, stop, step) :
      print(in_list[i])
  return in_list

# write a python function to multiply two user provided numbers and return the product
def mult_two_numbers(num1, num2):    
  prod = num1 * num2    
  return prod

# write a program to find and print the largest among three numbers
num1 = 10
num2 = 12
num3 = 14
if (num1 >= num2) and (num1 >= num3):   
  largest = num1
elif (num2 >= num1) and (num2 >= num3):   
  largest = num2
else:   
  largest = num3
print(f'largest:{largest}')

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
num = input("Enter a number: ")
mod = int(num) % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")

#write a python program that prints 10 random float numbers between 0.0 and 1.0
import random

for i in range(10):
    x = random.random()
    print(x)

# write a python function that prints elements of a list
def print_list(list_ex):
  for element in list_ex:
    print(element)

#write a function that minimum of a list
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

#write a python program to find the largest and print it
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

#write a python program to find length of a string and print it
str_ex = "Senthil"
print(len(str_ex))

#write a python program that we will count every word on every line of the input file and print the output

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

#write a function to add to numbers
def addtwo(a, b):
    added = a + b
    return added

#write a python program to convert celsius to Fahrenheit
inp = input('Enter Celsius Temperature:')
cel = float(inp)
fahr = (cel * 9.0) / 5.0 + 32.0
print(fahr)