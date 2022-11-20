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
wait_timer = core.Clock()

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

The core.wait() timer is precise to 5 decimal places with the following times below: 
Image duration was 1.0000911999959499 seconds
Image duration was 1.0002876999787986 seconds
Image duration was 0.9999881000258029 seconds
