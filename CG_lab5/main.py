from tkinter import messagebox
import numpy as np
from graphics import *
import math as mh

listBuildingObj = []
listOfLines = []
width = 300
length = 200
height = 250
retreat = 250

angle1 = 180
angle2 = -80

Tx = []
Ty = []
listPointOfParallelepiped = np.array([[width / 2 + retreat, length / 2 + retreat, -height / 2 + retreat, 1],
                                      [-width / 2 + retreat, length / 2 + retreat, -height / 2 + retreat, 1],
                                      [-width / 2 + retreat, -length / 2 + retreat, -height / 2 + retreat, 1],
                                      [width / 2 + retreat, -length / 2 + retreat, -height / 2 + retreat, 1],
                                      [width / 2 + retreat, length / 2 + retreat, height / 2 + retreat, 1],
                                      [-width / 2 + retreat, length / 2 + retreat, height / 2 + retreat, 1],
                                      [-width / 2 + retreat, -length / 2 + retreat, height / 2 + retreat, 1],
                                      [width / 2 + retreat, -length / 2 + retreat, height / 2 + retreat, 1]])


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


def drawWithBezie():
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
        obj.setOutline("red")
        obj.draw(win)
    Ty.clear()
    Tx.clear()


num = 0
pl = [400, 300, 500, 450, 550, 350, 600]
i = 0
st = 60
while True:
    win = GraphWin("method Bezie", 600, 600)
    l = (pl[i] / 2) - st
    listOfPoints1 = shift(listPointOfParallelepiped, l)
    listOfPoints1 = dimension(listOfPoints1, angle1, angle2)
    drawWithBezie()

    if num == 1:
        num = 0
        result = messagebox.askquestion('Attention', 'Завершити огляд фігури?')
        if result == 'yes':
            break
        else:
            win.close()
            continue
    num += 1
    win.close()

    if i == len(pl):
        i = 0
    i += 1
