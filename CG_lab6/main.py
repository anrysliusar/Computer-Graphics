import numpy as np
from graphics import *
import math as mh

retreatForParallelepiped = 400
retreatForSirpinsky = 100
retreatForMandel = 500

sizeMandel = 100

triSirpinsky = [[40 + retreatForSirpinsky, -90 + retreatForSirpinsky],
                [190 + retreatForSirpinsky, 180 + retreatForSirpinsky],
                [340 + retreatForSirpinsky, -90 + retreatForSirpinsky]]

listBuildingObj = []
listOfLines = []
width = 250
length = 150
height = 200

angle1 = 180
angle2 = -90
Tx = []
Ty = []
listPointOfParallelepiped = np.array([[width / 2 + retreatForParallelepiped, length / 2 + retreatForParallelepiped,
                                       -height / 2 + retreatForParallelepiped, 1],
                                      [-width / 2 + retreatForParallelepiped, length / 2 + retreatForParallelepiped,
                                       -height / 2 + retreatForParallelepiped, 1],
                                      [-width / 2 + retreatForParallelepiped, -length / 2 + retreatForParallelepiped,
                                       -height / 2 + retreatForParallelepiped, 1],
                                      [width / 2 + retreatForParallelepiped, -length / 2 + retreatForParallelepiped,
                                       -height / 2 + retreatForParallelepiped, 1],
                                      [width / 2 + retreatForParallelepiped, length / 2 + retreatForParallelepiped,
                                       height / 2 + retreatForParallelepiped, 1],
                                      [-width / 2 + retreatForParallelepiped, length / 2 + retreatForParallelepiped,
                                       height / 2 + retreatForParallelepiped, 1],
                                      [-width / 2 + retreatForParallelepiped, -length / 2 + retreatForParallelepiped,
                                       height / 2 + retreatForParallelepiped, 1],
                                      [width / 2 + retreatForParallelepiped, -length / 2 + retreatForParallelepiped,
                                       height / 2 + retreatForParallelepiped, 1]])


def multipr(listPointOfParallelepiped):
    f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    ft = f.T
    return listPointOfParallelepiped.dot(ft)


def shift(listPointOfParallelepiped, l):
    f = np.array([[1, 0, 0, l], [0, 1, 0, l], [0, 0, 1, l], [1, 0, 0, 1]])
    ft = f.T
    return listPointOfParallelepiped.dot(ft)


def multiplyL(listPointOfParallelepiped, TetaG):
    TetaR = (3 / 14 * TetaG) / 180
    f = np.array(
        [[1, 0, 0, 0], [0, mh.cos(TetaR), mh.sin(TetaR), 0], [0, -mh.sin(TetaR), mh.cos(TetaR), 0], [0, 0, 0, 1]])
    ft = f.T
    return listPointOfParallelepiped.dot(ft)


def dimension(listPointOfParallelepiped, angle1, angle2):
    angleR1 = (3 / 14 * angle1) / 180
    angleR2 = (3 / 14 * angle2) / 180
    f1 = np.array(
        [[mh.cos(angleR1), 0, -mh.sin(angleR1), 0], [0, 1, 0, 0], [mh.sin(angleR1), 0, mh.cos(angleR1), 1],
         [0, 0, 0, 0], ])
    ft1 = f1.T
    Prxy = listPointOfParallelepiped.dot(ft1)
    f2 = np.array(
        [[1, 0, 0, 0], [0, mh.cos(angleR2), mh.sin(angleR2), 0], [0, -mh.sin(angleR2), mh.cos(angleR2), 0],
         [0, 0, 0, 1]])
    ft2 = f2.T
    return Prxy.dot(ft2)


def rasterize(P1, P2):
    [x1, y1] = P1
    [x2, y2] = P2
    DX = x2 - x1
    DY = y2 - y1
    sG_x = 1 if DX > 0 else -1 if DX < 0 else 0
    sG_y = 1 if DY > 0 else -1 if DY < 0 else 0
    if DX < 0: DX = -DX
    if DY < 0: DY = -DY
    if DX > DY:
        pDX, pDY = sG_x, 0
        es, el = DY, DX
    else:
        pDX, pDY = 0, sG_y
        es, el = DX, DY
    x, y = x1, y1
    error, t = el / 2, 0
    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sG_x
            y += sG_y
        else:
            x += pDX
            y += pDY
        t += 1
        obj = Point(x, y)
        Tx.append(x)
        Ty.append(y)
        obj.setFill("lightskyblue")
        obj.draw(win)


