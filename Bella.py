
from infra import * #Image , Text , Buttons , run , temp
from random import random


coins = 18
HP = 100
Equipment = list()



Gold( coins )
Health( HP )


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
def Landing():
  Image( 'imgs/5.png' ) 
  Text( 
"""You walk slowly along the corridor looking at your surrondings, 
your feeling of wariness increasing. The silence and stillness of 
the corridor becomes increasingly obvious with each step you take:
It feels like the type of place you would see ghosts but there's 
nothing living around, not even a spider, despite the webs covering
the walls and furniture. The doors lining the corridor are immense, 
like the front doors of mansions. There are a lot of choices open
to you...""" )
  Buttons( ( "Door on the left" , Landing_Rm1 ) , 
           ( "1st Door on the right" , Landing_Rm2 ) , 
           ( "2nd Door on the right" , Landing_Rm3 ), 
           ( "Keep on walking down the corridor" , Landing_2 ) ) 
           #( "Go back down the stairs" , MainHall ) )
  

@temp
def Landing_Rm1(): 
  pass
  Image( 'imgs/.png' ) 

@temp
def Landing_Rm2(): 
  pass

@temp
def Landing_Rm3(): 
  pass

def Landing_2(): 
  Image( 'imgs/8.png' ) 
  Text("""You continue walking down the corridor,
 as you draw closer to the darkness
 more of the corridor becomes visable and you see
an ancient looking red velvet chair looking supprising appealing.
you suddenly realise how tired you are and 
everything seems a little more dreamlike... in your dreamlike 
state you spot a small  few gold coins hidden you scoop down 
nd pick them up.As you do so you have another wave of exustion...""")
  Buttons( ( "Do you sit down" , Landing_chr1) , ("continue walking" , Landing_3 ) ) 


@temp
def Landing_chr1(): 
  pass


def Landing_3(): 
  Image('imgs/7.png')
  Text("""As you continue walking everything gets
more and more drealike but you stagger on anyway determined
that you would not let this place whatever it is
get to you.Soon however it becomes apparent that you will need to
stop at somepoint and upon thinking this tou spot a open door with a bed inside.""")
  Buttons( ("""you have no choice 
    but to go in and rest""" , Landing_Rm4) )

def Landing_Rm4(): 
  Image()
  Text("""You stagger towards the bed finding it harder to stand with every step.
After what seems an age you finally get there and you are about to 
fall over from exhaustion you drop into the bed and promptly fall asleep.
Gain 5HP. However you find that you have lost three coins.
When you finally wake you feel refreshed and now that it's light nothing feels
so creepy.You wonder back into the corridor and stop
short in surprise. For just where the chair was last night is a door and from
behind that door there comes a pulling sensation. However you are now wary 
of this place and are not sure what to do.""")
  Buttons(("go into room" , Landing_Rm5) , ("you keep walking." , Landing_4))

  global HP
  HP = HP + 5
  Health( HP )

  global coins
  coins = coins - 3
  Gold( coins )


@start
def Landing_Rm5(): 
  Image('imgs/64.jpg')
  Text("""You enter the room gasping in amazement. You have entered the library.
you find yourself wondering along the shelves.As you get used get used to the amazing 
surrondings you start to notice something odd.All of the red books were put toghether facing 
towards something while all the other books were scattered everwhere. You follow the red books 
till you notice a small red book with a leather cover and the title is SPELLS. """)
  Buttons( ( "take book" , Landing_Rm5_TakeBk ) , 
           ( """Leave it, your 
feeling suspicious""" , Landing_Rm5_Next ) ) 


def Landing_Rm5_TakeBk(): 

  Text("""You take the book, put it in your backpack and walk on""")
  Buttons( ("Next" , Landing_Rm5_Next )) 
  Equipment.append( "Spell book" )


@start
def Landing_Rm5_Next(): 
  Image('imgs/117.jpg')



@temp
def Landing_4(): 
  pass


@temp
def MainHall(): 
  pass
# ===================================================================================================================



if __name__ == "__main__": run()
