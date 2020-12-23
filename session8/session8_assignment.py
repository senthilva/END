

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



Skip to content
Using Gmail with screen readers
Meet
Hangouts

4 of 3,280
Assignment 17B
Inbox

Nihar Kanungo
Attachments
Dec 20, 2020, 10:33 AM (3 days ago)
to me

Arch,

   PFA

Regards,
Nihar
Attachments area

senthil vinayagam
Dec 20, 2020, 11:00 AM (3 days ago)
Thanks a ton mate ! I owe you On Sun, 20 Dec 2020, 10:33 Nihar Kanungo, <nihar.kanungo@gmail.com> wrote: Arch, PFA Regards, Nihar

Nihar Kanungo
Dec 20, 2020, 11:14 AM (3 days ago)
to me

You are welcome  Arch

Thanks a lot.Thank you!Thanks a lot!

# Add two strings
def add_str(str1,str2):
   return str1 + str2

# we are dealing with multiple inheritance
class A(object):
    def foo(self):
        print("class A")

class B(object):
    def foo(self):
        print("class B")

class C(A, B):
    pass

# This is how pass works in case of multiple inheritance
class A1(object):
   def foo(self):
      print("class A1")

class B1(A1):
   pass

class C1(A1):
   def foo(self):
      print("class C1")

class D1(B1,C1):
   pass

# List are mutable
a_list = []
print('ID:', id(a_list))
a_list += [1]
print('ID (+=):', id(a_list))
a_list = a_list + [2]
print('ID (list = list + ...):', id(a_list))

# All blank lists are not the same 
a_list = []
print(a_list, '\nID (initial):',id(a_list), '\n')
a_list.append(1)
print(a_list, '\nID (append):',id(a_list), '\n')
a_list.extend([2])
print(a_list, '\nID (extend):',id(a_list))

# True and False in the datetime module
from platform import python_version
import datetime

print("Current python version: ", python_version())
print('"datetime.time(0,0,0)" (Midnight) ->', bool(datetime.time(0,0,0))) # Python version <= 3.4.5 evaluates this statement to False

# Python reuses objects for small integers - use "==" for equality, "is" for identity
a = 1
b = 1
print('a is b', bool(a is b))
c = 999
d = 999
print('c is d', bool(c is d))

# equality operator works this way
print('256 is 257-1', 256 is 257-1)
print('257 is 258-1', 257 is 258 - 1)
print('-5 is -6+1', -5 is -6+1)
print('-7 is -6-1', -7 is -6-1)

# illustrate the test for equality (==) vs. identity (is)
a = 'hello world!'
b = 'hello world!'
print('a is b,', a is b)
print('a == b,', a == b)

# We would think that identity would always imply equality, but this is not always true, as we can see in the next example:
a = float('nan')
print('a is a,', a is a)
print('a == a,', a == a)

# Shallow copy in python
list1 = [1,2]
list2 = list1        # reference
list3 = list1[:]     # shallow copy
list4 = list1.copy() # shallow copy
print('IDs:\nlist1: {}\nlist2: {}\nlist3: {}\nlist4: {}\n'
      .format(id(list1), id(list2), id(list3), id(list4)))

# Deepcopy in python

list1 = [[1],[2]]
list2 = list1.copy()    # shallow copy
list3 = deepcopy(list1) # deep copy
print('IDs:\nlist1: {}\nlist2: {}\nlist3: {}\n'
      .format(id(list1), id(list2), id(list3)))

#logical or logical and 
result = (2 or 3) * (5 and 7)
print('2 * 7 =', result)

#Don't use mutable objects as default arguments for functions!
def append_to_list(value, def_list=[]):
    def_list.append(value)
    return def_list
my_list = append_to_list(1)
print(my_list)

my_other_list = append_to_list(2)
print(my_other_list)

# args and sleep 
import time
def report_arg(my_default=time.time()):
    print(my_default)
report_arg()
time.sleep(5)
report_arg()

# Generators are consumed 
gen = (i for i in range(5))
print('2 in gen,', 2 in gen)
print('3 in gen,', 3 in gen)
print('1 in gen,', 1 in gen) 

# Convert generator to a list
gen = (i for i in range(5))
a_list = list(gen)

# Usage of bool class
print('isinstance(True, int):', isinstance(True, int))

# Create list of numbers using lambda function but not the right way
my_list = [lambda: i for i in range(5)]
for l in my_list:
    print(l())

# print the numbers properly by creating a list
my_list = [lambda x=i: x for i in range(5)]
for l in my_list:
    print(l())

# local scope representation
x = 0
def in_func():
    x = 1
    print('in_func:', x)

# Global Scope Representation
x = 0
def in_func1():
    x = 1
    print('in_func1:', x)
print('global:', x)

# Usage of global keyword
x = 0
def in_func2():
    global x
    x = 1
    print('in_func2:', x)
in_func2()
print('global:', x)

