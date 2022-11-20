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
