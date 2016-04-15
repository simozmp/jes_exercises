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
  # @return: Picture; Picture containing the first picture on the left
  #                   and the second picture on the right
  #                   (it'll have the height of the first picture)
  
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
  # @return: Picture; Picture containing the first picture on top
  #                   and the second picture on bottom
  #                   (it'll have the width of the first picture)
  
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

# The following function is meant to measure the average distance between two fragments/sectors

def averageDistance(sec1, sec2, size, direction) :
  # @param sec1: Picture;
  # @param sec2: Picture;
  # @param size: int;
  # @param direction: String;   This parameter indicates in wich position compare
  #                             the sectors (sector2 is "direction" to sector1)
  #                             Domain = {"up","right","down","left"}
  # @return: float; The average distance
  
  if (type(sec1) is Picture) and (type(sec2) is Picture) :    # Control on input type
    
    distancesSum = 0                          # It'll keep the sum of the distances
    
    height2 = getHeight(sec2)                 # The height of the second sector
    width2 = getWidth(sec2)                 # The width of the second sector
    
    for x in range(getWidth(sec1)) :        
    
      if direction == "up" :                        # Choose the pixels to compare on the base of direction..
        pix1 = getPixelAt(sec1,x,0)                 # ..
        pix2 = getPixelAt(sec2,x,height2-1)         # ..
      elif direction == "right" :                   # ..
        pix1 = getPixelAt(sec1,size-1,x)            # ..
        pix2 = getPixelAt(sec2,0,x)                 # ..
      elif direction == "down" :                    # ..
        pix1 = getPixelAt(sec1,x,height2-1)         # ..
        pix2 = getPixelAt(sec2,x,0)                 # ..
      elif direction == "left" :                    # ..
        pix1 = getPixelAt(sec1,0,x)                 # ..
        pix2 = getPixelAt(sec2,size-1,x)            # ..
      
      distancesSum = distancesSum + distance(getColor(pix1), getColor(pix2))    # Sums up the distance in total
    
    return distancesSum/x
  
  else :
    return None                                     # In case of wrong input type, None is returned 

def getBestNeighbor(list, index, size, direction) :
  # @param list: Picture[]; Fragments list
  # @param index: int; The index of the fragment to analyze
  # @param size: int; The size of the fragment
  # @param direction: String; It indicates in which direction we want to get the
  #                           best neighbor (with minor distance in that direction)
  #                           (list[result] is "direction" to list[index])
  #                           Domain = {"up","right","down","left"}
  # @return: (int, int); A tuple that contains:
  #                      (0) - The index in the list of the best neighbor
  #                      (1) - The distance between the fragment analyzed and its best neighbor
  
  distancesList = []                    # This list will be filled with the distance between
                                    # the analyzed sector and each other sector
  for sector in range(len(list)) :     # for each sector in the list..
    if sector == index :
      tempDist = 500.0              # (set the distance between the [index] sector and himself to 500.0)
    elif direction == "up" or direction == "right" or direction == "down" or direction == "left" :
      tempDist = averageDistance(list[index], list[sector], size, direction)    # ..get the distance between the [index] and the [sector]..
    else :
      return None                   # (in case of wrong input return None)
    distancesList.append(tempDist)  # ..and put it in the distancesList
  
  min = 500.0                       # this will keep track of the minium distance
  bestCandidate = -1                # this will keep track of the position of the best candidate to best neighbor
  
  for i in range(len(list)) :
    if distancesList[i] < min :
      bestCandidate = i
      min = distancesList[i]
  
  return (bestCandidate, int(min))

def recognizeRow(sectorsList, start, size, flagList) :
  # @param sectorsList: Picture[]; Fragments list
  # @param start: int; The index of the fragment to start the analysis
  # @param size: int; The size of the fragment
  # @param flagList: boolean[]; A list that indicates which sectors to analyze (and not already analysed)
  # @return int[]; A list that contain the index of the fragments that forms the
  #                recognised row (the one wich contains the sectorsList[start] fragment)
  
  row = [start]            # The recognized row (for the moment it contains just 
                           # the index of the fragment to start the analysis)
  topThreshold = 100       # Maximum distance allowed to consider a sector as neighbor
  bottomThreshold = 4      # Minimun distance allowed to consider a sector as neighbor (added in order to
                           # avoid plain colour borders to be considered neighbor)
  
  index = start            # Pointer set as start
  
  rightNeighbor = getBestNeighbor(sectorsList, index, size, "right")    # Get the best right neighbor
  leftNeighbor = getBestNeighbor(sectorsList, index, size, "left")      # Get the best left neighbor
  flagList[index] = false      # Set the sector as visited
  
  while rightNeighbor[1] < topThreshold and true in flagList and rightNeighbor[1] > bottomThreshold :   # If these conditions are not verified,
                                                                                                        # we have no other neighbors to the right
    row.append(rightNeighbor[0])              # Append the best right neighbor's index to the row
    index = rightNeighbor[0]                  # Move the pointer to this neighbor to continue the searching of right neighbors
    rightNeighbor = getBestNeighbor(sectorsList, index, size, "right")   # Search for another best neighbor
    flagList[index] = false                   # Set the sector as visited
  
  sector = start
  
  while leftNeighbor[1] < topThreshold and true in flagList and leftNeighbor[1] > bottomThreshold :     # If these conditions are not verified,
                                                                                                        # we have no other neighbors to the left
    row.insert(0,leftNeighbor[0])             # Insert the best left neighbor's index to the row
    index = leftNeighbor[0]                   # Move the pointer to this neighbor to continue the searching of left neighbors
    leftNeighbor = getBestNeighbor(sectorsList, index, size, "left")   # Search for another best neighbor
    flagList[index] = false                   # Set the sector as visited
  
  return row

