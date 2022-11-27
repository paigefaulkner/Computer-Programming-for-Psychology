# Assignment 8

## PsychoPy keypress exercises
### 1. event.getKeys is prone to collect as many responses as you can make in a trial, but often times you only want to collect one response for a trial.Come up with a solution so that only a single response is recorded from event.getKeys (e.g., ignoring all responses after the first response). Hint: one solution is used somewhere else in level 6.

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


### 2. Statement placement in your script is very important when collecting responses and refreshing keypresses. What happens if you put event.ClearEvents within the trial loop instead of outside the trial loop? What happens if you unindent the "if keys:" line?

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

