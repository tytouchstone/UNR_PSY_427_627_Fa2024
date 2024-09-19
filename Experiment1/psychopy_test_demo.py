#%% Psychopy demo script 2
#from psychopy import sound

from psychopy import visual, core
# Create a small screen window, 
win = visual.Window([400,400])
# Create a simple tezt message
message = visual.TextStim(win, text='hello')
# Automatically draw every frame
message.autoDraw = True  
win.flip()
core.wait(1.0)
# Change properties of existing stim
message.text = 'world'  
win.flip()
core.wait(1.0)
# Change properties of existing stim
message.text = 'bye!'  
win.flip()
core.wait(0.3)
print('\nClosing...\n')
win.close()

# %%