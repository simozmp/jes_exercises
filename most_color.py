def mostCol(pic, color) :
  # @param pic: Picture;
  # @param color: String;
  mostX = -1
  mostY = -1
  miniumDistance = 1000
  pDistance = -1
  
  if(color == "red") :
    target = makeColor(255,0,0)
  else :
    if(color == "green") :
      target = makeColor(0,255,0)
    else :
      if(color == "blue") :
        target = makeColor(0,0,255)
  
  for p in getPixels(pic) :
    pDistance = distance(getColor(p), target)
    if(pDistance < miniumDistance) :
      mostX = getX(p)
      mostY = getY(p)
      miniumDistance = pDistance
  
  print "The most " + String(color) + " pixel has been found at (" + String(mostX) + ", " + String(mostY) + ")."
  show(pic)
  showVars()

