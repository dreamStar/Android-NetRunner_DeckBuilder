# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 10:38:23 2014

@author: dell
"""

class enum:
    def get_name(cls,x):
        return [s for (s,i) in cls.__dict__.items() if i == x][0]
    get_name = classmethod(get_name)

class Card_Type(enum):
    unknown = 0
    identity = 1    
    
    operation = 2
    agenda = 3
    ice = 4
    asset = 5
    upgrade = 6
    
    event = 7
    hardware = 8
    program = 9
    resource = 10
    
class Cycles(enum):
    others = 0
    core = 1
    genesis =2
    creation_and_control = 3
    spin = 4    
    honor_and_profit = 5
    
class Packs(enum):
    others = "其他"
    core = "基础"
    
    what_lies_ahead = "前途未卜"
    trace_amount = "重重追踪"
    cyber_exodus = "赛博迁徙"
    a_study_in_static = "静态研究"
    humanitys_shadow = "人性阴影"
    future_proof = "未来考验"
    
    creation_and_control = "创造与掌控"
    
    opening_moves = "起手开局"
    second_thoughts = "深思熟虑"
    mala_tempora = "脑叶癫痫"
    true_colours = "真实面貌"
    fear_and_loathing = "恐惧与憎恶"
    double_time = "双重时间"
    
    honor_and_profit = "荣誉与利益"
    

class Card:
    def __init__(self):
        self.name = ""
        self.id = -1
        self.image = ""
        
class Deck:
    def __init__(self):
        self.name = ""
        self.describe = ""
        self.card_list = []
        self.card_count = 0
        self.ready = False
        self.card_count = 0
        self.card_count_min = 45
        
class Statistics:
    pass
        
class NetRunner_Card(Card):
    def __init__(self):
        Card.__init__(self)
        self.cycle = ""
        self.No = ""
        self.pack = ""
        self.side = ""
        self.faction = ""
        self.influence = 0
        self.type = ""
        self.second_tpye_set = set()
        
    
class NetRunner_Deck(Deck):
    def __init__(self):
        Deck.__init__(self)
        self.side = ""
        self.cycle_set = set()
        self.pack_set = set()
        self.identity = 0
        self.influence_used = 0
        self.influence_max = 15
        self.statistics = Statistics()