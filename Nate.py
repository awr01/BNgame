from infra import * #Image , Text , Buttons , run , temp
from random import random

from Bella import Landing

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

  def __str__( self ):
    return self.name



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
exit()


Health( plr.HP )




# ===================================================================================================================
print( "FIX FIGHT!!!" )
from datetime import datetime
def Fight( skill , stamina ):
  print( skill , stamina )
  Text()
  Buttons()

  global fate_
  fate_ , s = Im.open( "img2/fate1.png" ) , int(3*h/4)
  fate_ = fate_.resize((s,s), Im.LANCZOS)
  fate_ = PhotoImage( fate_ )
  fate = canvas.create_image( w/2 , h/2 , image=fate_ )
  now=[None]
  
  # def Set( now ):     
    # now[0]=datetime.now()
    
  # def Release( now ): 
    # print( datetime.now()-now[0] )
  
  # canvas.tag_bind( fate , "<ButtonPress-1>", lambda x , y=now : Set( y ) )
  # canvas.tag_bind( fate , "<ButtonRelease-1>", lambda x , y=now : Release( y )  )

# ===================================================================================================================






# ===================================================================================================================
@start
def Intro():
  Image( 'imgs/3.png' ) 
  Text( 
"""You trudge through the... you want to say 'forest' but it has been a 
long time since you have seen any living trees. You wonder if you should 
just give up and go home... Perhaps treasure quests are a fool's errand... 
just like everyone in the village told you. But to return empty handed 
would prove them right. As you ponder your wisdom in undertaking the quest,
you notice something that makes your heavy heart leap, something sitting in
a muddy puddle, something glinting, something gold.""" )
  Buttons( ( "Next" , Intro2 ) )
  
def Intro2():
  Text( 
"""You rush over to it and see a small gold statuette that looks like a pair
of hands cupping a dial marked in strange runes. Whatever it is, the gold alone
must be worth something. No-one would have discarded such a treasure on purpose,
so you assume that a previous traveller has dropped it, and you pick it up""" )
  Buttons( ( "Back" , Intro ) , ( "Next" , Intro3 ) )
 
def Intro3():
  Text( 
"""Examining it, you realise with a sense of dread what you have done. You have
become the 'proud' owner of a cursed object:

The Hands of Fate

Until you can rid yourself of this accursed object, randomness will affect every
battle you undertake and various decisions you will need to make. Reluctantly
you put it in your bag and trudge on...
""" )
  Buttons( ( "Back" , Intro2 ) , ( "Next" , TheCastle ) )  
# ===================================================================================================================

# ===================================================================================================================
def TheCastle():
  Image( 'imgs/2.png' ) 
  Text( 
"""You are standing in front of a creepy grey castle.
Your knees are knocking but the allure of the 
treasure makes you brave. You step through the 
door which swings shut behind you. You are 
trapped in the castle... there's no going back now.""" )
  Buttons( ( """You have no choice
but to go forward""" , EntranceHall ) )
# ===================================================================================================================


# ===================================================================================================================
def EntranceHall():
  Image( 'imgs/1.png' )
  Text( 
"""You are in a hallway lined
with suits of armour and weapons. 
There is a rare sword: 
Do you want to take it?""")
  Buttons( ( "Yes, take it" , EntranceHall_take ) , 
           ( "Leave it and move forward" , EntranceHall_donttake ) )

def EntranceHall_take():
  Text( """As you try to take 
the sword, the two suits of 
armour nearest to the sword 
spring to life, grab weapons 
from the wall and swing them
in your direction. There's a 
single rusty sword lying on the
floor: Do you grab it and fight,
or do you attempt to run away?""" )
  Buttons( ( "Take the sword and fight" , EntranceHall_takeSword ) , 
           ( "Leave it and run away" , EntranceHall_RunAway ) )

def EntranceHall_takeSword():
  Text( """When you grab the sword it 
gives your hand an electric shock.
Lose 5HP. Do you fight, or do you drop
the sword and run away?""" )
  Buttons( ( "Fight" , EntranceHall_fight ) , 
           ( "Drop it and run away" , EntranceHall_RunAway ) )
  
  plr.HP = plr.HP - 5
  Health( plr.HP )

def EntranceHall_fight():
  Text( """As you try to raise the sword 
you are surprised by the weight, but the 
sight of the armour lunging towards you 
gives you all the strength you need. Do 
you take on the left the right or both
at the same time?""" )  
  Buttons( ( "Left" , lambda: EntranceHall_fightlr( "left" ) ) , 
           ( "Both" , EntranceHall_fightboth ) , 
           ( "Right" , lambda: EntranceHall_fightlr( "right" ) )             
          )
  
