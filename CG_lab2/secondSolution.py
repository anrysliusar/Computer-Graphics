from tkinter import *
import math

hexagon = [[150, 500],
           [100, 475],
           [100, 425],
           [150, 400],
           [200, 425],
           [200, 475]]

numStepsOfMoving = 10
movingMatrix = [25, -25]

scalingMatrix = [[1.25, 0],
           [0, 1.25]]

numOfAngle = 0.3
rotationMatrix = [[math.cos(numOfAngle), math.sin(numOfAngle)],
                  [-math.sin(numOfAngle), math.cos(numOfAngle)]]


def drawHexagon(colour = "blue"):
    c.create_polygon((hexagon), fill=colour, outline=colour)


def operationMoving(hexagon, specialMatrix):
    for i in range(len(hexagon)):
        for j in range(len(hexagon[i])):
            hexagon[i][j] += specialMatrix[j]


def operationRotation(hexagon, specialMatrix):
    for i in range(len(hexagon)):
        x = hexagon[i][0]
        y = hexagon[i][1]
        hexagon[i][0] = x * specialMatrix[0][0] + y * specialMatrix[0][1]
        hexagon[i][1] = x * specialMatrix[1][0] + y * specialMatrix[1][1]


def operationScaling(hexagon, specialMatrix):
    for i in range(len(hexagon)):
        hexagon[i][0] *= specialMatrix[0][0]
        hexagon[i][1] *= specialMatrix[1][1]


root = Tk()
c = Canvas(root, width=800, height=550, bg="white")
drawHexagon()

for i in range(numStepsOfMoving):
    operationMoving(hexagon, movingMatrix)
drawHexagon("red")
operationRotation(hexagon, rotationMatrix)
drawHexagon("green")
operationScaling(hexagon, scalingMatrix)
drawHexagon("yellow")
print(9125 % 9)

c.pack()
root.mainloop()