def recognizeColumn(sectorsList, start, size, flagList) :
  # @param sectorsList: Picture[]; Fragments list
  # @param start: int; The index of the fragment to start the analysis
  # @param size: int; The size of the fragment
  # @param flagList: boolean[]; A list that indicates which sectors to analyze (and not already analysed)
  # @return int[]; A list that contain the index of the fragments that forms the
  #                recognised column (the one wich contains the sectorsList[start] fragment)
  
  column = [start]         # The recognized column (for the moment it contains just 
                           # the index of the fragment to start the analysis)
  topThreshold = 100       # Maximum distance allowed to consider a sector as neighbor
  bottomThreshold = 4      # Minimun distance allowed to consider a sector as neighbor (added in order to
                           # avoid plain colour borders to be considered neighbor)
  
  index = start            # Pointer set as start
  
  topNeighbor = getBestNeighbor(sectorsList, index, size, "up")        # Get the best top neighbor
  bottomNeighbor = getBestNeighbor(sectorsList, index, size, "down")   # Get the best bottom neighbor
  flagList[index] = false                   # Set the sector as visited
  
  while topNeighbor[1] < topThreshold and true in flagList and topNeighbor[1] > bottomThreshold :       # If these conditions are not verified,
                                                                                                        # we have no other neighbors to the top
    column.insert(0,topNeighbor[0])           # Insert the best top neighbor's index to the row
    index = topNeighbor[0]                    # Move the pointer to this neighbor to continue the searching of top neighbors
    topNeighbor = getBestNeighbor(sectorsList, index, size, "up")   # Search for another best neighbor
    flagList[index] = false                   # Set the sector as visited
  
  index = start            # Pointer set as start
  
  while bottomNeighbor[1] < topThreshold and true in flagList and bottomNeighbor[1] > bottomThreshold : # If these conditions are not verified,
                                                                                                        # we have no other neighbors to the bottom
    column.append(bottomNeighbor[0])          # Append the best bottom neighbor's index to the row
    index = bottomNeighbor[0]                 # Move the pointer to this neighbor to continue the searching of bottom neighbors
    bottomNeighbor = getBestNeighbor(sectorsList, index, size, "down")   # Search for another best neighbor
    flagList[index] = false                   # Set the sector as visited
  
  return column

# Main function

def automaticPictureRearrangement(pic, sectors) :
  # @param pic: Picture;  Input picture
  # @param sectors: int;  Total number of sectors/fragments, it has to be a positive squared number ( 4,6,9,16,25.. )
  # @return: Picture; Rearranged picture
  
  print "fragmentation.."
  sectorsList = fragmentation(pic,sectors)    # Converts the input picture in a list that contains each sector (as a Picture object)
  print "..done!"
  
  sectorSize = getHeight(sectorsList[0])      # The size of each sector
  
  # BUILD FLAGLISTS (lists of sqrt(sectors) trues, their role is
  # described in recognizeRow() and recognizeColumn() first comments)
  
  sectorsFlags = [] 
  stripesFlags = [] 
  
  for i in sectorsList :
    sectorsFlags.append(true)
  
  for i in range(sqrt(sectors)) :
    stripesFlags.append(true)
  
  # RECOGNIZE ROWS
  
  print "Recognizing rows.."
  rows = []                          # A list that will contain lists of indexes (each list will be a row)
  i=0                                # Pointer set as start
  
  while true in sectorsFlags :       # While there will be no unvisited fragments
    
    while sectorsFlags[i] == false : # While the pointed fragment is visited..
      i = i+1                        # ..pass to the next
    
    rows.append(recognizeRow(sectorsList, i, sectorSize, sectorsFlags))  # Recognize the row of the sector[i], than append it to the list
  
  print "..done! these are the recognized rows:"
  print rows
  
  # RECOGNIZE ROWS ORDER
  
  print "recognizing rows order.."
  
  firstColumn = []                   # This list will contain each sector that form the first column (its lenght will be sqrt(sectors))
  for i in range(sqrt(sectors)) :
    firstColumn.append(sectorsList[rows[i][0]])
  
  columns = recognizeColumn(firstColumn, 0, sectorSize, stripesFlags)    # Get the order of this first column, it will be
                                                                         # the order of the rows just detected  
  print "..done!"
  print columns
  
  # BUILD THE CALCULATED CORRECT ORDER
  
  print "Building correct order.."
  
  finalOrder = []                    # List of the correct order
  for i in range(len(rows)) :        # for each row..
    
    j = columns[i]                   # ..get the row index in order
    
    for k in range(len(rows[j])) :   # for each element of the row..
      finalOrder.append(rows[j][k])  # ..append it to final order
  
  print "..done! the caculated correct order is:"
  print finalOrder
  
  # Sort the sectorsList
  
  print "rearranging the sectors.."
  
  orderedList = []
  for i in range(sectors) :
    j=0                                 # ..
    while finalOrder[i] != j :               # ..
      j=j+1                             # .. get to the index of i
    orderedList.append(sectorsList[j])  # Fill the ordered list
  
  print "..done!"
  
  # Defragmentation
  
  print "defragmentation.."
  pic = defragmentation(orderedList)    # Convert the ordered list in the correct Picture
  print "..done!"
  
  # END
  
  return pic











