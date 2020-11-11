from tkinter import *
import math

hexagon = [[150, 500],
           [100, 475],
           [100, 425],
           [150, 400],
           [200, 425],
           [200, 475]]

numStepsOfMoving = 10
lenOfStepOfMoving = 25
numOfAngle = 0.3
numOfScaling = 1.25


def drawHexagon(colour="blue"):
    c.create_polygon(hexagon, fill=colour, outline=colour)


def operationMoving(hexagon, lenOfStep):
    for i in range(len(hexagon)):
        hexagon[i][0] += lenOfStep
        hexagon[i][1] -= lenOfStep


def operationRotation(hexagon, numOfAngle):
    for i in range(len(hexagon)):
        x = hexagon[i][0]
        y = hexagon[i][1]

        hexagon[i][0] = x * math.cos(numOfAngle) + y * math.sin(numOfAngle)
        hexagon[i][1] = x * (-math.sin(numOfAngle)) + y * math.cos(numOfAngle)


def operationScaling(hexagon, numOfScaling):
    for i in range(len(hexagon)):
        hexagon[i][0] *= numOfScaling
        hexagon[i][1] *= numOfScaling


root = Tk()
c = Canvas(root, width=800, height=550, bg="white")
drawHexagon()

for i in range(numStepsOfMoving):
    operationMoving(hexagon, lenOfStepOfMoving)
drawHexagon("red")
operationRotation(hexagon, numOfAngle)
drawHexagon("green")
operationScaling(hexagon, numOfScaling)
drawHexagon("yellow")

c.pack()
root.mainloop()
