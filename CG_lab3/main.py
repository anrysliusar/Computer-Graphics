import Graphics as g
import time
import math
from tkinter import messagebox

width = 300
length = 200
height = 250

retreatFromTheLeft = 300
retreatFromTheTop = 300
angle = 0.015


def rotation(angle, x, y, z):
    listX = [x, y * math.cos(angle) - z * math.sin(angle), y * math.sin(angle) + z * math.cos(angle)]
    listY = [x * math.cos(angle) + z * math.sin(angle), y, -x * math.sin(angle) + z * math.cos(angle)]
    listZ = [x * math.cos(angle) - y * math.sin(angle), x * math.sin(angle) + y * math.cos(angle), z]
    return [listX, listY, listZ]


def createListPointOfParallelepiped():
    A = (width / 2, length / 2, -height / 2)
    B = (-width / 2, length / 2, -height / 2)
    C = (-width / 2, -length / 2, -height / 2)
    D = (width / 2, -length / 2, -height / 2)
    A1 = (width / 2, length / 2, height / 2)
    B1 = (-width / 2, length / 2, height / 2)
    C1 = (-width / 2, -length / 2, height / 2)
    D1 = (width / 2, -length / 2, height / 2)
    listOfPoints = [A, B, C, D, A1, B1, C1, D1]
    return listOfPoints


def program(window):
    points = createListPointOfParallelepiped()

    def setListsPointsQuadrangle():
        return [[points[0], points[1], points[2], points[3]],  # [A, B, C, D]
                [points[0], points[4], points[5], points[1]],  # [A, A1, B1, B]
                [points[0], points[4], points[7], points[3]],  # [A, A1, D1, D]
                [points[1], points[5], points[6], points[2]],  # [B, B1, C1, C]
                [points[2], points[6], points[7], points[3]],  # [C, C1, D1, D]
                [points[4], points[5], points[6], points[7]]]  # [A1, B1, C1, D1]

    listBuildingObj = []

    def buildObj():

        for p in setListsPointsQuadrangle():
            p1 = p[0]
            p2 = p[1]
            p3 = p[2]
            p4 = p[3]
            listBuildingObj.append(g.Polygon(g.Point(p1[0] + retreatFromTheLeft, p1[1] + retreatFromTheTop),
                                             g.Point(p2[0] + retreatFromTheLeft, p2[1] + retreatFromTheTop),
                                             g.Point(p3[0] + retreatFromTheLeft, p3[1] + retreatFromTheTop),
                                             g.Point(p4[0] + retreatFromTheLeft, p4[1] + retreatFromTheTop)))

    def showObj(color='black'):
        buildObj()
        for obj in listBuildingObj:
            obj.draw(window)
            obj.setOutline(color)

    def hideObj():
        for obj in listBuildingObj:
            obj.undraw()

    buildObj()
    showObj()
    time.sleep(2)
    hideObj()
    time.sleep(0.5)

    showObj('red')
    time.sleep(2)
    hideObj()

    num = 0
    while True:
        hideObj()
        for i in range(len(points)):
            for j in range(3):
                tempRotation = rotation(angle, points[i][0], points[i][1], points[i][2])
                points[i] = tempRotation[j]

        listBuildingObj.clear()
        buildObj()
        showObj()
        #showObj('red')
        time.sleep(0.0001)

        num += 1
        if num == 400:
            num = 0
            result = messagebox.askquestion('Attention', 'Завершити обертання фігури?')
            if result == 'yes':
                break
            else:
                continue


if __name__ == '__main__':
    window = g.GraphWin("Lab 3", 600, 600)
    program(window)
    window.close()
