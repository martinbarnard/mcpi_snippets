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

# water is 9, air is 1
# We should turn this into a generic wall function...

def playback():
    myblocks=pickle.load(open('saved_loc','rb'))
    j = len(myblocks)
    for z in range(5,-5): # width
        for y in range(5,-5):
            for x in range(5,-5):
                mc.setBlock(playerTilePos.x + x,
                    playerTilePos.y + y,
                    playerTilePos.z + z,myblocks[j] )
                j -=1

if __name__=='__main__':
    print "playing back... please wait"
    playback()

