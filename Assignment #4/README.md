
# Asignmnet 4: Conditionals & Loops 
## Paige Faulkner 


## Conditional exercises

### 1. You want to tell your experiment to record participant responses. If the response is "1" or "2", print OK. If the response is "NaN" (empty), print a "subject did not respond" message. If the response is anything else, print "subject pressed the wrong key".
```
response = '1'

if response == '1' or response == '2':
    print("Ok")
elif response == "NaN":
    print("subject did not respond")
else:
    print("Subject pressed the wrong key")
```


### 2. Create a nested "if" statement in the above exercise. If the response is "1", print "Correct!". If the response is "2", print "Incorrect!"
```
response = 2
if response == 1 or response == 2:
    if response == 1:
        print('Correct')
    if response == 2: 
        print('Incorrect')
elif response == 'NaN':
    print("Subject did not repsond")
else: 
    print("subject pressed the wrong key")
```

    
### 3. Test out your script with various responses. Does it do what you expect it to?

```
response = 2
if response == 1 or response == 2:
    if response == 1:
        print('Correct')
    if response == 2: 
        print('Incorrect')
elif response == 'NaN':
    print("Subject did not repsond")
else: 
    print("subject pressed the wrong key")
```

I tested it by setting the response item to each conditional statement value and it worked. 
Example: my ouput was 'Incorrect' which I would expect becuase I set response = 2. 

## For loop exercises

### 1. Remember the exercise where you printed each letter of your name? Create a for loop that prints each letter without writing out all of the print statements manually.
```
name = 'Paige'
for letter in name:
    print(letter)
```
### 2. Add an index counter and modify your loop to print the index number after each letter

name = 'Paige'

counter = -1
for letter in name:
    counter = counter + 1
    print(letter)
    print(counter)
    
### 3. Create a list of names "Amy","Rory", and "River". Create a nested for loop to loop through each letter of each name.

names = ['Amy', 'Vernon', 'Miguel']


for name in names:
    print(name)
    for letter in name: 
        print(letter)


### 4. Add an index counter that gives the index of each letter for each name. The counter should start over at 0 for each name in the list.

names = ['Amy', 'Vernon', 'Miguel']


for name in names:
    print(name)
    letterCounter = -1
    for letter in name: 
        letterCounter = letterCounter + 1 
        print(letter)
        print(letterCounter)


## While loop exercises


### 1. Create a while loop of 20 iterations that prints "image1.png" for the first 10 iterations, and "image2.png" for the next 10 iterations.


iteration = 0 
while iteration < 20:
    if iteration < 10:
        print('%i, image1.png' % iteration)
    elif iteration < 20:
        print('%i, image2.png' % iteration)
    iteration = iteration + 1
    

### 2. Create a while loop that shows an image until the participant makes a response of 1 or 2. Run it a few times to make sure it works the way you expect.


#NEED TO WORK ON THIS ONE

import random
response = ''
looping = True

while looping:
    response = random.randint(0, 10)
    print(response)
    print('This image is an image')
    if response == 1 or response == 2:
        looping = False

    

### 3. Create a failsafe that terminates the previous while loop after 5 iterations if one of the valid responses (1,2) have not been made in that time.
import random
response = ''
looping = True
failsafe = 0

while looping:
    response = random.randint(0, 10)
    print(response)
    print('This image is an image')
    failsafe = failsafe + 1 
    if response == 1 or response == 2 or failsafe == 5:
        looping = False
