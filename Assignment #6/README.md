
## Dialog box exercises
### Use the PsychoPy help page on guis to customize your "exp_info" dialog box: psychopy.gui

### 1. Edit the dictionary "exp_info" so you have a variable called "session", with "1" preset as the session number.
(see code below)
### 2. Edit the "gender" variable in "exp_info" so the subject can write in whatever they want into an empty box, instead of the drop-down list
(see code below)
### Using DlgFromDict:

### 1. Customize my_dlg so that you have a title for your dialog box: "subject info".
(see code below)
### 2. Set the variable "session" as fixed. What happens?
When you use fixed = function, the particpant cannot edit the session value of 1. 
### 3. Set the order of the variables as session, subject_nr, age, gender, handedness.
(see code below)
### 4.Once you have done all of the above, don't show "my_dlg" right away. Tell your experiment to print "All variables have been created! Now ready to show the dialog box!". Then, show the dialog box.
(see code below)
### 5.Fill in the following pseudocode with the real code you have learned so far:
```ruby
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
from ctypes import sizeof
from matplotlib.pyplot import hsv
import psychopy
from psychopy import gui
from psychopy import visual, monitors, event
from datetime import datetime

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
```

## Monitor and window exercises
### Look at the psychopy help page on "window" to help solve the exercises:

### 1. How does changing "units" affect how you define your window size?
If you use height units, the size fo all the stimuli will adjust to your screen. 
When I increase numbers in the size = (), the size of the window increases. I set the window to full screen to mimic a real experiement. 
### 2. How does changing colorSpace affect how you define the color of your window? Can you define colors by name?

### 3. Fill in the following pseudocode with the real code you have learned so far:

```ruby
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=50.8, distance=60) #define the monitor parameters
mon.setSizePix([1920,1200])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]

win = visual.Window(monitor=mon, fullscr=True)
# win = visual.Window(monitor=mon, size = (1920,1200), color =(0,0.5,1), colorSpace= hsv)
#could also do fullscr = True 


#-define the window (size, color, units, fullscreen mode) using psychopy functions
```

## Stimulus exercises
### Check the psychopy help page on "ImageStim" to help you solve these exercises:

### 1. Write a short script that shows different face images from the image directory at 400x400 pixels in size. What does this do to the images? How can you keep the proper image dimensions and still change the size?

### 2. Write a short script that makes one image appear at a time, each in a different quadrant of your screen (put the window in fullscreen mode). Think about how you can calculate window locations without using a trial-and-error method.

### 3. Create a fixation cross stimulus (hint:text stimulus).

### 4. Fill in the following pseudocode with the real code you have learned so far:
```ruby
# retval = os.getcwd()
# print("Current working directory %s" % retval)

# my_image = visual.ImageStim(win)
# image_dir = os.path.join(main_dir, 'images')


# pic_loc = os.path.join(image_dir, 'face01.jpg')
# print(image_dir)
# my_image = visual.ImageStim(win, image=pic_loc)
# my_image.draw()
# win.flip()
# event.waitKeys()
# win.close()


#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text using psychopy functions
start_msg = 'Welcome to the Experiment'
#-define block (start)/end text using psychopy functions
block_msg = 'Press any key to proceed to the next block!'
trial_end_msg = 'End of trial'
#-define stimuli using psychopy functions (images, fixation cross)
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units ='pix', size =(100,100))
nTrials = 4
nBlocks = 2
image_dir = os.path.join(main_dir, 'images')
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg']
horiz_mult = [-1, 1, -1, 1]
vert_mult = [1, 1, -1, -1]
corrResp = [True, True, True, True,]

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
#-close window
```
