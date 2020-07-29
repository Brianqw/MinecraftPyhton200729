# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:13:48 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    hits=mc.events.pollBlockHits()

    if len(hits)>0:
        block=hits[0]
        x,y,z=block.pos.x,block.pos.y,block.pos.z
        mc.setBlock(x,y,z,41)
        if a==3:    
         mc.setBlock(x,y,z,57)   
        #mc.postToChat("你打到"+str(a))
        #mc.setBlock(x,y,z,41)



































