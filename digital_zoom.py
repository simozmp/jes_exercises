def digitalZoomFixedSize(pic, ratio) :
  # @param pic: Picture;        Picture to zoom
  # @param ratio: int, float;   It has to be <0
  width = getWidth(pic)
  height = getHeight(pic)
  widthMargin = int((width - (width / ratio)) / 2)      # Size of the vertical margins
  heightMargin = int((height - (height / ratio)) / 2)   # Size of the horizontal margins
                                                        # (picture portion that will not
                                                        # be included in the zoomed one)
                                                        # NB. These castings are done in
                                                        # order to allow float ratio values
  if ratio < 1 :
    widthMargin = 0
    heightMargin = 0
  
  newPic = makeEmptyPicture(width, height)      # The picture that will keep the result
  
  return zoomProcessing(pic, ratio, width, height, abs(widthMargin), abs(heightMargin), newPic, true)

def digitalZoom(pic, ratio) :

  width = getWidth(pic)
  height = getHeight(pic)
  
  newPic = makeEmptyPicture(int(width*ratio), int(height*ratio))
  
  return zoomProcessing(pic, ratio, width, height, 0, 0, newPic, false)

def zoomProcessing(pic, ratio, width, height, widthMargin, heightMargin, newPic, fixed) :
  # @param pic: Picture;             Original picture to zoom
  # @param ratio: int, float;        It has to be <0
  # @param width: int;               Width of the original picture
  # @param height: int;              Height of the picture
  # @param widthMargin: int;         Size of the vertical margins
  # @param heightMargin: int;        Size of the horizontal margins
  # @param newPic: Picture;          Canvas, for the result
  # @param fixed: boolean;           Flag for fixed size features
  
  if fixed and ratio < 1:
    i = (height - int(ratio*height))/2
    j = (width - int(ratio*width))/2
  else :
    i=0  #  *
    j=0  #  * indexes for iteration in newPic
  
  for x in range(widthMargin, (width - widthMargin)) :
    for y in range(heightMargin, (height - heightMargin)) :
      
      # For each pixel of the picture (without outer margins)..
      
      color = getColor(getPixelAt(pic, x, y))
      
      for newY in range(i,i+ratio) :
        for newX in range(j,j+ratio) :
          if (newX>=0 and newY>=0 and newX < width and newY < height and fixed) or not fixed :
            
            setColor(getPixel(newPic, newX, newY), color)
      
      i=i+ratio  # Getting to the next pixel (newPic)
    
    if fixed and ratio < 1 :
      i=(height - int(ratio*height))/2          # Leaving the row of pixels (newPic)
    else :
      i=0
    
    j=j+ratio    # Getting to the next row of pixels (newPic)
  
  return newPic
