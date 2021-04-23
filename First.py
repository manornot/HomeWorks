import math

# this code draws half of the sine wave in terminal

# task - modufy this code to draw full sive wave

for i in range(0, int(math.pi*10+1)):
    numOfSpaces = 25+int(math.sin(i/10)*25)
    space = ' '
    strToPrint = space * numOfSpaces
    print(strToPrint, 'o')
