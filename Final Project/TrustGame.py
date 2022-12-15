# -*- coding: utf-8 -*-

#INTRODUCTORY COMMENTS 
#In the virtual multi-round trust game, participants play 10 rounds with each "trustee" for a total of 30 rounds (Phan et al., 2010). 
# Particpants are instructed that they will play with other humans participants, despite them being computerized bots. Participants play as “investors” deciding to keep $1 or invest it 
# in their partner, the “trustee” (Delgado, 2007). If they keep the $1, the trustee receives nothing. If they choose to invest, the $1 is tripled and transferred to their trustee, 
# who can reciprocate trust by repaying the participant $1.50 or break trust by keeping all $3 (Delgado, 2007). 
# The three trustees are computer-simulated conditions with differing reciprocation rates, the percentage of trials where the trustee repays $1.50 (Phan et al., 2010). 
# The reciprocation rates for the trustworthy, neutral, and untrustworthy conditions are 75%, 50% and 25%, respectively (Phan et al., 2010). 

#IMPORT MODULES 
import sys
import random 
from random import sample
from ctypes import sizeof
from matplotlib.pyplot import hsv
from psychopy import visual, monitors, event, core, gui
from datetime import datetime
import numpy as np
import pandas as pd 
import os
import time

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
directory = os.getcwd() #set directory
path = os.path.join(directory, 'TrustGameData') 
if not os.path.exists(path): # if the directory is no there yet, make one with path specified
   os.makedirs(path)

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#create way to make new file name for each ppt: 
expInfo = {'subject_nr':0, 'age': 0} #create dictionary for gui 
myDlg = gui.DlgFromDict(dictionary=expInfo) #create gui & use dictionary
now = datetime.now()
dt_string = now.strftime("_date_%d-%m-%Y_time_%H:%M")
filename = (str(expInfo['subject_nr']) + dt_string + '_TrustGameData.csv') #save file for each ppt as a csv 

#STIMULI & TRIAL SETTINGS
nBlocks=3
nTrials=10
rt_clock = core.Clock()  # create a response time clock


#CREATION OF WINDOW & STIMULI - 15/100
#WINDOW
mon = monitors.Monitor('myMonitor', width=50.8, distance=60) #define the monitor parameters
mon.setSizePix([1600,900])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]
win = visual.Window(monitor=mon, color = 'Black', fullscr= True) #create window that is fullscreen and is black #CHANGE TO TRUE********

#STIMLULI

#Instructions
start_msg_1 = ('Instructions: You will play this game with a partner. \n \n In this game you are the “INVESTOR" and your partner is the "TRUSTEE" \n \n'
               'You start each round with $1 and must decide whether to KEEP or INVEST it. \n \n If you KEEP the $1, your partner receives $0. \n \n'
               'If you INVEST, the $1 transfers to your partner, and triples the amount to $3. \n' 
               'Your partner can split the $3 and you both receive $1.5 or your partner can keep the $3 for themselves and you recieve nothing for the round. \n \n'
               'You will play 3 games with a new partner each game. Each game will conist of 10 of rounds. \n \n'
               'If you understand the rules and consent to the game, enter "y". If you do not wish to play enter "n"')


#create players & their reciprocation rates
trustee_player_ID = ['Partner A','Partner B','Partner C'] 

#create nested list where the colour of the text and the colour of the font are denoted by 0, 0 [text, font]- later on I specify which is which
condition_list = [[0,0,0,1], [0,0,1,1], [0,1,1,1]] # #share (1) vs. keep (0) later I will shuffle the list conditions, then randomly select from within each condition 
trustee_decision = ['keep', 'share'] #keep = 0, share = 1 # dummy coding these will help with data analysis later
ppt_choice = ['keep', 'invest']
participant_total_earnings = 0.00
bot_decison_delay = [] #how long the bot takes to reply
partner_text_colour = ["LightSkyBlue", "Plum", "Gold"]

#delete - colour_text = visual.TextStim(win, text= 'Text', color='black') 
block_text = visual.TextStim(win)
trial_text = visual.TextStim(win)
Finish_Text = visual.TextStim(win)
# delete fixation = visual.TextStim(win, text='+', color='black') #creating fixation stimulus

#Prefill lists for responses & results of trust game
sub_resp = [] #Empty list to record whether ppt decides to KEEP or INVEST the money 
response_time = [] #Empty list to record how long the ppt takes to decide whether to KEEP or INVEST the money 
condition = [] #Empty list to record the Partner reciprocation rate during each block (Trustworthy, untrustworthy, neurtal)
trial_earnings = [] #Empty list to record how much the particpant earned during a given trial 
sum_earnings = [] #Empty list to record how much the participant has earned total for that Block (will reset at the start of a new block)


