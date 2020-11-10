import matplotlib.pyplot as plt
import numpy as np
from graphics import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

colr1 = "red"
colr2 = "blue"
colr3 = "orange"
colr4 = "green"

pos = [200, 150]
dimension = 40

def firstTask():
    win = GraphWin("Task 1", 500, 400)
    x1, y1 = 0, 1
    x2, y2 = 1, 0
    x3, y3 = 2, 1

    def createTriangle(p1, p2, p3, win, colour):
        Line(p1, p2).draw(win).setFill(colour)
        Line(p1, p3).draw(win).setFill(colour)
        Line(p2, p3).draw(win).setFill(colour)

    for i in range(4):
        p1 = Point(pos[0] + (x1 - 1.5 * i) * dimension, pos[1] + (y1 + 0.5 * i) * dimension)
        p2 = Point(pos[0] + x2 * dimension, pos[1] + (y2 - i) * dimension)
        p3 = Point(pos[0] + (x3 + 1.5 * i) * dimension, pos[1] + (y3 + 0.5 * i) * dimension)
        win.getMouse()
        if i > 2:
            createTriangle(p1, p2, p3, win, colr1)

        elif i > 0:
            createTriangle(p1, p2, p3, win, colr2)

        else:
            createTriangle(p1, p2, p3, win, colr3)
    win.getMouse()
    win.close()



def secondTask1():
    win = GraphWin("Task 2.1", 400, 250)

    def createRomb(x, y, colour="black"):
        Rline1 = Line(Point(x, y - 60), Point(x + 60, y))
        Rline2 = Line(Point(x - 60, y), Point(x, y - 60))
        Rline3 = Line(Point(x, y + 60), Point(x - 60, y))
        Rline4 = Line(Point(x + 60, y), Point(x, y + 60))

        def drawRomb(line, colour=colour):
            line.draw(win)
            line.setOutline(colour)

        drawRomb(Rline1)
        drawRomb(Rline2)
        drawRomb(Rline3)
        drawRomb(Rline4)

    # createRomb(200, 70)
    # createRomb(200, 140)
    # createRomb(245, 105)
    # createRomb(155, 105)

    createRomb(200, 70, colr1)
    createRomb(200, 140, colr2)
    createRomb(245, 105, colr3)
    createRomb(155, 105, colr4)

    win.getMouse()
    win.close()



def secondTask2():
    win = GraphWin("Task 2.2", 400, 250)

    romb1 = Polygon(Point(200, 20), Point(150, 70), Point(200, 120), Point(250, 70))
    romb2 = Polygon(Point(200, 90), Point(150, 140), Point(200, 190), Point(250, 140))
    romb3 = Polygon(Point(245, 55), Point(195, 105), Point(245, 155), Point(295, 105))
    romb4 = Polygon(Point(155, 55), Point(105, 105), Point(155, 155), Point(205, 105))

    def drawRomb(romb, colour = colr1):
        romb.draw(win)
        romb.setFill(colour)
        romb.setOutline(colour)

    drawRomb(romb1, colr1)
    drawRomb(romb2, colr2)
    drawRomb(romb3, colr3)
    drawRomb(romb4, colr4)

    win.getMouse()
    win.close()



def thirdTask():
    root = tk.Tk()
    root.title("Task 3")

    fig = plt.figure(figsize=(6, 6))
    ax_1 = fig.add_subplot(221)
    ax_2 = fig.add_subplot(222)
    ax_3 = fig.add_subplot(223)
    ax_4 = fig.add_subplot(224)

    ax_1.set_xlim([0, 10])
    ax_1.set_ylim([-1, 1])
    ax_1.set_xlabel("x")
    ax_1.set_ylabel("y")
    ax_1.set_title("Law 1")

    ax_2.set_xlim([0, 10])
    ax_2.set_ylim([-1, 1])
    ax_2.set_xlabel("x")
    ax_2.set_ylabel("y")
    ax_2.set_title("Law 2")

    ax_3.set_xlim([0, 10])
    ax_3.set_ylim([-1, 1])
    ax_3.set_xlabel("x")
    ax_3.set_ylabel("y")
    ax_3.set_title("Law 3")

    ax_4.set_xlim([0, 10])
    ax_4.set_ylim([-1, 1])
    ax_4.set_xlabel("x")
    ax_4.set_ylabel("y")
    ax_4.set_title("Law 4")

    x = np.linspace(0, 10, 1000)

    a = 21
    ax_1.plot(x, (2 * a * 0.01) * np.sin(x), color=colr2)

    ax_2.plot(x, (3 * a * 0.01) * np.sin(x), color=colr3)

    ax_3.plot(x, (4 * a * 0.01) * np.sin(x), color=colr4)

    ax_4.plot(x, (2 * a * 0.01) * np.sin(x), color=colr2)
    ax_4.plot(x, (3 * a * 0.01) * np.sin(x), color=colr3)
    ax_4.plot(x, (4 * a * 0.01) * np.sin(x), color=colr4)

    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().pack()

    root.mainloop()



if __name__ == '__main__':
    firstTask()
    secondTask1()
    secondTask2()
    thirdTask()

