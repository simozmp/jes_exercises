def areTwins(pix1, pix2) :
  # @param pix1: Pixel;
  # @param pix2: Pixel;
  # @return boolean;     Two pixels are twin when the sum of the pix1
  #                      components is equal to the sum of the pix2 components
  
  return getRed(pix1)+getGreen(pix1)+getBlue(pix1) == getRed(pix2)+getGreen(pix2)+getBlue(pix2)

def haveTwinForEachPix(pic1, pic2) :
  # @param pic1: Picture;  First picture
  # @param pic2: Picture;  Second picture
  # @return boolean;       The function is intended to see if each
  #                        of the pixel's colors in the first picture
  #                        has a respective twin in the second one
  
  for pix1 in getAllPixels(pic1) :    # scans each pixel of the first picture
    hasTwin = false                   # flag for pix1 (true when the pix1 pixel has a twin in the second picture)
    
    for pix2 in getAllPixels(pic2) :  # scans each pixel of the second picture
      if areTwins(pix1,pix2) :        # tests if the two colors are twins, in that case:
        hasTwin = true                #   - keep track of the found twin
        break                         #   - break the pix2 cycle
      
    if not hasTwin :                  # if pix1 doesn't have any twin in the second picture ...
      return false                    # ... result is false
  
  return true

##                                           WITH DEBUG MESSAGES
## def haveTwinForEachPix(pic1, pic2) :
##   # @param pic1: Picture;
##   # @param pic2: Picture;
##   
##   for pix1 in getAllPixels(pic1) :
##     # DEBUG # print "-----Pix1:" + String(getRed(pix1)+getGreen(pix1)+getBlue(pix1))
##     
##     check = false
##     
##     for pix2 in getAllPixels(pic2) :
##       # DEBUG # print "--Pix2:" + String(getRed(pix2)+getGreen(pix2)+getBlue(pix2))
##       
##       if areTwins(pix1,pix2) :
##         # DEBUG # print "--     twins!"
##         check = true
##         break
##       
##     if not check :
##       # DEBUG # print "false!!!!"
##       return false
##   
##   return true


#
# I used the two following functions to build test pictures
#


def makeFirstPic() :
  pic = makeEmptyPicture(3,3,white)
  
  setColor(getPixelAt(pic,0,0), makeColor(1,2,3))  # r+g+b = 6
  setColor(getPixelAt(pic,1,0), makeColor(2,2,3))  # r+g+b = 7
  setColor(getPixelAt(pic,2,0), makeColor(3,2,3))  # r+g+b = 8
  setColor(getPixelAt(pic,0,1), makeColor(4,2,3))  # r+g+b = 9
  setColor(getPixelAt(pic,1,1), makeColor(5,2,3))  # r+g+b = 10
  setColor(getPixelAt(pic,2,1), makeColor(6,2,3))  # r+g+b = 11
  setColor(getPixelAt(pic,0,2), makeColor(7,2,3))  # r+g+b = 12
  setColor(getPixelAt(pic,1,2), makeColor(8,2,3))  # r+g+b = 13
  setColor(getPixelAt(pic,2,2), makeColor(9,2,3))  # r+g+b = 14
  
  return pic

def makeSecondPic() :
  pic = makeEmptyPicture(3,3,white)
  
  setColor(getPixelAt(pic,0,0), makeColor(1,2,3))  # r+g+b = 6
  setColor(getPixelAt(pic,1,0), makeColor(2,2,3))  # r+g+b = 7
  setColor(getPixelAt(pic,2,0), makeColor(0,2,3))  # r+g+b = 5
  setColor(getPixelAt(pic,0,1), makeColor(4,2,3))  # r+g+b = 9
  setColor(getPixelAt(pic,1,1), makeColor(5,2,3))  # r+g+b = 10
  setColor(getPixelAt(pic,2,1), makeColor(6,2,3))  # r+g+b = 11
  setColor(getPixelAt(pic,0,2), makeColor(7,2,3))  # r+g+b = 12
  setColor(getPixelAt(pic,1,2), makeColor(8,2,3))  # r+g+b = 13
  setColor(getPixelAt(pic,2,2), makeColor(9,2,3))  # r+g+b = 14
  
  return pic
