#!/usr/bin/env python
# basic imports
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connect to server
mc = minecraft.Minecraft.create()

# Useful stuff:
# mc.postToChat('Why are we talking?')

# Grab player position
playerPos = mc.player.getPos()

# If we want to teleport, we do stuff like this
mc.player.setPos(30,50,70)
#time.sleep(10)

