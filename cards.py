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
        self.card_list = {}
        self.card_count = 0
        self.ready = False
        self.card_count_min = 45
        
class Card_Pool:
    def __init__(self):
        self.name = ""
        self.cards = {}
        self.card_count = 0
        self.next_id = 1
        
    def add(self,card):
        card.id = self.next_id
        self.next_id += 1
        self.cards[card.id] = card
        self.card_count += 1
        
    def delete(self,id):
        self.cards.pop(id)
        self.card_count -= 1
        
    def get_card(self,id):
        return self.cards[id]
        
class NetRunner_Card_Pool(Card_Pool):
    def __init__(self):
        Card_Pool.__init__(self)
        self.packs = {}
        
    def add(self,card):
        Card_Pool.add(self,card)
        if self.packs.has_key(card.pack):
            self.packs[card.pack].add(card.id)
        else:
            self.packs[card.pack] = [card.id]
    
    def delete(self,id):
        card = self.get_card(id)
        Card_Pool.delete(self,id)
        self.packs[card.pack].remove(id)
        if len(self.packs[card.pack]) == 0:
            self.packs.pop(card.pack)
        
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
        self.isUnique = False
        self.max_num = 3
        
class Card_Identity(NetRunner_Card):
    def __init__(self):
        NetRunner_Card.__init__(self)
        self.type = Card_Type.identity
        self.connection = 0
        self.deck_max_influence = 15
        self.deck_min_card_count = 45
        self.max_num = 1
        
    def check_deck_ready(self,deck):
        if deck.card_count < self.deck_min_card_count:
            deck.ready = False
            return False
        if deck.influence_used > self.deck_max_influence:
            deck.ready = False
            return False
        for (card,num) in deck.card_list:
            if num > card.max_num:
                deck.ready = False
                return False
        deck.ready = True
        return True
    
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
    
    def statistic_add(self,card):
        pass
    def statistic_del(self,card):
        pass
    def check_cycle_exist(self,cycle):
        for card in self.card_list.keys():
            if card.cycle == cycle:
                return True
        return False
        
    def check_pack_exist(self,pack):
        for card in self.card_list.keys():
            if card.pack == pack:
                return True
        return False
        
    def add(self,card):
        self.influence_used += self.get_influence(card) #must calculate the influence value before we put the card into the deck
        if self.card_list.has_key(card):
            self.card_list[card] += 1
        else:
            self.card_list[card] = 1
        self.card_count += 1
        
        self.cycle_set.add(card.cycle)
        self.pack_set.add(card.pack)
        self.statistic_add(card)
        
    def delete(self,card):
        if not self.card_list.has_key(card):
            return
        self.card_list[card] -= 1
        if self.card_list[card] == 0:
            self.card_list.pop(card)
            if not self.check_cycle_exist(card.cycle):
                self.cycle_set.remove(card.cycle)
            if not self.check_pack_exist(card.pack):
                self.pack_set.remove(card.pack)
        
        self.card_count -= 1
        self.influence_used -= self.get_influence(card)
        self.statistic_del(card)