# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 20:36:03 2014

@author: dell
"""

from cards import *

card_pool = NetRunner_Card_Pool()

c1 = Card_Identity()
c1.name = "噪音-超凡黑客"
c1.second_tpye_set.add("转基因人")
c1.connection = 0
c1.side = Sides.runner
c1.faction = Factions.anarch
c1.pack = Packs.core
c1.cycle = Cycles.core
c1.No = 1

card_pool.add(c1)