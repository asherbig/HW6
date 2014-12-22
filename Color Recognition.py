# Alexander Herbig, Conor Tanzman, Arshiya Singh
# Section B04
# We worked on this homework assignment alone, using this semester's course materials

from Myro import *
from random import *
#init("/dev/tty.Fluke2-02A9-Fluke2")
init()
setPicSize("small")
#setLED("left", 0)
#setLED("right", 0)


# This function takes a picture input and determines which color each pixel is.
# The conditional statements for finding colors are based on the pictures that our robot took, which were often dark.
# At the end, it totals how much of each color there is and chooses the most dominant color as the color of the picture.
def findColor(pic):
    green = 0
    yellow = 0
    red = 0
    white = 0
    other = 0
    pic2 = copyPicture(pic)
    # Trying to guess the contrast of the picture.
    # High number = high contrast 
    con = 30
    closeCon = 10
    # Sets the lower threshold for darkness
    # This prevents dark colors from being recognized as white
    dark = 20
    for p in getPixels(pic2):   
        r, g, b = getRGB(p)
        if b+con < r and g+con < r and b-g<closeCon:
            red += 1
            setRed(p,255)
            setGreen(p,0)
            setBlue(p,0)
        elif g > r and g>b:
            green += 1
            setBlue(p,0)
            setRed(p,0)
            setGreen(p,255)
        elif r>=g and r>(b+con) and g>(b+closeCon):
            yellow += 1
            setRed(p,255)
            setGreen(p,255)
            setBlue(p,0)
# The first two statements test to see if the difference between two colors is a small amount
# If the difference is less than a set value, then it will return true
# Also, if the colors are all brighter than a certain brightness, it will be true
# That stops black from being recognized as white
        elif g-b < con*3/4 and g-r < con*3/4 and b > dark and g > dark and r > dark:
            white += 1
            setBlue(p,255)
            setRed(p,255)
            setGreen(p,255)
        else:
            other += 1
            setBlue(p,0)
            setGreen(p,0)
            setRed(p,0)
    show(pic, "original")
    show(pic2, "edited")
    white = white/2
    if red > green and red > white and red > yellow:
        return "red"
    if green > red and green > white and green > yellow:
        return "green"
    if yellow > green and yellow > white and yellow > red:
        return "yellow"
    if white > yellow and white > green and white > red:
        return "white"
    else:
        return "None"

# This was used to make the robot randomly turn in a direction.
def turn():
    ranNum = randrange(2)
    if ranNum == 0:
        setLED("right", 1)
        turnBy(90,"deg")
        setLED("right", 0)
    else:
        setLED("left", 1)
        turnBy(-90,"deg")
        setLED("left", 0)

# This function is what ran and called the other functions.
# The robot takes pictures, and based on the color of the picture it took, it will do different movements.
def stopLight():
    while True:
        aPic = takePicture()
        color = findColor(aPic)
        print(color)
        if color == "green":
            forward(1,2)
        elif color == "yellow":
            forward(.5,2)
        elif color == "white":
            turn()
        elif color == "None":
            pass
        elif color == "red":
            stop()
            beep(1,800)
            return None