def createLineForDrawWithBezie(Points):
    A = [Points[0, 0], Points[0, 1]]
    B = [Points[1, 0], Points[1, 1]]
    C = [Points[5, 0], Points[5, 1]]
    D = [Points[4, 0], Points[4, 1]]
    A1 = [Points[2, 0], Points[2, 1]]
    B1 = [Points[3, 0], Points[3, 1]]
    C1 = [Points[6, 0], Points[6, 1]]
    D1 = [Points[7, 0], Points[7, 1]]
    return [[A1, C1], [C1, C], [C, B], [A, B1], [B1, D1], [D1, D], [D, A], [A, B], [B, A1], [A1, B1], [B1, A],
            [D, C], [C1, D1]]


def drawWithBezie(listOfPoints1):
    listOfPoints = multipr(listOfPoints1)
    listOfLines = createLineForDrawWithBezie(listOfPoints)
    for i in listOfLines:
        [P1, P2] = i
        rasterize(P1, P2)
        funcBezie()


def funcBezie():
    for i in range(len(Tx) - 1):
        x1 = Tx[i] * (1 - 0) + Tx[i + 1] * 0
        x2 = Tx[i] * (1 - 1) + Tx[i + 1] * 1
        y1 = Ty[i] * (1 - 0) + Ty[i + 1] * 0
        y2 = Ty[i] * (1 - 1) + Ty[i + 1] * 1
        obj = Line(Point(x1, y1), Point(x2, y2))
        obj.setOutline("blue")
        obj.draw(win)
    Ty.clear()
    Tx.clear()


def getPoint(coords):
    return Point(coords[0], coords[1])


def getMiddlePoint(point1, point2):
    return getNthPoint(point1, point2, 2)


def getNthPoint(point1, point2, N):
    return [(point1[0] + point2[0]) / N, (point1[1] + point2[1]) / N]


def buildTriangle(point1, point2, point3, win, color="red"):
    Line(getPoint(point1), getPoint(point2)).draw(win).setOutline(color)
    Line(getPoint(point1), getPoint(point3)).draw(win).setOutline(color)
    Line(getPoint(point2), getPoint(point3)).draw(win).setOutline(color)


def drawSierpinski(point1, point2, point3, win, depth):
    buildTriangle(point1, point2, point3, win)
    if depth > 0:
        drawSierpinski(point1, getMiddlePoint(point1, point2), getMiddlePoint(point1, point3), win, depth - 1)
        drawSierpinski(point2, getMiddlePoint(point2, point1), getMiddlePoint(point2, point3), win, depth - 1)
        drawSierpinski(point3, getMiddlePoint(point3, point1), getMiddlePoint(point3, point2), win, depth - 1)


def in_mandel(x, y):
    z = 0
    c = x + 1j * y
    for i in range(10):
        z = z ** 2 + c
        if abs(z) > 10:
            return False
    return True


def drawMandelbrot(win):
    for x in range(2 * sizeMandel):
        for y in range(2 * sizeMandel):
            if in_mandel((x - sizeMandel) * 2 / sizeMandel, (y - sizeMandel) * 2 / sizeMandel):
                Point(x + retreatForMandel, y).draw(win).setFill('green')


def main(window):
    l = (pl / 2) - st
    listOfPoints1 = shift(listPointOfParallelepiped, l)
    listOfPoints1 = dimension(listOfPoints1, angle1, angle2)
    drawMandelbrot(win)
    drawSierpinski(*triSirpinsky, window, 6)
    drawWithBezie(listOfPoints1)
    window.getMouse()
    win.close()


num = 0
pl = 400
st = 60
if __name__ == '__main__':
    win = GraphWin("Lab6", 800, 800)
    main(win)
    win.close()