# local vs. enclosed 
def outer():
    x = 1
    print('outer before:', x)

    def inner():
        x = 2
        print("inner:", x)
    inner()
    print("outer after:", x)
outer()

# nonlocal keyword comes in handy 
def outer():
    x = 1
    print('outer before:', x)

    def inner():
        nonlocal x
        x = 2
        print("inner:", x)
    inner()
    print("outer after:", x)
outer()

# tuples are immutable 
tup = (1,)
tup[0] += 1

# what if we put a mutable object into the immutable tuple
tup1 = ([],)
print('tup before: ', tup1)
tup1[0] += [1]


# there are ways to modify the mutable contents of the tuple without raising the TypeError
tup = ([],)
print('tup before: ', tup)
tup[0].extend([1])
print('tup after: ', tup)

# another way to append data to tuple
tup = ([],)
print('tup before: ', tup)
tup[0].append(1)
print('tup after: ', tup)

# Add tuples like numerics
my_tup = (1,)
my_tup += (4,)
my_tup = my_tup + (5,)
print(my_tup)

# What happens "behind" the curtains is that the tuple is not modified, but a new object is generated every time, which will inherit the old "name tag":
my_tup = (1,)
print(id(my_tup))
my_tup += (4,)
print(id(my_tup))
my_tup = my_tup + (5,)
print(id(my_tup))

# Create a plain list

def plainlist(n=100000):
    my_list = []
    for i in range(n):
        if i % 5 == 0:
            my_list.append(i)
    return my_list

# Create a list comprehension
def listcompr(n=100000):
    my_list = [i for i in range(n) if i % 5 == 0]
    return my_list

# Create a Generator
def generator(n=100000):
    my_gen = (i for i in range(n) if i % 5 == 0)
    return my_gen

# Generator using yield function
def generator_yield(n=100000):
    for i in range(n):
        if i % 5 == 0:
            yield i

# Generators are faster than list comprehension
import timeit
def test_plainlist(plain_list):
    for i in plain_list():
        pass


def test_listcompr(listcompr):
    for i in listcompr():
        pass


def test_generator(generator):
    for i in generator():
        pass


def test_generator_yield(generator_yield):
    for i in generator_yield():
        pass
print('plain_list:     ', end='')
%timeit test_plainlist(plainlist)
print('\nlistcompr:     ', end='')
%timeit test_listcompr(listcompr)
print('\ngenerator:     ', end='')
%timeit test_generator(generator)
print('\ngenerator_yield:     ', end='')
%timeit test_generator_yield(generator_yield)

# Public vs. private class methods and name mangling
    def public_method(self):
        print('Hello public world!')

    def __private_method(self):
        print('Hello private world!')

    def call_private_method_in_class(self):
        self.__private_method()


my_instance = my_class()

my_instance.public_method()
my_instance._my_class__private_method()
my_instance.call_private_method_in_class()

# The consequences of modifying a list when looping through it
a = [1, 2, 3, 4, 5]
for i in a:
    if not i % 2:
        a.remove(i)
print(a)
b = [2, 4, 5, 6]
for i in b:
     if not i % 2:
         b.remove(i)
print(b)

#  iterating through the list index by index
b = [2, 4, 5, 6]
for index, item in enumerate(b):
    print(index, item)
    if not item % 2:
        b.remove(item)
print(b)

# Dynamic binding and typos in variable names
print('first list:')
for i in range(3):
    print(i)
    
print('\nsecond list:')
for j in range(3):
    print(i) # I (intentionally) made typo here!

# List slicing using indexes that are "out of range"
my_list = [1, 2, 3, 4, 5]
print(my_list[5])

# Reusing global variable names and UnboundLocalErrors
def my_func():
    print(var)
var = 'global'
my_func()

# No problem to use the same variable name in the local scope without affecting the local counterpart:
def my_func():
    var = 'locally changed'
var = 'global'
my_func()
print(var)

# we have to be careful if we use a variable name that occurs in the global scope, and we want to access it in the local function scope if we want to reuse this name:
def my_func():
    print(var)  # want to access global variable
    var = 'locally changed'  # but Python thinks we forgot to define the local variable!

var = 'global'
my_func()

# We have to use the global keyword!

def my_func():
    global var
    print(var)  # want to access global variable
    var = 'locally changed'  # changes the gobal variable
var = 'global'
my_func()
print(var)

# Creating copies of mutable objects
my_list1 = [[1, 2, 3]] * 2
print('initially ---> ', my_list1)
# modify the 1st element of the 2nd sublist
my_list1[1][0] = 'a'
print("after my_list1[1][0] = 'a' ---> ", my_list1)

# we should better create "new" objects:
my_list2 = [[1, 2, 3] for i in range(2)]
print('initially:  ---> ', my_list2)
# modify the 1st element of the 2nd sublist
my_list2[1][0] = 'a'
print("after my_list2[1][0] = 'a':  ---> ", my_list2)

