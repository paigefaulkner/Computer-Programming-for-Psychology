# Answers to Assignment 2
## Paige Faulkner 


## Print Exercises
### 1. 
```
print("P")
print("A")
print("I")
print("G")
print("E")
```

### 2. Do any of the variables show up in the variable editior? 
No, they show up in the console but not in the variable explorer.


## Operation Exercises 

### 1. Divide 5/2 (integer format) and 5.0/2.0 (float format). Does python output the same values for these? (You might get a different answer depending on the version of python you are in). If you got a different answer for the two operations, explain why.
```
print(5/2)
print(5.0/2.0)
```
Python gave me the same output for each of these

### 2. What does the modulo operator (%) do? Try it out with a few numbers in this format: "x % y" to get an idea.
```
print(101%25)
print(56%7)
```
The modulo operator gives you the remainder after dividing the first number by the second number. 

### 3. What do these operators do: ** and //? Try them out with a few numbers in this format: "x // y" to get an idea.
```
print(2**3)
print(101//25)
```
** functions as a "to the power of" operation and // tells you how many times the second number divides into the first

### 4. Does python follow order of operations? Try it out with a few numbers in this format: "a + b + c * d / e"
```
print(6*5+11/2)
```
Yes, it follows the same order of operations as mathematics does (bedmas/pedmas.)

## Variables Exercises
### 1. Open "yourname.py". Edit the script so that each letter is labeled as a separate variable in this format: letter1, letter2, etc.
```
letter1 = "P"
letter2 = "A"
letter3 = "I"
letter4 = "G"
letter5 = "E"
```

### 2. Run the script. Do any variables show up in the Variable Editor?

Yes, they do show up in the variable editor called the variable explorer in spyder.

### 3. If there are not any repeated letters in your name: Create a final variable "letterX" that is the same as the first letter of your name. Run the script again. Print letterX and letter1 in the command line. Does python have a problem with two different variables having the same value?
```
letterx = "E"
print(letter5)
print(letterx)
```
There are no problems with two variables having the same value. 

### 4. If there are repeated letters in your name: Relabel one of those variables as "letterX". Print the variables with the same value one after the other in the command line. Does python have a problem with two (or more) different variables having the same value?

No repeated letters, move to Question 5. 

### 5. Give letterX a new letter that is not in your name. Print the new letterX and the other variable(s) that were previously all the same letter. Did changing the value of letterX change the value of the other variable(s)?

```letterx = "T"
print(letterx)
print(letter5)
```
Changing the variable letterx did not change the variable letter5.

### 6. Redefine letterX with another variable instead of a letter (e.g., letterX=letter1). Print letterX and letter1, one after the other. Now change the value of letter1 to "z". Print letterX and letter1, one after the other. Did changing the value of letter1 change the value of letterX? What does this tell you about python variable assignment?
```
letterx = letter1
print(letterx)
print(letter1)
letter1 = "Z"
print(letter1)
print(letterx)
```
letterx did not change to z. If you assign varaiable1 to equal another variable2, variable1 will change to equal varaible2. However, if you alter variable2 after that line of code, variable1 will remain the same. You must reassign variable 1 to equal variable 2 after you change the value of variable 2 if you want it to change as well.  


#Boolean Exercises

#List Exercisies

#Dictionary Exercises

#Array Exercises



import numpy as np

data = np.array([1,2,3,4,5])

print(data)

print(np.logspace(2,4,20))
3)
4)
5)
6)
7)
