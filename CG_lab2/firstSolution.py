from tkinter import *
import math

hexagon = [[150, 500, 1],
           [100, 475, 1],
           [100, 425, 1],
           [150, 400, 1],
           [200, 425, 1],
           [200, 475, 1]]

numStepsOfMoving = 10

movingMatrix = [[1, 0, 25],
                [0, 1, -25],
                [0, 0, 1]]

scalingMatrix = [[1.25, 0, 0],
                 [0, 1.25, 0],
                 [0, 0, 1]]

numOfAngle = 0.3

rotationMatrix = [[math.cos(numOfAngle), (math.sin(numOfAngle)), 0],
                  [-math.sin(numOfAngle), math.cos(numOfAngle), 0],
                  [0, 0, 1]]


def drawHexagon(colour="blue"):
    mattrixForPolygon = [[hexagon[0][0] / hexagon[0][2], hexagon[0][1] / hexagon[0][2]],
                         [hexagon[1][0] / hexagon[1][2], hexagon[1][1] / hexagon[1][2]],
                         [hexagon[2][0] / hexagon[2][2], hexagon[2][1] / hexagon[2][2]],
                         [hexagon[3][0] / hexagon[3][2], hexagon[3][1] / hexagon[3][2]],
                         [hexagon[4][0] / hexagon[4][2], hexagon[4][1] / hexagon[4][2]],
                         [hexagon[5][0] / hexagon[5][2], hexagon[5][1] / hexagon[5][2]], ]
    c.create_polygon(mattrixForPolygon, fill=colour, outline=colour)


def operation(hexagon, specialMatrix):
    for i in range(len(hexagon)):
        for j in range(len(specialMatrix)):
            x = hexagon[i][0] * specialMatrix[j][0]
            x1 = hexagon[i][1] * specialMatrix[j][1]
            x2 = hexagon[i][2] * specialMatrix[j][2]
            hexagon[i][j] = x + x1 + x2



root = Tk()
c = Canvas(root, width=800, height=550, bg="white")
drawHexagon()

for i in range(numStepsOfMoving):
    operation(hexagon, movingMatrix)
drawHexagon("red")
operation(hexagon, rotationMatrix)
drawHexagon("green")
operation(hexagon, scalingMatrix)
drawHexagon("yellow")

c.pack()
root.mainloop()
