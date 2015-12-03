import time



#This is the stored pictures, calling "global" so the entire program can use them.
setMediaPath("F:\COMP 120 Tinkering Graphics-JH182233\Pictures") 
picfour = makePicture("Tree-Four-Seasons.jpg") 
picwinter = makePicture("Tree-Winter.jpg") 
picspring = makePicture("Tree-Spring.jpg") 
picsummer = makePicture("Tree-Summer.jpg")
picautumn = makePicture("Tree-Autumn.jpg")  
picM = makeEmptyPicture(513, 556, black)
pic = makeEmptyPicture(1025, 1110, black)


#The main function for the program
def main():
#create an empty picture and populate it with others 
    startX = 0
    startY = 0 
    repaint (pic)
    time.sleep(1)  
    copyInto(picspring, pic, startX, startY)
    repaint (pic)
    
    startX = 512
    startY = 0    
    time.sleep(1) 
    copyInto(picsummer, pic, startX, startY)
    repaint (pic)
    
    startX = 0
    startY = 554  
    time.sleep(1)  
    copyInto(picautumn, pic, startX, startY)
    repaint (pic)
    
    startX = 512
    startY = 554  
    time.sleep(1)  
    copyInto(picwinter, pic, startX, startY)
    repaint (pic)
    request()
    
    
    
#Now the program will ask for a season that you would like to view
def request():
    startX = 230
    startY = 300   
    season = requestString("What season would you like to activate?")
    if String(season) =="Winter":
       blackoutleft()
       copyInto(picwinter, pic, startX, startY)
       repaint(pic)
       time.sleep(2)
       request2()
    elif String(season) =="Spring":
       blackoutleft()  
       copyInto(picspring, pic, startX, startY)
       repaint(pic)
       time.sleep(2)
       request2()
    elif String(season) =="Summer":
       blackoutleft()   
       copyInto(picsummer, pic, startX, startY)
       repaint(pic)
       time.sleep(2)
       request2()
    elif String(season) =="Autumn":
       blackoutleft()   
       copyInto(picautumm, pic, startX, startY)
       repaint(pic)
       time.sleep(2)
       request2()
    else:
       blackouttop()
       request2()
       time.sleep(2)
     
    

#another request, a simple Y/N question to see if you want to continue, it will either end for "N" or continue if "Y"    
def request2():
    endSeason = requestString("Would you like to view more Y/N?")
    if String(endSeason) == "Y":
       copyInto(picfour, pic, 0, 0)
       repaint(pic)
       playWinter()
    elif String(endSeason) == "N":
       blackouttop()
       copyInto(picfour, pic, 0, 0)
       repaint(pic)
       showInformation("Thank you for using BioSeasons")
       blackouttop()
    else:       
       request2()
     
     

#Thie function will play through the seasons while calling on the merge function to produce a better flow.
def playWinter():
    startX = 230
    startY = 300
    blackoutleft()
    copyInto(picwinter, pic, startX, startY)
    repaint(pic)
    source1 = picwinter
    source2 = picspring
    merge(source1, source2, picM)
    time.sleep(2)
    copyInto(picspring, pic, startX, startY)
    repaint(pic)
    time.sleep(2)
    playSpring()
    playSummer()
    playAutumn()
    request2()  
    
    
    
def playSpring():
    startX = 230
    startY = 300
    source1 = picspring
    source2 = picsummer      
    merge(source1, source2, picM)
    time.sleep(2)
    copyInto(picsummer, pic, startX, startY)
    repaint(pic)
    time.sleep(2)
    
    
    
def playSummer():
    startX = 230
    startY = 300
    source1 = picsummer
    source2 = picautumm
    merge(source1, source2, picM)
    time.sleep(2)
    copyInto(picautumm, pic, startX, startY)
    repaint(pic)
    time.sleep(2)

    
    
def playAutumn():
    startX = 230
    startY = 300
    source1 = picautumm
    source2 = picwinter     
    merge(source1, source2, picM) 
    time.sleep(2)
    copyInto(picwinter, pic, startX, startY)
    repaint(pic)
    time.sleep(2)

     
   
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
  startX = 230
  startY = 300
  
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
  copyInto(picM, pic, startX, startY)
  repaint(pic)      