#=====================
#START EXPERIMENT
#=====================

my_text = visual.TextStim(win, height=0.08, wrapWidth=1.8)
decision_text = visual.TextStim(win, height=0.08)
my_text.text = start_msg_1
my_text.draw()
win.flip()
keys = event.waitKeys(keyList=['y','n'], clearEvents =True)    #-allow participant to begin experiment if they consent
if keys[0] == 'n':
    win.close() #exit experiment if they do not consent
elif keys[0] == 'y': # continue on if they do consent

    random.shuffle(condition_list) #shuffle the order of the conditions 
    #could you do an if statement to assign proper condition w/ proper player- player names arent counterbalanced
    random.shuffle(trustee_player_ID) # this randomly shuffles the names of the Partners
    random.shuffle(partner_text_colour) #counterbalance colours

#=====================
#BLOCK SEQUENCE
#=====================

    for block in range(nBlocks):
        recip_rate = condition_list[block] #This is the reciprocation rate for each block
        partner = trustee_player_ID[block] #This will be the Partner for the each block
        partner_colour = partner_text_colour[block]
        participant_total_earnings = 0.00 #reset ppt earnings for each partner
    #Present Text for this block: 
        block_text.setPos((0, 0.25))
        block_text.setText('Block #' + str(block+1)) #set block_text to the current block
        my_text.setPos((0, -0.25))
        my_text.setText('You will play with ' + str(partner) + ' for this block. \n \n Press any key to continue.') # text indictating who they are playing with this block
        my_text.draw()
        block_text.draw() 
        win.flip() #present block text
        event.waitKeys() #proceed to trials once a key is pressed
    #=====================
    #TRIAL SEQUENCE
    #=====================  

        for trial in range(nTrials):
    #------Saving which condition occurs in the trial for csv file-----------
        #---- 0 = keep, 1 = share 
            if recip_rate == [0,0,0,1]: # if the reciprocate rate is 3 keep : 1 share, add the condition as untrustworthy to list
                condition.append("Untrustworthy")
            elif recip_rate == [0,0,1,1]: # if the reciprocate rate is 1 keep : 2 share, add the condition as neurtal to list 
                condition.append("Neutral")
            elif recip_rate == [0,1,1,1]: # if the reciprocate rate is 1 keep : 3 share, add the condition as trustworthy to list
                condition.append("Trustworthy")

    #--------Show ppt what trial they are on------------
            trial_text.setText('Trial #' + str(trial+1) + '\n \n Press any key to continue.') #set trial_text to the current trial
            trial_text.draw()
            win.flip() #present trial text
            event.waitKeys(clearEvents=True) #move to next thing once key is pressed
    # PARTICPANT DECISION:
            count=-1 #for counting keys
            start_time = rt_clock.getTime() #start time for decision
            my_text.setPos((0, 0.5)) #move text higher so it doesnt overlap with other text presented
            my_text.setColor(partner_colour)
            my_text.setText('You are playing with ' + str(partner)) # text indictating who they are playing with this round
            decision_text.setText('Would you like to KEEP the $1 for yourself or INVEST it with ' + str(partner) + '? \n \n Press "k" to KEEP and "i" to INVEST')
            my_text.draw()
            decision_text.draw()
            win.flip()
            #collect keypresses after flip
            keys = event.waitKeys(keyList=['k','i'], clearEvents =True)
            response_time.append(rt_clock.getTime() - start_time) #record how long it took the subject to make decision & press the key
            my_text.setPos((0, 0)) #reset the position of the text
            my_text.setColor('white')

