## Clock exercises
### 1. Create a "wait_timer" to find out exactly how long core.wait(2) presents each image. Make sure this is not counting the time of the whole trial, but only the duration of each image. How precise is core.wait?
```ruby
from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win)


#create a list if images to show
stims = []
for i in range(3):
    if i < 9: 
        stims.append('face0' + str(i +1) + '.jpg') 
print(stims)

nTrials=3 #create a number of trials for your images
wait_timer = core.wait()

for trial in range(nTrials): #loop through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip() #show
    core.wait(0.5) #wait .5 seconds, then:

    my_image.draw() #draw
    win.flip() #show
    imgStartTime = wait_timer.getTime()
    core.wait(1) #wait .5 seconds, then:
    imgEndTime = wait_timer.getTime()

    fix_text.draw()
    win.flip() #show
    core.wait(0.5) #wait .5 seconds, then:

    print('Image duration was {} seconds' .format(imgEndTime - imgStartTime))
win.close() #close the window after trials have looped 
```

The core.wait() timer is precise to 4 decimal places with the following times below: 
Image duration was 1.0000911999959499 seconds
Image duration was 1.0002876999787986 seconds
Image duration was 0.9999881000258029 seconds

### 2. Create a "clock_wait_timer" to find out exactly how long each image is presented when you use a clock + while loops. How precise is this?
```ruby
from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win)

#create a list if images to show
stims = []
for i in range(3):
    if i < 9: 
        stims.append('face0' + str(i +1) + '.jpg') 
print(stims)

nTrials=3 #create a number of trials for your images
clock_wait_timer = core.Clock()
stim_timer = core.Clock()

#clock_wait_timer & while loops: 

for trial in range(nTrials): #loop through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip() #show
    core.wait(0.5) #wait .5 seconds, then:

    stim_timer.reset()
    imgStartTime = clock_wait_timer.getTime()
    while stim_timer.getTime() <= 1:
        my_image.draw()
        win.flip()
    imgEndTime = clock_wait_timer.getTime()

    fix_text.draw()
    win.flip() #show
    core.wait(0.5) #wait .5 seconds, then:

    print('Image duration was {} seconds' .format(imgEndTime - imgStartTime))
win.close() #close the window after trials have looped 
```
 The core.Clock() timer has precision to the third decimal place. 

 Output: 
Image duration was 1.0043000999721698 seconds
Image duration was 1.004118799988646 seconds
Image duration was 1.0030713999876752 seconds

### 3. Create a "countdown_timer" to find out exactly how long each image is presented when you use a CountdownTimer + while loops. How precise is this?

```ruby
from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win)

#create a list if images to show
stims = []
for i in range(9):
    if i < 9: 
        stims.append('face0' + str(i +1) + '.jpg') 
print(stims)

nTrials= len(stims) #create a number of trials for your images
clock_wait_timer = core.Clock()
stim_timer = core.CountdownTimer()

#clock_wait_timer & while loops: 

for trial in range(nTrials): #loop through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip() #show
    core.wait(0.5) #wait .5 seconds, then:

    stim_timer.reset()
    stim_timer.add(1)
    imgStartTime = clock_wait_timer.getTime()
    while stim_timer.getTime() > 0:
        my_image.draw()
        win.flip()
    imgEndTime = clock_wait_timer.getTime()

    fix_text.draw()
    win.flip() #show
    core.wait(0.5) #wait .5 seconds, then:

    print('Image duration was {} seconds' .format(imgEndTime - imgStartTime))
win.close() #close the window after trials have looped 
```
The CountdownTimer() has pecision to three decimal places.

### 4. Edit your main experiment script so that the trials loop according to a clock timer. Also create and implement a block_timer and a trial_timer.

