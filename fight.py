
from player import *

plr = player(
    name = "Nate the Great",
    strength = 50,
    skill = 75,
    magic = 10,
    stamina = 100,
    speed = 50,
    armour = 20,
    luck = 80,
    coins = 18
  )



opponent = player(
    name = "Slugward the Ork",
    strength = 90,
    skill = 20,
    magic = 0,
    stamina = 100,
    speed = 20,
    armour = 60,
    luck = 40
  )




def fight( a , b ):

  print( a , "vs" , b )

  acounterattack = 0
  bcounterattack = 0

  while True:
    print()

    aspeed = a.speed + (a.luck * random()) + acounterattack
    bspeed = b.speed + (b.luck * random()) + bcounterattack

    print( aspeed , "vs" , bspeed )
    
    if aspeed > bspeed :
      print( a , "attacks")
      attacker , defender = a , b
      acounterattack , bcounterattack = -25 , +25
    else:
      print( b , "attacks")
      attacker , defender = b , a
      bcounterattack , acounterattack = -25 , +25

    attack = (( attacker.strength + attacker.skill + attacker.weapon ) / 3) + (attacker.luck * random())
    defense = (( defender.stamina + defender.armour )/2) + (defender.luck * random())

    print( attack  , defense)
    hit = attack - defense
   

    if hit > 0:
      print( "hit got through" , hit )
      defender.stamina -= int(hit)
      if defender.stamina <= 0: 
        print( defender , "is defeated" )
        break
      else:
        print(defender, "stamina = ", defender.stamina)
    else:
      print( "hit got blocked" , hit )
      attacker.weapon += int(0.25*hit*random())

      if attacker.weapon <= 0:
        print( attacker , "weapon is destroyed" )
        break
      else:
        print(attacker, "weapon",attacker.weapon)






fight( plr , opponent )
