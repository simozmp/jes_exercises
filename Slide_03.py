def greenBlueFilter (pic, percentage) :
  # @param image: Picture;
  # @param percentage: int;
  redRatio = 1 - (float(percentage)/100)
  for p in getPixels(pic) :
    originalRed = getRed(p)
    setRed(p, originalRed * redRatio)
  return pic

def greyScale(pic) :
  # @param pic: Picture;
  for p in getPixels(pic) :
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p, makeColor(intensity, intensity, intensity))
  return pic

def colScale(pic, color) :
  # @param pic: Picture;
  # @param color: String;
  if color == 'r' :
    for p in getPixels(pic) :
      intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
      setRed(p, intensity)
      setGreen(p,0)
      setBlue(p,0)
  else :
    if color == 'g' :
      for p in getPixels(pic) :
        intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
        setRed(p, 0)
        setGreen(p, intensity)
        setBlue(p, 0)
    else :
      if color == 'b' :
        for p in getPixels(pic) :
          intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
          setRed(p, 0)
          setGreen(p, 0)
          setBlue(p, intensity)
  return pic
  
def removeColor(pic, color) :
  # @param pic: Picture;
  # @param color: String;
  if color == 'r' :
    for p in getPixels(pic) :
      setRed(p, 0)
  else :
    if color == 'g' :
      for p in getPixels(pic) :
        setGreen(p, 0)
    else :
      if color == 'b' :
        for p in getPixels(pic) :
          setBlue(p, 0)
  return pic

def negativeFilter(pic) :
  # @param pic : Picture;
  for p in getPixels(pic) :
    setColor(p, makeColor(255 - getRed(p), 255 - getGreen(p), 255 - getBlue(p)))
  return pic

## ------- *FromFile functions ---------

def greenBlueFilterFromFile(path, percentage) :
  # @param path: String;
  # @param percentage: int;
  pic = makePicture(path)
  return greenBlueFilter(pic, percentage)

def colScaleFromFile(path, color) :
  # @param path: String;
  # @param color: String;
  pic = makePicture(path)
  return colScale(pic, color)

def greyScaleFromFile(path) :
  # @param path: String;
  pic = makePicture(path)
  return greyScale(pic)

def removeColorFromFile(path, color) :
  # @param path: String;
  # @param color: String;
  pic = makePicture(path)
  return removeColor(pic, color)

def negativeFilterFromFile(path) :
  # @param path: String;
  pic = makePicture(path)
  return negativeFilter(pic)
