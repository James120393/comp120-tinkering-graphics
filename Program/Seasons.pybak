import time


#This is the stored pictures, calling "global" so the entire program can use them.
setMediaPath(r"C:\Users\James\Documents\Uni\comp120-tinkering-graphics\Pictures") 
pic_seasons = makePicture("Tree-Four-Seasons.jpg") 
pic_winter = makePicture("Tree-Winter.jpg") 
pic_spring = makePicture("Tree-Spring.jpg") 
pic_summer = makePicture("Tree-Summer.jpg")
pic_autumn = makePicture("Tree-Autumn.jpg")  
pic_merge = makeEmptyPicture(513, 556, black)
pic_main = makeEmptyPicture(1025, 1110, black)



def copy():
#create an empty picture and populate it with others
#A new X,Y needs to be stated before each picture is copied into the canvas to ensure that thery appear with the correct POS. 
    startX = 0
    startY = 0 
    repaint (pic_main)
#time.sleep() is used so you have a chance to view the pictures
    time.sleep(1)  
    copyInto(pic_spring, pic_main, startX, startY)
    repaint (pic_main)
    
    startX = 512
    startY = 0    
    time.sleep(1) 
    copyInto(pic_summer, pic_main, startX, startY)
    repaint (pic_main)
    
    startX = 0
    startY = 554  
    time.sleep(1)  
    copyInto(pic_autumn, pic_main, startX, startY)
    repaint (pic_main)
    
    startX = 512
    startY = 554  
    time.sleep(1)  
    copyInto(pic_winter, pic_main, startX, startY)
    repaint (pic_main)
    
    
    
#Now the program will ask for a season that you would like to view, you must choose which one.
def request():
    startX = 230
    startY = 300   
    season = requestString("What season would you like to activate? Winter, Spring, Summer or Autumn")
    if str(season) =="Winter":
       blackoutleft()
       copyInto(pic_winter, pic_main, startX, startY)
       repaint(pic_main)
       time.sleep(2)
    elif String(season) =="Spring":
       blackoutleft()  
       copyInto(pic_spring, pic_main, startX, startY)
       repaint(pic_main)
       time.sleep(2)
    elif String(season) =="Summer":
       blackoutleft()   
       copyInto(pic_summer, pic_main, startX, startY)
       repaint(pic_main)
       time.sleep(2)
    elif String(season) =="Autumn":
       blackoutleft()   
       copyInto(pic_autumm, pic_main, startX, startY)
       repaint(pic_main)
       time.sleep(2)
    else:
       time.sleep(2)    
     
    

#another request, a simple Y/N question to see if you want to continue, it will either end for "N" or continue if "Y"    
def nextRequest():
    endSeason = requestString("Would you like to view more Y/N?")
    if String(endSeason) == "Y":
       copyInto(pic_seasons, pic_main, 0, 0)
       repaint(pic_main)
       beginWinter()
    elif String(endSeason) == "N":
       blackouttop()
       copyInto(pic_seasons, pic, 0, 0)
       repaint(pic_main)
       showInformation("Thank you for using BioSeasons")
       blackouttop()
    else:       
       nextRequest()
     
     

#Thie function will play through the seasons while calling on the merge function to produce a better flow.
def beginWinter():
    startX = 230
    startY = 300
    blackoutleft()
    copyInto(pic_winter, pic_main, startX, startY)
    repaint(pic_main)
    source_1 = pic_winter
    source_2 = pic_spring
    merge(source_1, source_2, pic_merge)
    time.sleep(2)
    copyInto(pic_spring, pic_main, startX, startY)
    repaint(pic_main)
    time.sleep(2)
    playNextSeason(pic_spring, pic_summer)
    playNextSeason(pic_summer, pic_autumn)
    playNextSeason(pic_autumn, pic_winter)
    nextRequest()  
    
    
#This will use the merge function and copy the new picture into the old canvas, without opening a new window.
def playNextSeason(source_1, source_2):
    startX = 230
    startY = 300
    merge(source_1, source_2, pic_merge)
    time.sleep(2)
    copyInto(source_2, pic_main, startX, startY)
    repaint(pic_main)
    time.sleep(2)
    
         
   
#Slowly blacken out the image from the top to bottom
def blackouttop():
  startX = 0
  startY = 0
  w = getWidth(pic_main)
  h = getHeight(pic_main)
  
  for y in range(0,h):
     for x in range(0,w):
        px = getPixel(pic_main, x, y)
        setColor(px,black)
     repaint (pic_main)
     
     

#Blackens out the image from left to right
def blackoutleft():
  startX = 0
  startY = 0
  w = getWidth(pic_main)-1
  h = getHeight(pic_main)-1
  
  skip = 4
  for x in range(0, w, skip):
      for i in range(0, skip):
          for y in range(0, h):
            if x + i < h:
              px = getPixel(pic_main, x + i, y)
              setColor(px,black)
          repaint (pic_main)
   
   

#here the merge functions gets its sources from the selection made in the request function, e.g. if Winter was choosen the source1 = Winter and source2 = Spring.
#This is also a modified version of the Blending Pictures algorithm in the Intro to Python Book. by Mark J. Guzdial pages:184-186   
def merge(source_1, source_2, pic_merge):
  startX = 230
  startY = 300
  
  maxHeight = getHeight(source_1)
  if getHeight(source_2) > maxHeight:
      maxHeight = getHeight(source_2)
  
  maxWidth = getWidth(source_1)
  if getWidth(source_2) > maxWidth:
      maxWidth = getWidth(source_2)

  sourceX = 0  
  for targetX in range(0, maxWidth - 1):
     sourceY = 0
     for targetY in range(0, maxHeight - 1):
        onePixel = getPixel(source_1, sourceX, sourceY)
        twoPixel = getPixel(source_2, sourceX, sourceY)
        newRed = 0.50 * getRed(onePixel) + 0.50 * getRed(twoPixel)
        newGreen = 0.50 * getGreen(onePixel) + 0.50 * getGreen(twoPixel)
        newBlue = 0.50 * getBlue(onePixel) + 0.50 * getBlue(twoPixel)
        color = makeColor(newRed, newGreen, newBlue)
        setColor(getPixel(pic_merge, targetX, targetY), color)
        sourceY = sourceY +1
     sourceX = sourceX +1
  copyInto(pic_merge, pic_main, startX, startY)
  repaint(pic_main)      
  
  
  
#The main function for the program
def main():
    copy()
    request()
    nextRequest()
      