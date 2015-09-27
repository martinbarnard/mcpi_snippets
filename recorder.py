#!/usr/bin/env python
# basic imports
import mcpi.minecraft as minecraft
import mcpi.block as block
import pickle
# store out blocks
myblocks=[]
# connect to server
mc = minecraft.Minecraft.create()
playerPos = mc.player.getPos()
mc.postToChat('wait here...')
playerTilePos = mc.player.getTilePos()
# Better to use getBlocks(), but we need beg & end of each
# water is 9, air is 1
# We should turn this into a generic wall function...
def record_stuff():
    for x in range(-5,5): # width
        for y in range(-5,5): #
            for z in range(-5,5): #
                myblocks.append(mc.getBlock(playerTilePos.x + x,
                    playerTilePos.y + y,
                    playerTilePos.z + z))
    pickle.dump(myblocks, open('saved_loc', 'wb'))

def playback():
    myblocks=pickle.load(open('saved_loc','rb'))

if __name__=='__main__':
    print "recording... please wait"
    record_stuff()

