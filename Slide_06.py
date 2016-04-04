def redEyeRemover(pic, topLeftCorner_x, topLeftCorner_y, bottomRightCorner_x, bottomRightCorner_y) :
  # @param pic: Picture
  # @param topLeftCorner_x: int
  # @param topLeftCorner_y: int 
  # @param bottomRightCorner_x: int
  # @param bottomRightCorner_y: int
  
  # Tested with jenny-red.jpg, with corners at:
  # (100, 80) (Top Left)
  # (210, 120) (Bottom Right)
  
  for x in range(topLeftCorner_x, bottomRightCorner_x) :
    for y in range(topLeftCorner_y, bottomRightCorner_y) :
      pix = getPixelAt(pic,x,y)
      if distance(getColor(pix), red) < 165 :
        setRed(pix, 0)
  
  return pic


def posterizeBw(pic, percentage) :
  # @param pic: Picture
  # @param percentage: int (0 <= percentage >= 100)
  
  if 0 <= percentage and percentage <= 100 :
    limit = int((float(percentage)/100)*256)
    
    for pix in getAllPixels(pic) :
      if (getRed(pix) + getGreen(pix) + getBlue(pix))/3 > limit :
        setColor(pix, white)
      else :
        setColor(pix, black)
    return pic
  else :
    return "ERROR"

