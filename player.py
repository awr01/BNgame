


# coins = 18
# HP = 100
# Equipment = list()

class player:

  def __init__( self,
                name,
                strength,
                skill,
                magic,
                stamina,
                speed,
                armour,
                luck,
                weapon = 40,
                coins = 0,
                Equipment = list()
               ):
    self.name = name
    self.coins = coins
    self.Equipment = Equipment
    self.strength = strength
    self.skill = skill
    self.magic = magic
    self.stamina = stamina
    self.speed = speed
    self.armour = armour
    self.luck = luck
    self.weapon = weapon
    
    print( name , strength + skill + magic + stamina + speed + armour + luck + weapon )

  def __str__( self ):
    return self.name
