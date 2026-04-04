# #! /bin/python3

# import glob, os


# for ext in [ "png" , "jpg" ]:
  # files = []
  # lMax = 0
  # for file in glob.glob( f"*{ext}" ):
    # try:
      # i = int( file[:-4] )
      # if i > 10000: raise Exception( "boop" )
      # lMax = max( i , lMax )
    # except:
      # files.append( file )

  # for file in files:
    # lMax += 1
    # print( file , "->" , f"{lMax}.{ext}" )
    # os.rename( file , f"{lMax}.{ext}" )  
    
    
    
    
    
    
    
# #! /bin/python3

# import glob, os
# import subprocess

# for file in glob.glob( f"*.jpg" ):
  # subprocess.run([ "git", "mv" , file , f"x{file}" ] ) 
    