def EntranceHall_fightlr( lr ):
  if lr == "left": weapon , skill , stamina = "axe"  , 4 , 6
  else:            weapon , skill , stamina = "pike" , 5 , 5
  
  Text( f"""You lunge towards the {lr} 
  suit which immediately takes a swing at
  your head with his {weapon}.""" ) 

  Buttons( ( "Next" , lambda: Fight( skill , stamina ) ) )  

def EntranceHall_fightboth():
  Text( f"""You take a swipe at both the 
lunging suits of armour... and miss both!
Luckily for you, the brazeness of your 
approach surprises your opponents and causes
them to collide: Whoever enchanted them had 
not taken your bold style into account. The 
two suits of armour collapse in a jumbled pile of
pieces on the floor. You thank your lucky
stars, pick up the rare sword and make your
way to the doorway.""" ) 

  Buttons( ( "Next" , CorridorA ) )
  plr.Equipment.append( "Rare sword" )

def EntranceHall_RunAway():
  
  rndm = int( 10 * random() )
  
  if   rndm == 0: 
    msg = f"""Fortunately, it misses you and 
you make it safely through the arch"""
  elif rndm  < 4: 
    msg = f"""You are quick and dodge out of
the way, but it still cuts your leg. Lose {rndm}HP."""
  elif rndm  < 7: 
    msg = f"""You are too slow and the spear clips
your arm, cutting your wrist. Lose {rndm}HP."""
  else:
    msg = f"""You are far too slow and the spear digs 
deep into your shoulder. Lose {rndm}HP."""
      
  Text( f"""As you run to the door at the
far end of the room,one of the suits grabs 
a spear and hurls it towards your throat.
{msg}""" )

  plr.HP = plr.HP - rndm
  Health( plr.HP )

  Buttons( ( "Next" , CorridorA ) )
  
def EntranceHall_donttake():
  Text( """You decide to leave the sword
  and move through to the next room. As 
  you go you think you see some of the 
  suits of armour watching you but you 
  tell yourself you are being silly.""" )
  
  Buttons( ( "Next" , CorridorA ) )  
# ===================================================================================================================



# ===================================================================================================================
def CorridorA():
  Image( 'imgs/87.jpg' ) 
  Text( """The arch leads to a long corridor
made out of light grey granite with 
tapestries adorning the walls.Towards
the end of the corridor there is a door 
with a light glowing behind it.You feel oddly
drawn to it. Do you straight to the room or 
do you first explore the tapestries?""" )  

  Buttons( ( "Go straight to the room" , MainHall ) , 
           ( "Explore the tapestries" , CorridorA_Explore ) )  
        
def CorridorA_Explore():          
  Text( """You decide to explore behind 
the tapestries.The first 9 have nothing
to reveal but cobwebs and dust, it's clear
no one has moved them for a long time.
You are almost ready to give up but persist
and are rewarded as the last tapestry reveals 
a hole in the wall. Try as you might, you 
cannot see anything, it is just too dark inside.
Will you put your hand inside, or will you 
ignore it and go straight to the room?""" )
  Buttons( ("Go straight to the room" , MainHall ) , 
           ( "Stick your hand in the hole" , CorridorA_ExploreHole ) )     

         
def CorridorA_ExploreHole():           
  Text( """You pluck up the courage to stick 
  your hand in the hole. You draw your hand back
  when it encounters something solid.
  When you reach back in you grasp the 
  solid thing and pull it out. It is
  a oak chest. Do you want to open the 
  chest or reach back into the hole?""" )
  Buttons( ( "Reach back into the hole", CorridorA_ExploreHole2 ) ,
           ( "Open the chest", CorridorA_OpenChest ) )
          
       
def CorridorA_ExploreHole2():
  Text( """As you reach into the
  hole again you feel cobwebs .
  You hesitate for a minute 
  then remind yourself of treasure
  and start digging through the thick
  mesh of cobwebs. As soon as you get 
  through the webs a rat sinks its 
  teath into your hand. Lose 3HP.You sourly
  tell yourself thats what you get for  being
  so greedy! You   immediately draw back
  your hand.  If you havent already you may open
  the chest, otherwise go to the lighted 
  room""" )
  Buttons ( ( "Open the chest" , CorridorA_OpenChest ),
            ( "Go straight to the room" , MainHall ) )
  
  plr.HP = plr.HP - 3
  Health( plr.HP )
  
  
         
def CorridorA_OpenChest():
  Text("""When you try to open the chest
you discover it is firmly locked. You decide
 it will be worth it and start to bash the
lock. A shard of metal flies off and stabs 
you in the shoulder.Lose 4HP. But the final 
blow breaks open the lock. You flip back the 
lid to reaveal a skelatal hand you drop the 
chest to in horror.You peer down and see
there is a ring. You pull off the ring and 
examine it closely.It has runes over it.
Do you put on the ring or do you leave it 
and go to the lighted room?""" )
# ===================================================================================================================
  Buttons(("Put on the ring",CorridorA_WearRing),
          ("Go to room",MainHall))
  
  plr.HP = plr.HP - 4 
  Health( plr.HP )  
          
          
