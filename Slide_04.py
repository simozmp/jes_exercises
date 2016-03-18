def verticalMirroring(pic) :
  # @param pic: Picture;
  width = getWidth(pic)
  mirrorPoint = width/2
  for x in range(0, getHeight(pic)) :
    for y in range(0, mirrorPoint) :
      leftPixel = getPixel(pic, x, y)
      rightPixel = getPixel(pic, width-x-1, y)
      setColor(rightPixel, getColor(leftPixel))
  return pic

def verticalMirroringFromFile(path) :
  # @param path: String
  return verticalMirroring(makePicture(path))