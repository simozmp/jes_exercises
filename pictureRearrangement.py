def fragmentation(pic, sectors) :
  # @param pic: Picture;
  # @param sectors: int;
  # @return Picture[];    List of fragments/sectors, squared image portions
  
  sectorSize = int(getHeight(pic)/(sqrt(sectors)))    # Size of a single squared sector
  list = []                                           # list of fragments
  
  for sectorY in range(sqrt(sectors)) :                    # ..
    for sectorX in range(sqrt(sectors)) :                  # .. cycles to scan each sector in the picture
      
      tempPic = makeEmptyPicture(sectorSize,sectorSize)    # A temporary picture, it'll be the single sector
      
      for x in range(sectorSize) :                         # ..
        for y in range(sectorSize) :                       # .. cycles to scan the picture in the sector area
          pix1 = getPixelAt(tempPic,x,y)                                              # ..
          pix2 = getPixelAt(pic, (sectorSize*sectorX)+x, (sectorSize*sectorY)+y)      # ..
          setColor(pix1, getColor(pix2))                                              # .. copy of the pixel
      
      list.append(tempPic)                                 # append the sector to the list
  
  return list

def defragmentation(list) :
  # @param list: Picture[];  
  # @return Picture; The complete picture
  
  sectorsPerSide = int(sqrt(len(list)))     # Number of sectors on each side
  
  for y in range(sectorsPerSide) :          # Cycle for the rows' collage
    for x in range(sectorsPerSide) :        # Cycle to get a single row
      if x == 0 :                           # *
        stripe = list[y*sectorsPerSide]     # At the first run of the cycle, 'stripe' is set as the first sector of the row
      else :                                # *
        stripe = horizontalCollage(stripe, list[(y*sectorsPerSide)+x])    # append each sector to 'stripe'
    
    if y == 0 :                                   # *
      result = stripe                             # At the first run of the cycle, 'result' is set as the first stripe of the entire picture
    else :                                        # *
      result = verticalCollage(result, stripe)    # append each stripe to 'result'
  
  return result


def horizontalCollage(pic1, pic2) :
  # @param pic1: Picture; First picture (Left)
  # @param pic2: Picture; Second picture (Right)
  
  width1 = getWidth(pic1)
  height1 = getHeight(pic1)
  width2 = getWidth(pic2)
  height2 = getHeight(pic2)

  result = makeEmptyPicture(width1+width2,height1)
  
  # Copy of the first picture in the final
  for y in range(height1) :
    for x in range(width1) :
      setColor(getPixelAt(result,x,y),getColor(getPixelAt(pic1,x,y)))
  
  # Copy of the second picture in the final
  for y in range(height2) :
    for x in range(width2) :
      pix1 = getPixelAt(result,x+width1,y)
      pix2 = getPixelAt(pic2,x,y)
      setColor(pix1,getColor(pix2))
  
  return result

def verticalCollage(pic1, pic2) :
  # @param pic1: Picture; First picture (Top)
  # @param pic2: Picture; Second picture (Bottom)
  
  width1 = getWidth(pic1)
  height1 = getHeight(pic1)
  width2 = getWidth(pic2)
  height2 = getHeight(pic2)

  result = makeEmptyPicture(width1,height1+height2)
  
  # Copy of the first picture in the final
  for y in range(height1) :
    for x in range(width1) :
      setColor(getPixelAt(result,x,y),getColor(getPixelAt(pic1,x,y)))
  
  # Copy of the second picture in the final
  for y in range(height2) :
    for x in range(width2) :
      pix1 = getPixelAt(result,x,y+height1)
      pix2 = getPixelAt(pic2,x,y)
      setColor(pix1,getColor(pix2))
  
  return result

def pictureRearrangement(pic, sectors, order) :
  # @param pic: Picture;  The 'disordered' picture
  # @param sectors: int;  Number of total sectors/fragments in the picture
  # @param order: int[];  List of the correct order of the picture (len = sectors)
  
  print "fragmentation.."
  sectorsList = fragmentation(pic,sectors)
  print "..done!"
  
  print "rearranging the sectors.."
  
  orderedList = []
  for i in range(sectors) :
    j=0                                 # ..
    while order[i] != j :               # ..
      j=j+1                             # .. get to the index of i
    orderedList.append(sectorsList[j])  # Fill the ordered list
  
  print "..done!"
  
  print "defragmentation.."
  pic = defragmentation(orderedList)
  print "..done!"
  
  return pic











