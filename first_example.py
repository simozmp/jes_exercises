def function(par1,par2):
  return log(par1) + sqrt( par2 - sin(par1) ) 
  
def pickAndPlay():
  myFile = pickAFile()
  mySound = makeSound(myFile)
  play(mySound)
  
def pickAndShow():
  myFile = pickAFile()
  myPicture = makePicture(myFile)
  show(myPicture)
  showVars()
  