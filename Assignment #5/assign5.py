#=====================
#IMPORT MODULES
#=====================
import numpy as np  #-import numpy and/or numpy functions *
from psychopy import core, visual, gui, event #-import psychopy functions
#-import file save functions
import json  # can save files various ways (i.e. csv but json has good cross platform readability) 
#-(import other functions as necessary: os...)
import random # could be useful for randomizing trials later on 
import os # allows you to find files and save data

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
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10 
nBlocks = 2
#-stimulus names (and stimulus extensions, if images) *
cats = ['faces']*10
imgs = ['img1.png', 'img2.png', 'img3.png', 'img4.png', 'img5.png', 'img6.png', 'img7.png', 'img8.png', 'img9.png', 'img10.png'] 
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
pics = []
for i in range(10):
    pics.append('face' + str(i + 1) + '.png')
print(pics)
imgs_in_dir = sorted(os.listdir(image_dir)

for j in range (10): 
    if pics == imgs_in_dir:
        print(pic[0] + 'was found')
    elif not pics == imgs_in_dir
        raise Exception("The image lists do not add up!")
    j =+ 1
#-create counterbalanced list of all conditions *
catimgs = list(zip(cats,imgs))


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
stimOrd_id = 
#-create an empty list for recording the order of stimulus properties *
stimOrd_prop = [];

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in range(nBlocks):
    #-present block start message
    #-randomize order of trials here *
    random.shuffle(nTrials)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment
```

## Import Exercises 

### 1. Fill in the "Import Modules" section of the experiment structure: 
```ruby
#=====================
#IMPORT MODULES
#=====================
import numpy as np  #-import numpy and/or numpy functions *
from psychopy import core, visual, gui, event #-import psychopy functions
#-import file save functions
import json  # can save files various ways (i.e. csv but json has good cross platform readability) 
#-(import other functions as necessary: os...)
import random # could be useful for randomizing trials later on 
import os # allows you to find files and save data
```
