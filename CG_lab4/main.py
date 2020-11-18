import math
import time
from copy import deepcopy
import random
from tkinter import messagebox
import Graphics as g

listBuildingObj = []
listOfLines = []
width = 300
length = 200
height = 250
retreatFromTheLeftAndTop = 350
angle = 0.2


def rotation(angle, x, y, z):
    listX = [x, y * math.cos(angle) - z * math.sin(angle), y * math.sin(angle) + z * math.cos(angle)]
    listY = [x * math.cos(angle) + z * math.sin(angle), y, -x * math.sin(angle) + z * math.cos(angle)]
    listZ = [x * math.cos(angle) - y * math.sin(angle), x * math.sin(angle) + y * math.cos(angle), z]
    return [listX, listY, listZ]


def createListPointOfParallelepiped():
    A = [width / 2, length / 2, -height / 2]
    B = [-width / 2, length / 2, -height / 2]
    C = [-width / 2, -length / 2, -height / 2]
    D = [width / 2, -length / 2, -height / 2]
    A1 = [width / 2, length / 2, height / 2]
    B1 = [-width / 2, length / 2, height / 2]
    C1 = [-width / 2, -length / 2, height / 2]
    D1 = [width / 2, -length / 2, height / 2]
    listOfPoints = [A, B, C, D, A1, B1, C1, D1]
    return listOfPoints


def program():
    points = createListPointOfParallelepiped()

    def createListWithLinesOfParallelepiped(points):
        copyPoints = deepcopy(points)
        for point in copyPoints:
            for i in range(len(point)):
                point[i] += retreatFromTheLeftAndTop
        points = copyPoints
        A = points[0]
        B = points[1]
        C = points[2]
        D = points[3]
        A1 = points[4]
        B1 = points[5]
        C1 = points[6]
        D1 = points[7]
        return [[A1, A], [A, B], [A, D], [B, B1], [C, B], [C1, C], [C, D], [D, D1], [D1, C1], [D1, A1], [A1, B1],
                [B1, C1]]

    # алгоритм Брезенхема для растрифікації ліній
    def draw_line_pixel(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy
        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy
        x, y = x1, y1
        error, t = el / 2, 0

        obj = g.Point(x, y)
        listBuildingObj.append(obj)

        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            obj = g.Point(x, y)
            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            colour = g.color_rgb(red, green, blue)
            obj.setFill('' + colour)
            listBuildingObj.append(obj)

    def buildObj():
        for line in listOfLines:
            draw_line_pixel(line[0][0], line[0][1], line[1][0], line[1][1])

    def showObj():
        buildObj()
        for obj in listBuildingObj:
            obj.draw(window)

    def hideObj():
        for obj in listBuildingObj:
            obj.undraw()

    listOfLines = createListWithLinesOfParallelepiped(points)
    showObj()
    time.sleep(1)
    hideObj()
    time.sleep(1)
    num = 0
    while True:
        hideObj()
        for i in range(len(points)):
            for j in range(3):
                tempRotation = rotation(angle, points[i][0], points[i][1], points[i][2])
                points[i] = tempRotation[j]
        listBuildingObj.clear()
        listOfLines = createListWithLinesOfParallelepiped(points)

        showObj()
        time.sleep(0.3)
        num += 1
        if num == 4:
            num = 0
            result = messagebox.askquestion('Attention', 'Завершити огляд фігури?')
            if result == 'yes':
                break
            else:
                continue



if __name__ == '__main__':
    window = g.GraphWin("Lab4", 700, 700)
    window.setBackground('black')
    program()
    window.close()