#Once the particpant makes a decision, the decision must be recorded and the trial must continue based on their choice to keep or invest. 
            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get key for only the first response in that loop
                                    #get key for only the first response in that loop
                    sub_resp.append(keys[0]) #get key that they pressed- might be better to dummy code this 
                    #print(sub_resp) - delete***********************************
                if keys[0] == 'k': #IF THE PPT CHOOSES TO KEEP THE $1.00:
                    participant_total_earnings = participant_total_earnings + 1.00 #add $1 
                    sum_earnings.append(participant_total_earnings)
                    trial_earnings.append(1.00)
                    my_text.setText("You KEPT the money this round. \n Your round earnings = $1.00 \n Your sum total earnings = $" + str(participant_total_earnings) + "0 \n" + str(partner)+ "'s round earning = $0.00 \n \n \n Press any key to continue")
                    my_text.draw()
                    win.flip()
                    event.waitKeys()
                
                elif keys[0] == 'i': #IF THE PPT CHOOSES TO INVEST THE $1.00:
                    states = [".", "..", "..."]
                    first_run = True
                    i = 0
                    loop = True
                    timer = None
                    while loop:
                        if first_run:
                            timer = time.time()
                            first_run = False
                            #print(i)
                        my_text.setText("You chose to INVEST the $1, increasing it's value to $3 \n" + str(partner) + " will now decide whether to share the money with you or keep the money for themself." + "\n" + states[i]) #themself or themselves
                        my_text.draw()
                        win.flip()
                        time.sleep(0.2)
                        i = ((i + 1) % len(states))  
                        #print("word")
                        if (time.time() - timer) >= random.randint(2,8) and i == 0:       
                            loop = False                   
                # NOW THE "PARTNER" OF THE PARTICIPANT DECIDES WHETHER TO SHARE OR KEEP ALL THE MONEY TO THEMSELF
                    #A CHOICE OF 1 = SHARE W/ PPT
                    # A CHOICE OF 0 = KEEP THE $3
                    choice = random.choice(recip_rate) # this is the "partner" making a choice based on their reciprocation rate (25%, 50% or 75%)
                    #The choice is determined by the current Partner's reciprocaion rate 

                    #UNCOMMENT BELOW************************************************************ #change time 
                    #core.wait(round(random.uniform(2,4), 1)) #random amount of time from 2-4 seconds (making my bot partner a more life-like!)
                    #store in 
                    if choice == 1: #if the partner(bot) chooses to share, then 
                        participant_total_earnings = participant_total_earnings + (3.00/2.00) # the particpnats total earnings increase by $1.50
                        sum_earnings.append(participant_total_earnings) #the total sum amount for THIS block/condition is added to a list for saving data
                        trial_earnings.append(1.50) #The earnings for this trial ($1.50) is added to a list for saving data 
                    #REVEAL PARTNER DECISION TO PARTICIPANT:
                        my_text.setText(str(partner) + " decided to share with you and split the $3. \n Your total earnings this round = $1.50 \n Your sum total earnings = $ " + str(participant_total_earnings) + "0 \n" + str(partner)+ "'s earning this round = $1.50 \n \n Press any key to continue") #themself or themselves
                        my_text.draw()
                        win.flip()
                        event.waitKeys()
                    elif choice == 0: 
                        trial_earnings.append(0.00) # Add the earnings for this trial ($0.00) is to trial earning list to data saving 
                        sum_earnings.append(participant_total_earnings) # Add the participant total earnings, no change since last trial since the partner did not share
                    #REVEAL PARTNER DECISION TO PARTICIPANT:
                        my_text.setText(str(partner) + " decided to not split the money with you and keep the $3. \n Your total earnings this round = $0.00 \n Your sum total earnings = $ " + str(participant_total_earnings) + "0 \n" + str(partner)+ "'s earning this round = $3.00 \n \n Press any key to continue") #themself or themselves
                        my_text.draw()
                        win.flip()
                        event.waitKeys()
#END OF EXPERIMENT: 
    # Give the particpants their total earnings per block: 
    Finish_Text.setText("You have finished all three games. Here are your total earnings. \n \n "
                        "Earnings in Block 1: $" + str(sum_earnings[9]) + "0"
                        "\n \n Earnings in Block 2: $" + str(sum_earnings[19]) + "0"
                        "\n \n Earnings in Block 3 $:" + str(sum_earnings[29]) + "0"
                        "\n \n Press any key to end the experiment")
    Finish_Text.draw()
    win.flip()
    event.waitKeys()
# Create & save data frame 
    df = pd.DataFrame(data={
    "Block Number": [i for i in range(3) for j in range(10)], #records block number
    "Condition": condition, #records condition (i.e trustworthy, untrustworthy neurtal)
    "Trial Number": list(range(10))*3, # records trial number for each trial in a block
    "Subject Response": sub_resp, #records whether the participant chose to invest or keep their money
    "Subject Earning this Trial": trial_earnings, #records the amount the particpant gained for that trial
    "Subject Sum Earnings this round": sum_earnings, #records the total earnings thus far during a given block
    "Response Time (seconds)": response_time #records how long the participant took to make their decsion each trial
    })
    df.to_csv(os.path.join(path, filename), sep=',', index=False) #Create csv 
    win.close() #close window once done! 


# References 

# Phan, K., L., Sripada, C. S., Angstadt, M., & McCabe, K. (2010). Reputation for reciprocity engages the brain reward center. 
#   Proceedings of the National Academy of Sciences, 107(29), 13099-13104. 
#   https://doi.org/10.1073/pnas.1008137107

#Delgado, M. R., Frank, R. H., & Phelps, E. A. (2005). Perceptions of moral character modulate the neural systems of reward during the trust game. 
#   Nature Neuroscience, 8(11), 1611–1618. 
#   https://doi.org/10.1038/nn1575


