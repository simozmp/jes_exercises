def mostCol(pic, color) :
  # @param pic: Picture;
  # @param color: String;
  
  # Variable initializations
  
  mostX = -1
  mostY = -1
  miniumDistance = 1000
  pDistance = -1
  
  # Recognizing the target color from the
  # input string ("red, "green and "blue" string accepted)
  
  if(color == "red") :
    target = makeColor(255,0,0)
  else :
    if(color == "green") :
      target = makeColor(0,255,0)
    else :
      if(color == "blue") :
        target = makeColor(0,0,255)
  
  # Cicle
  
  for p in getPixels(pic) :
    pDistance = distance(getColor(p), target)
    if(pDistance < miniumDistance) :
      mostX = getX(p)
      mostY = getY(p)
      miniumDistance = pDistance
  
  # Final check and output
  
  if((mostX == -1) or (mostY == -1) or (miniumDistance == 1000)) :
    print "Something went wrong."
  else :
    print "The most " + String(color) + " pixel has been found at (" + String(mostX) + ", " + String(mostY) + ")."
  
  openPictureTool(pic)
  

