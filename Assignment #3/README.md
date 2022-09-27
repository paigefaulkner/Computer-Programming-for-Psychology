# Assignment 3
## Paige Faulkner
## Variable operations exercises
### 1. Create three variables: "sub_code", "subnr_int", and "subnr_str". The sub_code should be "sub". Assign the integer 2 to subnr_int, and assign the string "2" to subnr_str. Which form of subnr (int or str) can be added to sub_code to create the output "sub2"? Why don't both work?

```ruby
import np as np
import numpy as np
sub_code = "sub"
subnr_int = 2
subnr_str = "2"
print(sub_code + subnr_int)
print(sub_code + subnr_str)
```
It can print sub_code + subnr_str becuase they are both strings. It cannot print(sub_code + subnr_int) becuase you cannot combine a string and and interger

### 2. Use operations to create the following outputs with your variables:
"sub 2"
"sub 222"
"sub2sub2sub2"
"subsubsub222"

```ruby
print(sub_code + " " + subnr_str)

print(sub_code + " " + (subnr_str * 3))
print((sub_code + subnr_str)*3)
print((sub_code * 3) + (subnr_str*3))
```

## List operations exercises
### 1. Create a list of numbers [1,2,3] called "numlist". Multiply the list by 2.
```ruby
numlist = [1, 2, 3]
print(numlist * 2)
```
### 2.Create a numpy array of numbers [1,2,3] called "numarr". Multiply the array by 2. What is the difference between multiplying lists and multiplying arrays?
```ruby
numarr = np.array([1, 2, 3])
print(numarr * 2)
```
In the array, it multplies each number in the list whereas, lists repeat the lists two limes when times by 2.


### 3.Create a list of strings ['do','re','mi','fa'] called "strlist". Use operations to create the following outputs with your variable:
['dodo','rere','mimi','fafa']
['do','re','mi','fa','do','re','mi','fa']
['do','do','re','re','mi','mi','fa','fa']
[['do','do'],['re','re'],['mi','mi'],['fa','fa']]
```ruby
strlist = ['do', 're', 'mi', 'fa']
print([strlist[0] * 2, strlist[1]*2, strlist[2]*2, strlist[3]*2])
print(strlist * 2)
print([strlist[0], strlist[0],
      strlist[1], strlist[1],
      strlist[2], strlist[2],
      strlist[3], strlist[3], ])
print([[strlist[0], strlist[0]],
      [strlist[1], strlist[1]],
      [strlist[2], strlist[2]],
      [strlist[3], strlist[3]], ])
```

## Zipping exercises
### 1.You are designing a memory experiment in which 1 face and 1 house are presented on each trial, one after the other, followed by a post-cue that tells the participant which of the two images to remember. You want to present all combinations of stimuli an equal number of times, with a random trial order for each participant. The order of image presentations (face first or house first) should also be counterbalanced ahead of time.
Specifically, you have:

2 categories of images (faces, houses)
5 images from each category
2 post-cues (1,2)

## Create a script that outputs a counterbalanced list with every face paired with every house, repeated with each possible post-cue. Then, randomize the order of the list. The final output should look something like this:
```ruby
Add code in
```


## Indexing exercises
### 1.Create a list of strings called "colors", containing the following colors in this order: red, orange, yellow, green, blue, purple
```ruby
colours= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(colours)
```
### 2.Using indexing, print the penultimate color.
```ruby
print(colours[-2])
```

### 3.Using indexing, print the 3rd and 4th characters of the penultimate color.
```ruby
print(colours[-2][2])
print(colours[-2][3])
```
### 4.Using indexing, remove the color "purple" and add "indigo" and "violet" to the list instead.
```ruby
colours[-1]= 'indigo'
colours.append('violet')
print(colours)
```
## Slicing exercises
### 1.Create a list of numbers 0-100 called "list100".
```ruby
list100 = (range(0, 101))
print(list(list100))
```
### 2.Using slicing, print the first 10 numbers in the list.
```ruby
print(list(list100[: 10]))
```
### 3.Using slicing, print all the odd numbers in the list backwards.
```ruby
temp = (list100[1:: 2])
```

### 4.Using slicing, print the last four numbers in the list backwards.
```ruby
print(list(temp[:: -1]))
```
### 5.Are the 40th-44th numbers in the list equal to integers 39-43? Show the Boolean operation you would use to determine the truth value.
```ruby
print(list(temp[-4:: -1]))
```
