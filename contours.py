def contours(pic, neighbourhoodSize, threshold) :
  # @param pic: Picture;
  # @param neighbourhoodSize: int;   Size of the neighbourhood to compare colors (for each pixel)
  # @param threshold: int;
  
  # usage notes: for a better result, is recommended to use the following range of settings:
  # 1) neighbourhoodSize = 1: threshold in range 30~100
  # 2) neighbourhoodSize = 2: threshold in range 100~200
  # 3) neighbourhoodSize = 3: threshold in range 150~250
  # NB: elaboration time increases as neighbourhoodSize does
  
  width = getWidth(pic)
  height = getHeight(pic)
  
  newPic = makeEmptyPicture(width, height, white)    # Creates the white canvas for the result
  
  for x in range(width) :          # Main cycles to scans each pixel of the x-axis ...
    for y in range(height) :       # ... and y-axis
      
      if isNeighborhoodFar(pic, x, y, width, height, neighbourhoodSize, threshold) :
        setColor(getPixel(newPic, x,y), black)
      
  return newPic

def isNeighborhoodFar(pic, x, y, width, height, size, threshold) :
  # @param pic: Picture;
  # @param x: int;           x axis coordinate of the central pixel
  # @param y: int;           y axis coordinate of the central pixel
  # @param width: int;
  # @param height: int;
  # @param size: int;        size of the neighbourhood
  # @param threshold: int;
  
  pixColor = getColor(getPixelAt(pic, x, y))    # Keep the color of the pointed pixel in order to compare it with its neighbor's
  
  for neighbourX in range(x-size, x+size) :         # Secondary cycle to scan each pixel of the neighbour (x-axis)
    if neighbourX < width and neighbourX >= 0 :     # Check done in order to avoid size overflows
      for neighbourY in range(y-size, y+size) :     # Secondary cycle to scan each pixel of the neighbour (y-axis)
        
        if (neighbourX != x and neighbourY != y) and (neighbourY < height) and (neighbourY >= 0) :  # Check done in order to avoid size overflows, ..
                                                                                                    # .. and to pass over the pointed pixel (x,y)
          if distance(getColor(getPixelAt(pic, neighbourX, neighbourY)), pixColor) > threshold :    # Check if neighbor is far enough to (x,y)
            return true
  
  return false