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

blocks=['AIR', 'STONE', 'GRASS', 'DIRT', 'COBBLESTONE', 'WOOD_PLANKS', '', 'BEDROCK',
    'WATER_FLOWING', 'WATER_STATIONARY', 'LAVA_FLOWING', 'LAVA_STATIONARY', 'SAND', 'GRAVEL',
    'GOLD_ORE', 'IRON_ORE', 'COAL_ORE', 'WOOD','NONE',
    'NONE', 'GLASS', 'LAPIS_LAZULI_ORE', 'LAPIS_LAZULI_BLOCK' , 'NONE', 'SANDSTONE', 'NONE', 'BED'  ,
    'NONE', 'NONE', 'NONE', 'COBWEB', 'GRASS_TALL', 'NONE', 'NONE', 'NONE', 'WOOL' , 'NONE', 'FLOWER_YELLOW', 'FLOWER_CYAN', 'MUSHROOM_BROWN', 'MUSHROOM_RED', 'GOLD_BLOCK', 'IRON_BLOCK', 'STONE_SLAB_DOUBLE', 'STONE_SLAB', 'BRICK_BLOCK', 'TNT', 'BOOKSHELF', 'MOSS_STONE', 'OBSIDIAN', 'TORCH', 'FIRE', 'NONE', 'STAIRS_WOOD', 'CHEST', 'NONE', 'DIAMOND_ORE', 'DIAMOND_BLOCK', 'CRAFTING_TABLE', 'NONE', 'FARMLAND', 'FURNACE_INACTIVE', 'FURNACE_ACTIVE', 'NONE', 'DOOR_WOOD', 'LADDER', 'NONE', 'STAIRS_COBBLESTONE', 'NONE', 'NONE', 'NONE', 'DOOR_IRON', 'NONE', 'REDSTONE_ORE', 'NONE', 'NONE', 'NONE', 'NONE', 'SNOW' , 'ICE'   , 'SNOW_BLOCK', 'CACTUS', 'CLAY', 'SUGAR_CANE', 'NONE', 'FENCE', 'NONE', 'NONE', 'NONE', 'GLOWSTONE_BLOCK' , 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'BEDROCK_INVISIBLE', 'NONE', 'NONE', 'STONE_BRICK', 'NONE', 'NONE', 'NONE', 'GLASS_PANE', 'MELON', 'NONE', 'NONE', 'NONE', 'FENCE_GATE',
]
def plane(mc, loc, blocktype=45):
    '''
    We will build a 3x4 plane and drop an air block and
    ladder in the center
    '''
    for x in range(3):
        for z in range(4):
            mc.setBlock(loc.x + x, loc.y, loc.z + z, blocktype)
    # Now we place air in the middle
    mc.setBlock(loc.x + 1, loc.y, loc.z + 2, block.AIR)
    mc.setBlock(loc.x + 1, loc.y, loc.z + 1, block.AIR)
    # Our ladder. Doesn't work... so we just have a 2-block airgap in the tunnel
    #mc.setBlock(loc.x + 1, loc.y, loc.z + 1, 76)

# Always go in the 'north' direction
playerTilePos.z += 1

# Our original origin(y)
origy = playerTilePos.y
# TODO: Clear a 3-tile hight above the tunnel

depth= input('How deep is the tunnel going to go (blocks)? ')
if depth>250:
    print('Too deep. Sorry, resetting to 10')
    depth=10
valid_ids=[]
for i,b in enumerate(blocks):
    if b.lower() != 'none':
        if b.lower() !='':
            valid_ids.append(i)
            print i,b

blockid=input('give me a blockid (45=brick, default): ')
if blockid in valid_ids:
    print('using {} as blockid').format(blocks[blockid])
else:
    print('Blockid is wrong. defaulting to brick')
    blockid=45

# Tunnel is 100 deep
for y in range(depth):
    playerTilePos.y = origy -y
    plane(mc, playerTilePos, blockid)

mc.postToChat("Tunnels are nearby!")
