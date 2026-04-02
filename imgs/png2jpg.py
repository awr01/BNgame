#! /bin/python3

from PIL import Image as Im
import glob, os


changes = []

for file in glob.glob( f"*.png" ):
  
  file.replace( "\\" , "/" )
  
  newfile = file[:-4] + "z.jpg"  
  print( file , "->" , newfile )
  
  img = Im.open( file ).convert( 'RGB' )
  img.save( newfile )
  
  changes.append( ( file , newfile ) )
 

 
for src in [ "../Bella.py" , "../Nate.py" ]:
  with open( src , "r" ) as f:
    x = f.read()
    for From,To in changes: x = x.replace( "/"+From , "/"+To )

  with open( src , "w" ) as f:
    f.write( x )


    
