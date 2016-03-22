
def digitalZoom(pic, ratio) :
  # @praram pic: Picture;
  # @param ratio: int, float;  It has to be >= 1
  
  width = getWidth(pic)
  height = getHeight(pic)
  newPic = makeEmptyPicture(width, height)      # The picture that will keep the result
  
  widthMargin = int((width - (width / ratio)) / 2)      # Size of the vertical margins
  heightMargin = int((height - (height / ratio)) / 2)   # Size of the horizontal margins
                                                        # (picture portion that will not
                                                        # be included in the zoomed one)
                                                        # NB. These castings are done in
                                                        # order to allow float ratio values
  
  i=0  #  *
  j=0  #  * indexes for iteration in newPic
  
  for x in range(widthMargin, (width - widthMargin)) :
    for y in range(heightMargin, (height - heightMargin)) :
      
      # For each pixel of the picture (without outer margins)..
      
      for newY in range(i,i+ratio) :
        if newY < height :                    # In order to avoid size overflows
          for newX in range(j,j+ratio) :
            if newX < width :                 # In order to avoid size overflows
            
              # For each pixel in the "ratio x ratio" squared neighbor
              # relative to the pixel x,y of the original image
              
              setColor(getPixel(newPic, newX, newY), getColor(getPixelAt(pic, x, y)))
        
      i=i+ratio  # Getting to the next pixel (newPic)
    
    i=0          # Leaving the row of pixels (newPic)
    j=j+ratio    # Getting to the next row of pixels (newPic)
  
  return newPic
