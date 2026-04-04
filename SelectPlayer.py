from infra import * #Image , Text , Buttons , run , temp
from random import random

from Nate import Intro
from player import *

# plr = player( name = "Nate the Great", strength = 50, skill = 75, magic = 10, stamina = 100, speed = 50, armour = 20, luck = 80, coins = 18 )


players = [
  ( "f1.jpg" , ), 
  ( "m1.jpg" , player( name = "Forest rogue (m)" , strength = 50, skill =  75, magic =   5, stamina = 70, speed = 70, armour =  10, luck =  70, weapon =  50 ) ),
  ( "f2.jpg" , ),
  ( "m2.jpg" , player( name = "Paladin (m)"      , strength = 80, skill =  30, magic =   5, stamina = 70, speed = 20, armour =  80, luck =  40, weapon =  75 ) ),
  ( "f3.jpg" , ),
  ( "m3.jpg" , player( name = "Gambler (m)"      , strength = 50, skill =  80, magic =  15, stamina = 50, speed = 75, armour =  10, luck = 100, weapon =  20 ) ),
  ( "f4.jpg" , ),
  ( "m4.jpg" , player( name = "Elf (m)"          , strength = 35, skill =  80, magic =  45, stamina = 60, speed = 80, armour =  10, luck =  80, weapon =  10 ) ),
  ( "f5.jpg" , ),
  ( "m5.jpg" , player( name = "Dwarf (m)"        , strength = 80, skill =  20, magic =   0, stamina = 60, speed = 15, armour = 100, luck =  25, weapon = 100 ) ),
  ( "f6.jpg" , ),
  ( "m6.jpg" , player( name = "Mage (m)"         , strength = 20, skill =  90, magic =  90, stamina = 60, speed = 55, armour =   5, luck =  70, weapon =  10 ) ),
  ( "f7.jpg" , ),
  ( "m7.jpg" , player( name = "Sorcerer (m)"     , strength = 20, skill = 100, magic = 100, stamina = 55, speed = 50, armour =  10, luck =  50, weapon =  15 ) ),
  ( "f8.jpg" , ),
  ( "m8.jpg" , player( name = "Wolf clan (m)"    , strength = 60, skill =  70, magic =   5, stamina = 70, speed = 50, armour =  65, luck =  40, weapon =  40 ) ),
  ( "f9.jpg" , ),
  ( "m9.jpg" , player( name = "Beast hunter (m)" , strength = 70, skill =  60, magic =   5, stamina = 70, speed = 60, armour =  25, luck =  35, weapon =  75 ) ),
  ( "f10.jpg" , ),
  ( "m10.jpg" , player( name = "Gypsy (m)"       , strength = 65, skill =  55, magic =  20, stamina = 65, speed = 90, armour =   5, luck =  90, weapon =  10 ) ) 
]


# ===================================================================================================================
def drag_start(event,obj):
  widget = event.widget
  coords = widget.coords( obj )
  widget._offset = ( event.x - coords[0] , event.y - coords[1] )


def drag_motion(event,obj,box):
  widget = event.widget
  x,y = event.x - widget._offset[0] , event.y - widget._offset[1]
  if box: x , y = min( max( x , box[0] ) , box[2] ) , min( max( y , box[1] ) , box[3] )
  widget.coords( obj , x , y  )

def draggable(canvas,obj,box=None):
  canvas.tag_bind( obj , "<Button-1>" , lambda event,obj=obj,box=box : drag_start(event,obj) )
  canvas.tag_bind( obj , "<B1-Motion>", lambda event,obj=obj,box=box : drag_motion(event,obj,box) )    
# ===================================================================================================================


# ===================================================================================================================
widgets = []

@start
def PlayerSelect( index=0 ):
  Image( f'players/bg.jpg' ) 

  global player_img
  global widgets

  for x in widgets: canvas.delete( x )
  widgets = []
  
  player_img = Im.open( path.join( dir , f'players/{players[index][0]}' ) )
  x,y = player_img.size
  scale = 0.8*h/y
  player_img = player_img.resize( (int(scale*x),int(scale*y)), Im.LANCZOS )
  player_img = PhotoImage( player_img )  
  
  img2 = canvas.create_image( 3*w/4 , h/2 , image = player_img )
  widgets.append( img2 )


  global gem_img
  gem_img = Im.open( path.join( dir , f'players/gem.png' ) )
  gem_img = gem_img.resize( (60 , 60) , Im.LANCZOS )
  gem_img = PhotoImage( gem_img )

  for t,label in enumerate( [ "Strength" , "Skill" , "Stamina" , "Speed" , "Armour" , "Luck" , "Magic" ] ):
    txt2 = canvas.create_text( w/5 , h*(t+3)/15 , font=("Ariel", 36, "italic") , fill="white" , text = label )
    bbox = canvas.bbox(txt2)
    
    if len( players[index] ) > 1:
      attr = getattr( players[index][1] , label.lower() )    
      x = ( w/2 - w/5 ) * attr/100
    else:
      x = ( w/2 - w/5 ) * t/8
    
    canvas.coords( txt2 , w/5 - (bbox[2]-bbox[0])/2 - 30 , h*(t+3)/14 )   
    widgets.append( txt2 )    
    line = canvas.create_line( w/5 , h*(t+3)/14 , w/2 , h*(t+3)/14 , fill="white" )
    widgets.append( line )       
    imgx = canvas.create_image( w/5 + x , h*(t+3)/14 , image = gem_img )
    widgets.append( imgx )       
    
    # draggable( canvas , imgx , ( w/5 , h*(t+3)/14 , w/2 , h*(t+3)/14 ) )

  Buttons( ( "Previous" , lambda x = index : PlayerSelect( (index-1) % len(players) ) ) ,
           ( "Select"   , lambda x = index : PlayerSelect2( index ) ) ,
           ( "Next"     , lambda x = index : PlayerSelect( (index+1) % len(players) ) ) )
        
        
def PlayerSelect2( index ):
  global widgets
  for x in widgets: canvas.delete( x )
  widgets = []
  
  print( "Selected" , index )
  Intro()

if __name__ == "__main__": run()