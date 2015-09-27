#!/usr/bin/env python
# basic imports
import mcpi.minecraft as minecraft
import mcpi.block as block
import os,time,sys
import cPickle as pickle

# connect to server
# Don't assume that minecraft is running...
try:
    mc = minecraft.Minecraft.create()
    playerPos = mc.player.getPos()
except:
    sys.exit('Minecraft pi is not running... quitting')

# Our saved file
mcpi_saves='mcpi.pkl'
homeloc=os.path.join('/','home', 'pi', mcpi_saves)

# Load our previously used dict. Bail on error
try:
    if os.path.exists(homeloc):
        saved_states=pickle.load(open(homeloc, 'rb'))
    else:
        print("Generating new saves file")
        saved_states={'locs':{}}
except:
    sys.exit('Error attempting to access saves file')

if not saved_states.has_key('locs'):
    saved_states['locs']={}

saved_locs=saved_states['locs']
# Ask for a name to save as. Loop through until
# we don't get an 'l'
myloc = 'l'
locations=sorted(saved_locs.keys())
while myloc == 'l':
    print "Currently saved locations "
    for k in locations:
        print k
    myloc=raw_input('give it a name or press "L" to list current locations ')

# Update our dictionary
saved_locs[myloc]=playerPos

# Now to wrap it up and add it back to our pickle dict
saved_states['locs'] = saved_locs

# Save back out.
pickle.dump(saved_states,open(homeloc,'wb'))

# Useful stuff:
mc.postToChat('Saved current position')
print("Position saved {}").format(playerPos)


