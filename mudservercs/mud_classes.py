import numpy as np

class World():
    
    def __init__(self, size = 16, maxplayers = 4):
        
        self.size = size
        self.maxplayers = maxplayers
        self.players = [None] * maxplayers
        self.playercount = 0
        self.randomgrid = np.random.randint(127, size = (size, size), dtype = 'int8')
        self.nsx = np.full((size + 1, size), -1, dtype = 'int8')
        self.nsx[1:-1, :] = np.random.randint(8, size = (size - 1, size), dtype = 'int8')
        self.ewx = np.full((size, size + 1), -1, dtype = 'int8')
        self.ewx[:, 1:-1] = np.random.randint(8, size = (size, size - 1), dtype = 'int8')
        self.monsters = ['Skeleton', 'Beholder', 'Imp', 'Fire Elemental']
        self.rooms = [[Room(self, self.randomgrid[a, b]) for a in range(size)] for b in range(size)]
    
    def add_player(self, name):
        
        if self.playercount == self.maxplayers:
            
            return 'Game is full'
        
        self.players[self.playercount] = Player(self, self.playercount, name)
        self.playercount +=1
        
        return 'Player created!'
        

class Room():
    '''docstring for Room'''

    def __init__(self, name, description, treasure=None, enemyList=None):
        self.name = name
        self.description = description
        self.treasure = [] if treasure is None else treasure
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.enemyList = [] if enemyList is None else enemyList
    def add_item(self,item):
        self.treasure.append(item)
    def remove_item(self,item):
        self.treasure.remove(item)
    def __str__(self):
        return(f'{self.name},{self.description},{self.treasure},{self.enemyList}')    
    def battle():
        pass    
        
        
class Player():
    '''docstring for Player'''

    def __init__(self, room, health, attack, inventory=None, weapon_on = None):
        self.room = room
        self.health = health
        self.attack = attack
        self.inventory = [] if inventory is None else inventory
        self.weapon_on = None if weapon_on is None else weapon_on
    def pick_up(self,item):
        self.inventory.append(item)
        print("You picked-up the item")  #add item to player inventory and remove it from room treasure
    def drop(self,item):
        self.inventory.remove(item)
        print("You dropped the item") #remove item to player inventory and add it to room treasure
    def equip_wpn(self,item):
        self.weapon_on = item
        self.attack = self.attack+item.damage
        e_item = item
        print('You equip:',e_item)    
    def unequip_wpn(self,item):
        self.weapon_on = None
        self.attack = self.attack-item.damage
        print('WPN ON:',self.weapon_on)
        print('Status:',self)    
    def use_potion(self,item):
        self.health = self.health + item.heal
        self.inventory.remove(item)
        print('You used a healing potion.Regained ',item.heal,'health.')
    def __str__(self):
        return ('{self.room},{self.health},{self.attack},{self.inventory}, {self.weapon_on}'.format(self=self))
    

class Item():
    '''docstring for Item'''

    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return('{self.name}, {self.description}').format(self=self)      

class Potion(Item):
    '''docstring for Potion Item subclass'''

    def __init__(self,name,description,heal):
        super().__init__(name,description)
        self.heal = heal

# class Trinket(Item):
#     '''docstring for Trinket Item subclass'''

#     def __init__(self,name,description):
#         super().__init__(name,description)
#         self.effect = effect  
#     def __str__(self):
#         return('{self.name}, {self.description}').format(self=self)

class Weapon(Item):
    '''docstring for Weapon Item subclass'''

    def __init__(self,name,description,damage):
        super().__init__(name,description)
        self.damage = damage
    def __str__(self):
        return(f'{self.name}, {self.description}, {self.damage}')    
        # return('testing')
        

class Monster():
    def __init__(self,name,health,damage,hit,loot=None):
        self.name = name
        self.health = health
        self.damage = damage
        self.hit = hit
        self.loot = [] if loot is None else loot
    def attack():
        pass 
    def run():
        pass
    def cast():
        pass
    def __str__(self):
        return(f'{self.name},{self.health},{self.damage},{self.hit},{self.loot}')