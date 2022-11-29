# Assignment 8

## PsychoPy keypress exercises
### 1. event.getKeys is prone to collect as many responses as you can make in a trial, but often times you only want to collect one response for a trial.Come up with a solution so that only a single response is recorded from event.getKeys (e.g., ignoring all responses after the first response). Hint: one solution is used somewhere else in level 6.

This was my orginal solution that worked at recording the first key and not the others but if you didnt press any key, it would record the key from the prior trial. 

```ruby
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')
sub_resp = []

for trial in range(nTrials):
    
    keys = event.getKeys(keyList=['1','2']) #put getkeys HERE
    my_text.text = "trial %i" %trial #insert integer into the string with %i
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() #clear events HERE
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print("keys that were pressed", keys) #which keys were pressed?
    
    if keys:
        sub_resp = keys[0] #only take first response
        
    print("response that was counted", sub_resp)    
    
win.close()
```
I changed it to this, so I could record, the no reponse trials correctly and the trials where they pressed the wrong key in addition to the trials were they pressed 1 or 2. 

```ruby 
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')
sub_resp = []

for trial in range(nTrials):
    
    keys = event.getKeys() #put getkeys HERE
    trial = trial +1 
    my_text.text = "trial %i" %trial #insert integer into the string with %i
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() #clear events HERE- this avoids including key presses that occur during fixation cross 
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print("keys that were pressed", keys) #which keys were pressed?
    
#--------------WORKING properly now :))-------------------------------------------------------------------------------------------------------------
    if not keys: 
        print('response that was counted', 'no response') # if sub response is empty, print this 
    else:
        sub_resp = keys[0] 
        if sub_resp == '1' or sub_resp == '2':
            print('response that was counted', sub_resp)
        else: 
            print('response that was counted', 'Wrong key response')

win.close()
```


### 2. Statement placement in your script is very important when collecting responses and refreshing keypresses. What happens if you put event.ClearEvents within the trial loop instead of outside the trial loop? What happens if you unindent the "if keys:" line?

When I unindent the event.clearEvents, it can no longer be placed into the for loop where I want it. Inside the for loop, between the fixation portion and the trial, it clears any responses recorded during the fixation cross presentation. So, when I take it out of the loop (as seen below) any key presses occuring during the fixation cross period will be recorded, which I do not want. 
```ruby
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')
sub_resp = []

for trial in range(nTrials):
    
    keys = event.getKeys() #put getkeys HERE
    trial = trial +1 
    my_text.text = "trial %i" %trial #insert integer into the string with %i
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print("keys that were pressed", keys) #which keys were pressed?
    
#--------------NOT WORKING-------------------------------------------------------------------------------------------------------------
    if keys: 
        sub_resp = keys[0] 
        if sub_resp == '1' or sub_resp == '2':
            print('response that was counted', sub_resp)
        elif not sub_resp:
            print('response that was counted', 'no response') # if sub response is empty, print this 
        else: 
            print('response that was counted', 'Wrong key response')
event.clearEvents() #clear events HERE- this avoids including key presses that occur during fixation cross 
win.close()
```
What happens if you unindent the "if keys:" line?:
```ruby

from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')
sub_resp = []

for trial in range(nTrials):
    keys = event.getKeys(keyList=['1','2']) #put getkeys HERE
    my_text.text = "trial %i" %trial #insert integer into the string with %i
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() #clear events HERE
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print("keys that were pressed", keys) #which keys were pressed?
    
if keys:
    sub_resp = keys[0] #only take first response
        
    print("response that was counted", sub_resp)    
    
win.close()
```
When I un indent the if keys: conditional, it does not print "the response that was counted" for each trial. Instead, it only prints the response that was counted as the first response of trial 10. 


## Save csv exercises
### 1. Using csv.DictWriter (use your favorite search engine to find the help page), save your dictionary (that you created above) as a .csv file.
```ruby
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1])

filename = 'assign8TesterNov282022'
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
fullAddress = os.path.join(data_dir, filename)
print(fullAddress)

#
#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
sub_resp = [[-1]*nTrials]*nBlocks
sub_acc = [[-1]*nTrials]*nBlocks
prob = [[-1]*nTrials]*nBlocks
corr_resp = [[-1]*nTrials]*nBlocks
resp_time = [[-1]*nTrials]*nBlocks
blocks = [[0, 0, 0, 0], [1, 1, 1, 1]] 
trials = [[0, 1, 2, 3], [0, 1, 2, 3]] 



#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 0 #arbitrary number for inaccurate response 
                                    #(should be something other than -1 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial], 'reaction time=',
              resp_time[block][trial])

win.close()

data_as_list = [prob, corr_resp, sub_resp, sub_acc, resp_time]
print(data_as_list)

with open(fullAddress, 'w') as sub_data:
    fieldnames = ['block', 'trial', 'problem','corr_resp','sub_resp','sub_acc', 'resp_time']
    data_writer = csv.DictWriter(sub_data, fieldnames=fieldnames)
    data_writer.writeheader()

    for block in range(nBlocks):
        data_as_dict = []
        for a,b,c,d,e,f,g in zip(blocks[block], trials[block], prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
            data_as_dict.append({'block':a, 'trial':b, 'problem':c,'corr_resp':d,'sub_resp':e,'sub_acc':f, 'resp_time':g})
        print(data_as_dict)
        for iTrial in range(nTrials):
            data_writer.writerow(data_as_dict[iTrial])
 ```           


## Save JSON exercises
### 1. Add JSON filesaving to your experiment script.

## Read JSON exercises
### 1. Create a short "read and analysis" script that loads a saved JSON file, performs rudimentary analyses on the data, and prints the means.

### 2. Change your "read and analysis" script so that RTs for inaccurate responses are removed from analysis.

### 3. Change your "read and analysis" script so that any trials without a response (0 value) are removed from analysis.