for a, b in zip(my_list1, my_list2):
    print('id my_list1: {}, id my_list2: {}'.format(id(a), id(b)))

# Abortive statements in finally blocks
def try_finally1():
    try:
        print('in try:')
        print('do some stuff')
        float('abc')
    except ValueError:
        print('an error occurred')
    else:
        print('no error occurred')
    finally:
        print('always execute finally')
try_finally1()

# Assigning types to variables as values
a_var = str
a_var(123)

#random choice 
from random import choice

a, b, c = float, int, str
for i in range(5):
    j = choice([a,b,c])(i)
    print(j, type(j))


# Only the first clause of generators is evaluated immediately
gen_fails = (i for i in 1/0)

# lazy evaluation 
gen_succeeds = (i for i in range(5) for j in 1/0)
print('But obviously fails when we iterate ...')
for i in gen_succeeds:
    print(i)

# Usge of *args 
def a_func(*args):
    print('type of args:', type(args))
    print('args contents:', args)
    print('1st argument:', args[0])
a_func(0, 1, 'a', 'b', 'c')

# usage of kwargs
def b_func(**kwargs):
    print('type of kwargs:', type(kwargs))
    print('kwargs contents: ', kwargs)
    print('value of argument a:', kwargs['a'])

b_func(a=1, b=2, c=3, d=4)

# Unpacking of iterables
val1, *vals = [1, 2, 3, 4, 5]
print('val1:', val1)
print('vals:', vals)

# if else for 
for i in range(5):
    if i == 1:
        print('in for')
else:
    print('in else')
print('after for-loop')

# usage of break
for i in range(5):
    if i == 1:
        break
else:
    print('in else')
print('after for-loop')

# conditional usecase
a_list = [1,2]
if a_list[0] == 1:
    print('Hello, World!')
else:
    print('Bye, World!')

# Usage of while
i = 0
while i < 2:
    print(i)
    i += 1
else:
    print('in else')

# Interning of string 
hello1 = 'Hello'
hello2 = 'Hell' + 'o'
hello3 = 'Hell'
hello3 = hello3 + 'o'
print('hello1 is hello2:', hello1 is hello2)
print('hello1 is hello3:', hello1 is hello3)

# Disassembler 
import dis
def hello1_func():
    s = 'Hello'
    return s
dis.dis(hello1_func)

# example to demonstrate usage of docstring
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

# Absolute function
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num
print(absolute_value(2))
print(absolute_value(-4))

#usage of dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

# accept user input
str = input("Enter your input: ")
print ("Received input is : ", str)

# A recursive function to find nth catalan number 
def catalan(n): 
    # Base Case 
    if n <= 1: 
        return 1
  
    # Catalan(n) is the sum  
    # of catalan(i)*catalan(n-i-1) 
    res = 0
    for i in range(n): 
        res += catalan(i) * catalan(n-i-1) 
  
    return res 
  
# Driver Code 
for i in range(10): 
    print (catalan(i))

# A naive recursive Python implementation 
  
def binomialCoeff(n , k): 
  
    if k > n : 
       return 0
    if k==0 or k ==n : 
        return 1
  
    # Recursive Call 
    return binomialCoeff(n-1 , k-1) + binomialCoeff(n-1 , k) 
  
# Driver Program to test ht above function 
n = 5
k = 2
print ("Value of C(%d,%d) is (%d)" %(n , k , binomialCoeff(n , k)) )

# A naive Python implementation of LIS problem 
  
""" To make use of recursive calls, this function must return 
 two things: 
 1) Length of LIS ending with element arr[n-1]. We use 
 max_ending_here for this purpose 
 2) Overall maximum as the LIS may end with an element 
 before arr[n-1] max_ref is used this purpose. 
 The value of LIS of full array of size n is stored in 
 *max_ref which is our final result """
  
# global variable to store the maximum 
global maximum 
  
def _lis(arr , n ): 
  
    # to allow the access of global variable 
    global maximum 
  
    # Base Case 
    if n == 1 : 
        return 1
  
    # maxEndingHere is the length of LIS ending with arr[n-1] 
    maxEndingHere = 1
  
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
       IF arr[n-1] is maller than arr[n-1], and max ending with 
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n): 
        res = _lis(arr , i) 
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere: 
            maxEndingHere = res +1
  
    # Compare maxEndingHere with overall maximum. And 
    # update the overall maximum if needed 
    maximum = max(maximum , maxEndingHere) 
  
    return maxEndingHere 
  
def lis(arr): 
  
    # to allow the access of global variable 
    global maximum 
  
    # lenght of arr 
    n = len(arr) 
  
    # maximum variable holds the result 
    maximum = 1
  
    # The function _lis() stores its result in maximum 
    _lis(arr , n) 
  
    return maximum 
  
# Driver program to test the above function 
arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60] 
n = len(arr) 
print ("Length of lis is ", lis(arr) )

# Function for nth Fibonacci number 
  
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
  
print(Fibonacci(9)) 



