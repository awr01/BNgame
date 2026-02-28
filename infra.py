if __name__ == "__main__": exit()

from playsound3 import playsound
from tkinter import Tk , Canvas , CENTER
from PIL import Image as Im
from PIL.ImageTk import PhotoImage
import sys

root = Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda x : sys.exit() )
w,h = root.winfo_screenwidth() , root.winfo_screenheight()

canvas = Canvas( width=w , height=h , bg="black", highlightthickness=0 )
canvas.pack()
img = canvas.create_image( w/2 , h/2 )
rect = canvas.create_image(  w/2 , h/2 )
txt = canvas.create_text( w/2 , h/2 , font=("Ariel", 36, "italic") , fill="white" , justify=CENTER )

scroll = Im.open( "img2/scroll2.png" )
scroll = scroll.resize((400,150), Im.LANCZOS)
scroll = PhotoImage( scroll )
buttons = []

health = canvas.create_text( 70 , 20 , font=("Ariel", 20, "italic") , fill="white" , justify=CENTER )
gold  = canvas.create_text( w-70 , 20 , font=("Ariel", 20, "italic") , fill="white" , justify=CENTER )


def play():
  playsound( 'audio.mp3' , block=False )
  root.after( (60*60*1000)+2 , play ) # File is 1hour and 1s long, so after 1 hour and 2s, come back and play it again...  
play()


def Audio( filename ):
  playsound( filename , block=False )

def Image( filename="dummy.png" ):
  # Update the background and text
  global imgfile # stop the image file data going out of scope!
  imgfile = Im.open( filename )
  x,y = imgfile.size
  scale = min( w/x , h/y )
  imgfile = imgfile.resize( (int(scale*x),int(scale*y)), Im.LANCZOS )
  imgfile = PhotoImage( imgfile )
  canvas.itemconfigure( img , image = imgfile )

def Text( text="" ):
  canvas.itemconfigure( txt , text = text )
  x0,y0,x1,y1 = canvas.bbox( txt )
  global rect_
  rect_ = PhotoImage( Im.new('RGBA', (x1-x0, y1-y0), "#80808080" ) )
  canvas.itemconfigure( rect , image = rect_ )
  
def Buttons( *btns ):  
  # Delete any old buttons
  for (a,b) in buttons:
    canvas.delete( a )
    canvas.delete( b )
  buttons[:] = []

  # Create the new buttons
  dw = w /(len(btns)+1)
  for i,(text,callback) in enumerate(btns):
    a = canvas.create_image( (i+1)*dw , 0.9*h ,image=scroll)
    b = canvas.create_text( (i+1)*dw , 0.9*h , font=("Ariel", 18, "italic") , fill="black" , justify=CENTER , text=text )
    buttons.append( (a,b) )    
    canvas.tag_bind( a , "<Button-1>", lambda x , y=callback: y() )
    canvas.tag_bind( b , "<Button-1>", lambda x , y=callback: y() )
    

  
  
def temp( func ):
  print( f"Unimplemented function: {func.__name__}" )
  
  #-----------------------------
  def myinner():         
    Text( f">>> {func.__name__} <<<" )
    Buttons()    
  #-----------------------------
    
  return myinner

start_ = None
def start( func ):
  global start_
  # if start_ is None: 
  start_ = func
  return func


import traceback
from tkinter import messagebox

# You would normally put that on the App class
def show_error(*args):
  err = traceback.format_exception_only(*args[:2])
  messagebox.showerror('Exception',err)

root.report_callback_exception = show_error


def run(): 
  if start_: start_()
  root.mainloop()



def Health( HP ):
  canvas.itemconfigure( health , text = f"{HP}HP" )  


def Gold( coins ):
  canvas.itemconfigure( gold , text = f"{coins} coins" )
