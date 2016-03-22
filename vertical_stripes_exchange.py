
def pixelExchange(sourcePixel, targetPixel) :
  # @param sourcePixel: Pixel;
  # @param targetPixel: Pixel;
  color = getColor(targetPixel)
  setColor(targetPixel, getColor(sourcePixel))
  setColor(sourcePixel, color)

def verticalStripesExchange(pic, stripesNumber) :
  # @param pic: Picture;
  # @param stripesNumber: int;    Number of stripes in the picture
  
  height = getHeight(pic)
  delta = getWidth(pic) / stripesNumber    # Width of the stripes
  
  # print getWidth(pic)    # debug message
  # print delta            # debug message
  
  for stripe in range(0, (stripesNumber/2)*2, 2) :        # "(stripesNumber/2)*2" is done in order to
                                                          # avoid an odd number of stripes (in case 
                                                          # of odd number of stripes, the last one
                                                          # will remain untouched)
    for x in range(delta*stripe,(delta*stripe)+delta) :
      # print String(x) + ", " + String(stripe)             # debug message
      for y in range(0,height) :
        pixelExchange(getPixelAt(pic,x,y), getPixelAt(pic,x+delta,y))
  
  return pic

#---

def floatToIntApprox(number) :
  # @param number: float
  
  if number%1 <= 0.5 :
    result = int(number)
  else :
    result = int(number) + 1
  
  return result