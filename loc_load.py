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
    playerTilePos = mc.player.getTilePos()
except:
    sys.exit('Minecraft pi is not running... quitting')

# Our saved file
mcpi_saves='mcpi.pkl'
homeloc=os.path.join('/','home','pi', mcpi_saves)

# Load our previously used dict. Bail on error
try:
    if os.path.exists(homeloc):
        saved_states=pickle.load(open(homeloc, 'rb'))
    else:
        sys.exit("unable to find saved file")
        saved_states={'locs':{}}
except:
    sys.exit('Error attempting to load the file')

if not saved_states.has_key('locs'):
    sys.exit('No saves in our file. Quitting')

saved_locs=saved_states['locs']
locations=sorted(saved_locs.keys())
print "Currently saved locations "
i = 0
for k ,v in sorted(saved_locs.items()):
    print("{}: {} - {}").format(i,k, v)
    i+=1

myloc=input('Choose a number: ')
if myloc >=0 and myloc < len(saved_locs):
    # Grab the key from our list of saved locations
    loc_key = locations[myloc]
    print myloc, loc_key
    print("teleporting to saved location {}").format(loc_key)
    mc.postToChat("Teleporting to saved location {}".format(loc_key))
    mc.player.setPos(saved_locs[loc_key])
else:
    print("I didn't understand that... Quitting")

