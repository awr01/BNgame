from infra import * #Image , Text , Buttons , run , temp
from random import random

from Nate import Intro

players = [
  ( "f1.jpg" , ),
  ( "m1.jpg" , ),
  ( "f2.jpg" , ),
  ( "m2.jpg" , ),
  ( "f3.jpg" , ),
  ( "m3.jpg" , ),
  ( "f4.jpg" , ),
  ( "m4.jpg" , ),
  ( "f5.jpg" , ),
  ( "m5.jpg" , ),
  ( "f6.jpg" , ),
  ( "m6.jpg" , ),
  ( "f7.jpg" , ),
  ( "m7.jpg" , ),
  ( "f8.jpg" , ),
  ( "m8.jpg" , ),
  ( "f9.jpg" , ),
  ( "m9.jpg" , ),
  ( "f10.jpg" , ),
  ( "m10.jpg" , )
]




# ===================================================================================================================
def drag_start(event,obj):
  widget = event.widget
  coords = widget.coords( obj )
  # widget._offset = ( event.x - coords[0] , event.y - coords[1] )
  widget._offset = ( event.x - coords[0] , coords[1] )

def drag_motion(event,obj):
  widget = event.widget
  # widget.coords( obj , event.x - widget._offset[0] , event.y - widget._offset[1] )
  widget.coords( obj , event.x - widget._offset[0] , widget._offset[1] )

def draggable(canvas,obj):
  canvas.tag_bind( obj , "<Button-1>" , lambda x,y=obj : drag_start( x,y ) )
  canvas.tag_bind( obj , "<B1-Motion>", lambda x,y=obj : drag_motion( x,y ) )    
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

  # draggable( canvas , img2 )

  global gem_img
  gem_img = Im.open( path.join( dir , f'players/gem.png' ) )
  gem_img = gem_img.resize( (60 , 60) , Im.LANCZOS )
  gem_img = PhotoImage( gem_img )

  for t,label in enumerate( [ "Strength" , "Skill" , "Stamina" , "Speed" , "Armour" , "Luck" , "Magic" , "Weapon" ] ):
    txt2 = canvas.create_text( w/5 , h*(t+3)/15 , font=("Ariel", 36, "italic") , fill="white" , text = label )
    bbox = canvas.bbox(txt2)
    canvas.coords( txt2 , w/5 - (bbox[2]-bbox[0])/2 - 20 , h*(t+3)/14 )   
    widgets.append( txt2 )    
    line = canvas.create_line( w/5 , h*(t+3)/14 , w/2 , h*(t+3)/14 , fill="white" )

    imgx = canvas.create_image( w/5 + (10*t) , h*(t+3)/14 , image = gem_img )
    draggable( canvas , imgx )


  Buttons( ( "Previous" , lambda x = index : PlayerSelect( (index-1) % len(players) ) ) ,
           ( "Select" , lambda x = index : PlayerSelect2( index ) ) ,
           ( "Next" , lambda x = index : PlayerSelect( (index+1) % len(players) ) ) )
        
        
def PlayerSelect2( index ):
  global widgets
  for x in widgets: canvas.delete( x )
  widgets = []
  
  print( "Selected" , index )
  Intro()

if __name__ == "__main__": run()