# ===================================================================================================================


def MainHall():
  Image( 'imgs/1001.png' ) 
  Text("""When you get to the ornate translucent
door you hesitate before shoving the door open.
You step through and see 6 suits of armour 
a roaring fire even though there is no one 
around ,an unearthly howling wind there is moss
 on the stairs but strangly nowhere else 
 and on top of the staircases there are two doors
 but although there are 2 glass windows next too 
 them they are as dark as ink and there are tapestries
 adorning the walls.As you walk across the room you 
 find a trap door!Upon opening it you find steps 
leading deep down.Do you go upstairs or do you go
down into the gloom? """)  
  Buttons(("Creep downstairs",Dungeon_Entrance),
          ("Go upstairs",Landing))    
# ===================================================================================================================
      
def CorridorA_WearRing():
  Text("""You decide to put the ring on
and it was a good decicion as this ring 
was made and owned by the white wizard 
Azabarn the Great. Plus 5HP. Go to the 
lighted room.""")

  Buttons(("Go to the room",MainHall))
  
  
  plr.HP = plr.HP + 5
  Health( plr.HP )

@start
def Dungeon_Entrance():
  Image( 'imgs/8.jpg' ) 
  Text("""You decide to descend the stairs and are on a
  walkway looking down into what is now clear to be the 
  dungeons. More stairs lead down to a giant grey cavernous 
  room: There is something on a table. Do you want to search  
  the cavern and see what is on the table, or continue along 
  the walkway?""" )
  Buttons( ("Search the cavern",Cavern_1),
          ( "Continue along the walkway",Walkway_1) )


def Cavern_1():
  Image("imgs/1003.png")
  Text("""You walk into the cavern and see what is on the
  table which turns out to be a brestplate orenately 
  decorated with a cross.Do you put it on or do you continue
   your search of the cavern?""") 
  Buttons(("Wear the armour",Cavern1_WearBrestplate     ),
          ("Continue searching",Cavern1_KeepSearching))       


def Cavern1_WearBrestplate():
  Image("imgs/1003.png")
  Text("""When you put on the armour a wave of strength 
    washes ver you.Plus 2HP.If you havent already you 
    may search the cavern otherwise go back to the 
    walkway.""") 
  Buttons(("Go to the walkway",Walkway_1),
          ("Continue searching",Cavern1_KeepSearching))       

  
  plr.HP = plr.HP + 2
  Health( plr.HP )


def Cavern1_KeepSearching():  
  Text("""The cavern is empty apart from a gold 
    coin in a crack in the floor.There is nothing
    else to be found.You look in the alcoves but 
    they are bare. There is a door but it is firmly 
    locked and your instincts tell you it's probably 
    too strong and hard to break your way through.""")
  Buttons( ("Try forcing the door anyway",lambda : Cavern1_BreakDoor( 1 ) ),
           ("Go to the walkway",Walkway_1))

   
  plr.coins = plr.coins + 1
  Gold( plr.coins )


def Cavern1_BreakDoor( count ):

  if   count == "1": label = ""
  elif count == "2": label = "2nd"
  elif count == "3": label = "3rd"
  else: label = f"{count}th"


  Text("""You throw your full weight against the door
          with all your strength, and end up with a 
          thoroughly bruised shoulder to show for it,
          but the door remains firmly shut. Lose 2 HP.""" ) 
  Buttons( ("Try forcing the door again", lambda : Cavern1_BreakDoor( count + 1 ) ),
           ("Go to the walkway",Walkway_1))

  
  plr.HP = plr.HP - 2
  Health( plr.HP )

  if plr.HP <= 0 : exit()




@start
def Walkway_1():  
  Text("""You go back onto the walkway and start walking down 
         it. Accidentaly you kick a stone and it falls through
         a crack in the stone clacking against the floor. It is 
         not a big sound but is enough to alert anything down 
         there of your presence. You feel somthing powerfully 
         urging you to go to  the cavern. Go into the cavern.""")
  Buttons( ("Go into the cavern",Cavern_2 ) )



def Cavern_2():    
  Image( "imgs/4a.png")
  Text("""As you decend the stairs you are met by a horrible 
    sight.There is a necromancer so skinny he would be that 
    skinny if he was a skelaton. He held a bone staff which had a 
    glowing purple crystal on top. Next to a fountain floats 
    a blue glowing spectre. Behind the necromancer is a pitch black
     arch. The necromanser waves his staff and the ghost glides 
     towards you. You have no choise but to fight it.""")




# @temp
# def Landing():  pass  
  
# Image( 'imgs/1.png' )
# EntranceHall_fightlr( "left" )

if __name__ == "__main__": run()