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


# If we want to teleport, we do stuff like this
#mc.player.setPos(playerPos.x, playerPos.y + 40, playerPos.z)
#time.sleep(10)

# So we can get the block types around the player by using this
# variable...
blockBelowPlayerType =  mc.getBlock(playerTilePos.x, playerTilePos.y -1 , playerTilePos.z)
# We should turn this into a generic wall function...
for i in range(6): # Walls
	for j in range(50): # height
		mc.setBlock(playerTilePos.x + 1 + i ,
                playerTilePos.y + j,
                playerTilePos.z + 3,
                10)

mc.postToChat('look around')
