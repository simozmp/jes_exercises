def contours(pic, neighbour, treshold) :
 # @param pic: Picture;
 # @param neighbour: int;   Size of the neighbour to compare colors (for each pixel)
 # @param treshold: int;
 
 # usage notes: for a better result, is recommended to use the following range of settings:
 # 1) neighbour = 1: treshold in range 30~100
 # 2) neighbour = 2: treshold in range 100~200
 # 3) neighbour = 3: treshold in range 150~250
 # NB: elaboration time increases as neighbour value does
 
 width = getWidth(pic)
 height = getHeight(pic)
 
 newPic = makeEmptyPicture(width, height, white)    # Creates the white canvas for the result
 
 checkList = []   # List of booleans (it will keep,
                  # for each pixel of the image, flags
                  # relative to each pixel of the neighbor
                  # (neighbourX, neighbourY), that indicates if
                  # their color is enough distant to the
                  # pointed one (x,y)
 
 for x in range(width) :          # Main cycles to scans each pixel of the x-axis...
   for y in range(height) :       # ...and y-axis
     
     pixColor = getColor(getPixelAt(pic, x, y))    # Keep the color of the pointed pixel in order to compare it with its neighbor's
     
     for neighbourX in range(x-neighbour, x+neighbour) :         # Secondary cycle to scan each pixel of the neighbour (x-axis)
       if neighbourX < width and neighbourX >= 0 :              # Check done in order to avoid size overflows
         for neighbourY in range(y-neighbour, y+neighbour) :     # Secondary cycle to scan each pixel of the neighbour (y-axis)
           
           if (neighbourX != x and neighbourY != y) and (neighbourY < height) and (neighbourY >= 0): # Check done in order to avoid size overflows,
                                                                                                      # and to pass over the pointed pixel (x,y)
             
             checkList.append(distance(getColor(getPixelAt(pic, neighbourX, neighbourY)), pixColor) > treshold)    # Append boolean elements to the check list
     
     if true in checkList :                      # Check if all the pixels of the neighbour are distant enough to the pointed one (x,y)
       setColor(getPixelAt(newPic, x, y), black)
     else :
       setColor(getPixelAt(newPic, x, y), white)
     
     
     checkList = []          # Reset the check list for the next cycle
     
 return newPic