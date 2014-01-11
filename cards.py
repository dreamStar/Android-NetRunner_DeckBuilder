# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 10:38:23 2014

@author: dell
"""

class enum:
    def get_name(cls,x):
        return [s for (s,i) in cls.__dict__.items() if i == x][0]
    get_name = classmethod(get_name)
    
class Sides(enum):
    others = 0
    corporation = 1
    runner = 2
    
class Factions(enum):
    neatual = 0
    
    jinteki = 1
    nbn = 2
    haas = 3
    weyland = 4
    
    anarch = 5
    criminal = 6
    shaper = 7

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
        self.card_count_min = 45
        
class Statistics:
    pass
        
class NetRunner_Card(Card):
    def __init__(self):
        Card.__init__(self)
        self.cycle = Cycles.others
        self.No = 0
        self.pack = Packs.others
        self.side = Sides.others
        self.faction = Factions.neatual
        self.influence = 0
        self.type = Card_Type.unknown
        self.second_tpye_set = set()
        
class Card_Identity(NetRunner_Card):
    def __init__(self):
        NetRunner_Card.__init__(self)
        self.type = Card_Type.identity
        self.connection = 0
        self.deck_max_influence = 15
        self.deck_min_card_count = 45
        
    def check_deck_ready(self,deck):
        if deck.card_count < self.deck_min_card_count:
            deck.ready = False
            return False
        if deck.influence_used > self.deck_max_influence:
            deck.ready = False
            return False
    
    def get_influence(self,card):        
        if card.faction == self.faction:
            return 0
        if card.type == Card_Type.agenda:
            return 999
        return card.influence
        
    
class NetRunner_Deck(Deck):
    def __init__(self):
        Deck.__init__(self)
        self.side = Sides.others
        self.faction = Factions.neatual
        self.cycle_set = set()
        self.pack_set = set()
        self.identity = 0
        self.influence_used = 0
        self.influence_max = 15
        self.statistics = Statistics()
        
    def check_ready(self):
        try:
            return self.identity.check_deck_ready(self)
        except:
            return False
            
    def get_influence(self,card):
        return self.identity.get_influence(card)
        
    def set_indentity(self,identity):
        self.identity = identity
        self.side = identity.side
        self.faction = identity.faction
        self.influence_max = identity.deck_max_influence
        self.card_count_min = identity.deck_min_card_count
        self.influence_used = sum(map(self.get_influence,self.card_list))
        self.ready = self.check_ready()