```ruby
#=====================
#IMPORT MODULES
#=====================
import numpy as np  #-import numpy and/or numpy functions *
from psychopy import core, visual, gui, event, monitors #-import psychopy functions
#-import file save functions
import json  # can save files various ways (i.e. csv but json has good cross platform readability) 
#-(import other functions as necessary: os...)
import random # could be useful for randomizing trials later on 
import os # allows you to find files and save data
from ctypes import sizeof
from matplotlib.pyplot import hsv
from datetime import datetime

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()
#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

print(data_dir)
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

print(image_dir)
#-check that these directories exist
os.path.isdir(image_dir)


#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness


exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':(), 'session':1}


my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                        title="subject info",
                        fixed=['session'],
                        order=['session', 'subject_nr', 'age', 'gender', 'handedness'], 
                        show= False)

print("All variables have been created! Now ready to show the dialog box!")

show_dlg = my_dlg.show()


#get date and time


date = datetime.now() #what time is it right now?
print(date)
exp_info['date'] = str(date.day) + str(date.month) + str(date.year)
print(exp_info['date'])
#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)
import os
main_dir = os.getcwd() #define the main directory where experiment info is stored
#create a subject info directory to save subject info
sub_dir = os.path.join(main_dir,'sub_info',filename)

#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10 
nBlocks = 2
#-stimulus names (and stimulus extensions, if images) *
pics = []
for i in range(10):
    if i < 9:
        pics.append('face0' + str(i + 1) + '.jpg')
    elif i == 9:
        pics.append('face' + str(i + 1) + '.jpg')
print(pics)
imgs_in_dir = sorted(os.listdir(image_dir))
print(imgs_in_dir)
#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200]
stimDur = 1
stimOrien = [10]
#-start message text *
startMessage = "Welcome to the experiment, press any key to begin."

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist


for j in range (10): 
    if pics == imgs_in_dir:
        print(str(pics[j]) + ' was found')
    elif not pics == imgs_in_dir:
        raise Exception("The image lists do not add up!")
    j =+ 1
    if j == 10:
        break

    
#-create counterbalanced list of all conditions *
random.shuffle(pics)

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
corrResp = []
corrResp = [[0]*nTrials]*nBlocks
#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
pptResp = []
pptResp = [[0]*nTrials]*nBlocks

#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
accResp = []
accResp = [[0]*nTrials]*nBlocks

#-create an empty list for response time collection *
RT = []
RT = [[0]*nTrials]*nBlocks
#-create an empty list for recording the order of stimulus identities *
stimOrd_id = []
#-create an empty list for recording the order of stimulus properties *
stimOrd_prop = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=50.8, distance=60) #define the monitor parameters
#-define the window (size, color, units, fullscreen mode) using psychopy functions
mon.setSizePix([1920,1200])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]

win = visual.Window(monitor=mon, fullscr=True)

#-define experiment start text unsing psychopy functions
start_msg = 'Welcome to the Experiment'
#-define block (start)/end text using psychopy functions
block_msg = 'Press any key to proceed to the next block!'
trial_end_msg = 'End of trial'
#-define stimuli using psychopy functions (images, fixation cross)
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units ='pix', size =(400,400))
nTrials = 4
nBlocks = 2
block_timer = core.Clock()
trial_timer = core.Clock()
image_dir = os.path.join(main_dir, 'images')
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg']
horiz_mult = [-1, 1, -1, 1]
vert_mult = [1, 1, -1, -1]
corrResp = [True, True, True, True,]
#-create response time clock
#A7 input***
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
my_text = visual.TextStim(win)
my_text.text = start_msg
my_text.draw()
win.flip()

#-allow participant to begin experiment with button press
event.waitKeys()
#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks): 
    block_timer.reset()
    while block_timer.getTime() <= 20:
        my_text.text = block_msg #-present block start message
        my_text.draw()
        win.flip()
        event.waitKeys()
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
        #-set stimuli and stimulus properties for the current trial  
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw image
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw end trial text
        #-flip window
        #-wait time (stimulus duration)

        for trial in range(nTrials): #-randomize order of trials here
            my_image.image = os.path.join(image_dir, stims[trial])

            my_image.pos = (horiz_mult[trial] * thisWidth/4, horiz_mult[trial] * thisHeight/4)
            trial_timer.reset()
            while trial_timer.getTime() < 1:
                my_image.draw()
                fix_text.draw()
                win.flip()
                event.waitKeys()
            my_text.text = trial_end_msg + str(trial)
            my_text.draw()
            win.flip()
            event.waitKeys()
win.close()
        
#======================
# END OF EXPERIMENT
#======================   
```
### 1. Adjust your experiment so that it follows frame-based timing rather than clock timing (comment out the clock-based timing code in case you want to use it again) using for loops and if statements.
My monitors refresh rate = 60hz. 
```ruby
from psychopy import visual, monitors, event, core, logging
import os
refresh=1.0/60.0 #single frame duration in seconds
print(1/(1/60)) #reciprocal of refresh 
#So this:
fix_dur = 1.0 #1 sec
image_dur = 2.0 #2 sec
text_dur = 1.5 #1.5 sec

#Becomes:
fix_frames = fix_dur / refresh
image_frames = image_dur / refresh
text_frames = text_dur / refresh

print("Seconds:", fix_dur, image_dur, text_dur)
print("Frames:", fix_frames, image_frames, text_frames)


#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window
refresh=1.0/60.0
#set durations
fix_dur = 1.0 #200 ms
image_dur = 2.0 #100 ms
text_dur = 1.5 #200 ms

#set frame counts
fix_frames = int(fix_dur / refresh) #whole number
image_frames = int(image_dur / refresh) #whole number
text_frames = int(text_dur / refresh) #whole number
#the total number of frames to be presented on a trial
total_frames = int(fix_frames + image_frames + text_frames)

fix = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win)

nBlocks=1
nTrials=20

#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()
#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')
image_dir = os.path.join(main_dir,'images')
stims = ['face01.jpg','face02.jpg','face03.jpg'] 

#this can output various information about your experiment

win.recordFrameIntervals = True #record frames
#give the monitor refresh rate plus a few ms tolerance (usually 4ms)
win.refreshThreshold = 1.0/60.0 + 0.004

# Set the log module to report warnings to the standard output window 
#(default is errors only).
logging.console.setLevel(logging.WARNING)


for block in range(nBlocks):
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        
        my_image.image = os.path.join(image_dir,stims[trial])
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames): #for the whole trial...
            #-draw stimulus
            if 0 <= frameN <= fix_frames: #number of frames for fixation      
                fix.draw() #draw
                win.flip() #show
                
                if frameN == fix_frames: #last frame for the fixation
                    print("End fix frame =", frameN) #print frame number
                    
            #number of frames for image after fixation
            if fix_frames < frameN <= (fix_frames+image_frames):      
                my_image.draw() #draw
                win.flip() #show 
                
                if frameN == (fix_frames+image_frames): #last frame for the image
                    print("End image frame =", frameN) #print frame number  
                    
            #number of frames for the final text stimulus    
            if (fix_frames+image_frames) < frameN < total_frames:  
                fix.draw() #draw
                win.flip() #show  
                
                if frameN == (total_frames-1): #last frame for the text
                    print("End text frame =", frameN) #print frame number 
        
        #this will print total number of frames dropped following every trial
        print('Overall, %i frames were dropped.' % win.nDroppedFrames)   
                
win.close()  

#-close window
```
### 2. Add a "dropped frame" detector to your script to find out whether your experiment is dropping frames. How many total frames are dropped in the experiment? If 20 or fewer frames are dropped in the whole experiment (1 frame per trial), keep frame-based timing in your experiment. Otherwise, switch back to the CountdownTimer.
The code above includes and dropped frame detector and I have dropping greater than 1 frame per trial. Therefore, I will switch back to the CoundownTimer. 
