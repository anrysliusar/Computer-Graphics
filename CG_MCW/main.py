from tkinter import *
import math

rectangle = [[100, 600, 1],
             [300, 600, 1],
             [300, 700, 1],
             [100, 700, 1]]

numOfAngle = 0.3

rotationMatrix = [[math.cos(numOfAngle), (math.sin(numOfAngle)), 0],
                  [-math.sin(numOfAngle), math.cos(numOfAngle), 0],
                  [0, 0, 1]]

rotationAndMovingMatrix = [
    [math.cos(numOfAngle), (math.sin(numOfAngle)), 10],
    [-math.sin(numOfAngle), math.cos(numOfAngle), -10],
    [0, 0, 1]]


def drawRectangle(colour="blue", colourOut="blue"):
    matrixForPolygon = [[rectangle[0][0] / rectangle[0][2], rectangle[0][1] / rectangle[0][2]],
                         [rectangle[1][0] / rectangle[1][2], rectangle[1][1] / rectangle[1][2]],
                         [rectangle[2][0] / rectangle[2][2], rectangle[2][1] / rectangle[2][2]],
                         [rectangle[3][0] / rectangle[3][2], rectangle[3][1] / rectangle[3][2]]]
    c.create_polygon(matrixForPolygon, fill=colour, outline=colourOut)


def operation(rectangle, specialMatrix):
    for i in range(len(rectangle)):
        for j in range(len(specialMatrix)):
            x = rectangle[i][0] * specialMatrix[j][0]
            x1 = rectangle[i][1] * specialMatrix[j][1]
            x2 = rectangle[i][2] * specialMatrix[j][2]
            rectangle[i][j] = x + x1 + x2


root = Tk()
c = Canvas(root, width=900, height=800, bg="white")

drawRectangle()
drawRectangle("red", "red")

operation(rectangle, rotationMatrix)
drawRectangle("green", "green")

for i in range(2):
    operation(rectangle, rotationAndMovingMatrix)
    drawRectangle("yellow")

c.pack()
root.mainloop()
