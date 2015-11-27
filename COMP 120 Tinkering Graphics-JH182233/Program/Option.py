import time



#This is the stored pictures, calling "global" so the entire program can use them.
setMediaPath("F:\COMP 120 Tinkering Graphics-JH182233\Pictures")
global picture1 
picture1 = makePicture("Tree-Four-Seasons.jpg")
global picture2 
picture2 = makePicture("Tree-Winter.jpg")
global picture3 
picture3 = makePicture("Tree-Spring.jpg")
global picture4 
picture4 = makePicture("Tree-Summer.jpg")
global picture5 
picture5 = makePicture("Tree-Autumn.jpg")  
global picture6
picture6 = makePicture("tree.jpg")
global picture7
picture7 = makePicture("test.jpg")
global picM
picM = makeEmptyPicture(513, 556, black)



#The main function for the program
def main():
#create an empty picture and populate it with others 
    startX = 0
    startY = 0
    global pic
    pic = makeEmptyPicture(1025, 1110, black) 
    repaint (pic)
    time.sleep(1)  
    copyInto(picture2, pic, startX, startY)
    repaint (pic)
    
    startX = 512
    startY = 0    
    time.sleep(1) 
    copyInto(picture3, pic, startX, startY)
    repaint (pic)
    
    startX = 0
    startY = 554  
    time.sleep(1)  
    copyInto(picture4, pic, startX, startY)
    repaint (pic)
    
    startX = 512
    startY = 554  
    time.sleep(1)  
    copyInto(picture5, pic, startX, startY)
    repaint (pic)
    request()
    
    
    
#Now the program will ask for a season that you would like to view
def request():
    startX = 230
    startY = 300   
    season = requestString("What season would you like to activate?")
    if String(season) =="Winter":
     blackoutleft()
     copyInto(picture2, pic, startX, startY)
     repaint(pic)
     time.sleep(2)
     request2()
    elif String(season) =="Spring":
     blackoutleft()  
     copyInto(picture3, pic, startX, startY)
     repaint(pic)
     time.sleep(2)
     request2()
    elif String(season) =="Summer":
     blackoutleft()   
     copyInto(picture4, pic, startX, startY)
     repaint(pic)
     time.sleep(2)
     request2()
    elif String(season) =="Autumn":
     blackoutleft()   
     copyInto(picture5, pic, startX, startY)
     repaint(pic)
     time.sleep(2)
     request2()
    else:
     blackout()
     fourseasons()
     time.sleep(2)
     
    

#another request, a simple Y/N question to see if you want to continue, it will either end for "N" or continue if "Y"    
def request2():
    endSeason = requestString("Would you like to view more Y/N?")
    if String(endSeason) == "Y":
     copyInto(picture1, pic, 0, 0)
     repaint(pic)
     playseason()
    elif String(endSeason) == "N":
     blackouttop()
     copyInto(picture1, pic, 0, 0)
     repaint(pic)
     showInformation("Thank you for using BioSeasons")
     blackouttop()
    else:       
     request()
     
     

#Thie function will play through the seasons while calling on the merge function to produce a better flow.
def playseason():
    startX = 230
    startY = 300
    blackoutleft()
    copyInto(picture2, pic, startX, startY)
    repaint(pic)
    source1 = picture2
    source2 = picture3
    merge(source1, source2, picM)
    copyInto(picM, pic, startX, startY)
    time.sleep(2)
    copyInto(picture3, pic, startX, startY)
    time.sleep(2)
    source1 = picture3
    source2 = picture4      
    merge(source1, source2, picM)
    copyInto(picM, pic, startX, startY) 
    time.sleep(2)
    copyInto(picture4, pic, startX, startY)
    repaint(pic)
    source1 = picture4
    source2 = picture5
    merge(source1, source2, picM)
    copyInto(picM, pic, startX, startY)
    time.sleep(2)
    copyInto(picture5, pic, startX, startY)
    time.sleep(2)
    source1 = picture5
    source2 = picture2      
    merge(source1, source2, picM) 
    copyInto(picM, pic, startX, startY)
    time.sleep(2)
    request2()    

     
   
#Slowly blacken out the image from the top to bottom
def blackouttop():
  startX = 0
  startY = 0
  w = getWidth(pic)
  h = getHeight(pic)
  
  for y in range(0,h):
   for x in range(0,w):
    px = getPixel(pic, x, y)
    setColor(px,black)
   repaint (pic)

#Blackens out the image from left to right
def blackoutleft():
  startX = 0
  startY = 0
  w = getWidth(pic)-1
  h = getHeight(pic)-1
  
  skip = 4
  for x in range(0, w, skip):
    for i in range(0, skip):
      for y in range(0, h):
        if x + i < h:
          px = getPixel(pic, x + i, y)
          setColor(px,black)
    repaint (pic)
   
   

#here the merge functions gets its sources from the selection made in the request function, e.g. if Winter was choosen the source1 = Winter and source2 = Spring.
#This is also a modified version of the Blending Pictures algorithm in the Intro to Python Book. by Mark J. Guzdial pages:184-186   
def merge(source1, source2, picM):
  
  maxHeight = getHeight(source1)
  if getHeight(source2) > maxHeight:
    maxHeight = getHeight(source2)
  
  maxWidth = getWidth(source1)
  if getWidth(source2) > maxWidth:
    maxWidth = getWidth(source2)

  sourceX = 0  
  for targetX in range(0, maxWidth - 1):
   sourceY = 0
   for targetY in range(0, maxHeight - 1):
    onePixel = getPixel(source1, sourceX, sourceY)
    twoPixel = getPixel(source2, sourceX, sourceY)
    newRed = 0.50 * getRed(onePixel) + 0.50 * getRed(twoPixel)
    newGreen = 0.50 * getGreen(onePixel) + 0.50 * getGreen(twoPixel)
    newBlue = 0.50 * getBlue(onePixel) + 0.50 * getBlue(twoPixel)
    color = makeColor(newRed, newGreen, newBlue)
    setColor(getPixel(picM, targetX, targetY), color)
    sourceY = sourceY +1
   sourceX = sourceX +1