
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
  delta = float(getWidth(pic)) / float(stripesNumber)     # Width of the stripes (castings are done in order to
                                                          # prevent missing exchanges of stripes in (*) cycle)
  
  for stripe in range(0, (stripesNumber/2)*2, 2) :        # "(stripesNumber/2)*2" is done in order to
                                                          # avoid an odd number of stripes (in case 
                                                          # of odd number of stripes, the last one
                                                          # will remain untouched)
    
    for x in range(int(delta*stripe),int(delta*stripe)+int(delta)) :  # (*)
      for y in range(0,height) :
        pixelExchange(getPixelAt(pic,x,y), getPixelAt(pic,x+int(delta),y))
  
  return pic
