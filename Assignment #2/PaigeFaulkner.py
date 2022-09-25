#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:11:37 2022

@author: johngray
"""
#Print Exercises
print("P")
print("A")
print("I")
print("G")
print("E")

#Do any of the variables show up in the variable editior? 
#   No, they show up in the console but not in the variable explorer

#Operation Excersises 
#Question 1

print(5/2)
print(5.0/2.0)
#Python gave me the same output for each of these. 
#Question 2
print(101%25)
print(56%7)
#it gives you the remainder after dividing the first number by the second number

#Question 3 
print(2**3)
print(101//25)
# ** functions as a "to the power of" operation and // tells you how many times the second number divides into the first

#Question 4
print(6*5+11/2)
#Yes, it follows the same order of operations as mathematics does (bedmas/pedmas.)

#Variable Excersises
#Question 1
letter1 = "P"
letter2 = "A"
letter3 = "I"
letter4 = "G"
letter5 = "E"
#Question 2
#Yes, they do show up in the variable editor called the variable explorer in spyder
#Question 3
letterx = "E"
print(letter5)
print(letterx)
#There are no problems with two variables having the same value
#Question 5
letterx = "T"
print(letterx)
print(letter5)
#Changing the variable letterx did not change the variable letter5
#Question 6
letterx = letter1
print(letterx)
print(letter1)
letter1 = "Z"
print(letter1)
print(letterx)
#letterx did not change to z. If you assign varaiable1 to equal another variable2, variable1 will change to equal varaible2. 
#However, if you alter variable2 after that line of code, variable1 will remain the same. 
#You must reassign variable 1 to equal variable 2 after you change the value of variable 2 if you want it to change as well.  
letterx = letter1
print(letter1)
print(letterx)

# Boolean Exercises
### 1. Are 1 and 1.0 equivalent? Are "1" and "1.0" equivalent? Why do you think this is?
print(1 == 1.0)
#Yes, the console prints true and I assume it is becuase boolean operations do not differeniate between floats and intergers. 

### 2. Are 5 and (3+2) equivalent?
print(5 == (3 + 2))
#Yes, the console prints true. 
### 3. Write out the statements [Are 1 and 1.0 equivalent?] X [Are "1" and "1.0" equivalent?] X [Are 5 and (3+2) equivalent?] 
#in proper Boolean syntax, in which you replace X with "and", "or", "and not", or "not". List 5 ways to get True as your output.
print(1 == 1.0 or "1" == "1.0")
print(1 == 1.0 and not "1" == "1.0")
print(5 ==(3+2) or 1 == 1.0)
print(5 ==(3+2) and 1 == 1.0)
print(5 ==(3+2) and not "1" == "1.0")

# List Exercisies
### 1. Create a list called "oddlist", listing all of the odd integers between 0 and 10. Did oddlist become a variable?
oddlist = [1,3,5,7,9]
#Yes, the list, "oddlist", became a variable. 
### 2.Print oddlist. If you get an error message, double check how you created your list.
print(oddlist)
#No error message. 
### 3.When you use the "len" function on oddlist, how long does python say the list is?
print(len(oddlist))
#It says the length of the list is 5. 
### 4.When you use the "type" function on oddlist, what type of variable does python say oddlist is? If you get something other than a list, double check how you created your list and try again.
print(type(oddlist))
#Python returns <class 'list'>
### 5.Create a list called "intlist", listing all of the integers between 0 and 100 -- do not type them all out manually!
intlist = (range(1,100))
### 6.Print intlist. Does it list all integers between 0 and 100? If not, double check how you created your list.
print(list(intlist))
#Yes, it prints intergers from 1-99 becase the first number is the start and the last number is the number it stops at. If you wanted all the numbers inclduing 100, you would do list(range(1,101))

# Dictionary Exercises

### 1. Create a dictionary called "about_me" that contains the following information: your name (string format), age (float format), year of study (integer format), and favorite foods in a list (list of strings).
about_me = {'myname' : "Paige", 'myage' : 24.0, 'yearofstudy' : 1, 'favouritefoods' : ['Chocolate', 'Candy', 'The Grick Middle Sandwhich from Farrow', 'hummus & veggies']}
### 2. Print about_me. If there are no error messages at this point, double check your variable with the "type" function to make sure you have made a dictionary.
print(about_me)
print(type(about_me))
#The console output returns <class 'dict'>. 
### 3. Check the length of about_me. How does python determine the length of a dictionary?
print(len(about_me))
# The output was 4. Therefore, dictonaries' length is determined by the number of variables ('myname', 'myage', 'yearofstudy', 'favouritefoods'.)



# Array Exercises

### 1. Create an array called "mixnums" composed of 3 integers and 3 floats. Print the array. What has happened to the array?
import numpy as np

mixnums = np.array([1,2,3,4.2,5.0])
print(mixnums)
#When you print the array, the output numbers are all floats not intergers. This may indidicate that np.arrays cannot have mixed data types (i.e. floats & intergers) 

### 2. Create an array called "mixtypes" composed of 2 integers, 2 floats, and 2 strings. Print the array. What has happened to the array? What does python do to arrays with mixed types?
mixtypes = np.array([1,2,4.2,5.0,'Hello', 'World'])
print(mixtypes)
#The array when printed, made all the intergers and floats strings. This may be because np.arrays cannot have mixed data types in a single array. 
### 3. Create an array called "oddarray" of all odd numbers between 0 and 100.
oddarray = np.arange(1,100,2)
print(oddarray)
### 4. Create an array called "logarray" of 16 numbers between 1 and 5 that follow a logarithmic distribution. These should not be integers.
logarray = np.logspace(0.05,0.69,16)
print(logarray)




