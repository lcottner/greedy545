# imports
from tkinter import *
import math
import timeit
import matplotlib
import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Object class for Vertices
class Vertex:
    def __init__(self, name, point):
        self.name = name
        self.point = point

# Object class for Edges
class Edge:
    distance = 0

    def __init__(self, name, node1, node2):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        if (node1 != 0):
            self.distance = math.dist(node1.point, node2.point)

    def setVars(self, name, node1, node2):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.distance = math.dist(node1.point, node2.point)


# Initializes the plot in the tkinter GUI
def canvasInit(root, figure, plot):
    plot.plot(0, 0, color="white", marker="o", linestyle="")
    plot.plot(100, 100, color="white", marker="o", linestyle="")
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().grid(row=0, column=0)
    figure.supxlabel('X Axis')
    figure.supylabel('Y Axis')



# Draws the text above the node
def annotater(plot, node):
    plot.annotate(node.name, (node.point[0], node.point[1]), xytext=(node.point[0], node.point[1] + 1.5))


# Draws the node to the screen
def initPoint(plot, node):
    plot.plot(node.point[0], node.point[1], color="blue", marker="o", linestyle="")
    annotater(plot, node)


# Draws each edge in arrayEdge to the plot
def plotEdge(plot, arrayEdge):
    for edge in arrayEdge:
        plot.plot([edge.node1.point[0], edge.node2.point[0]], [edge.node1.point[1], edge.node2.point[1]], color='red')


# Determines the distance from the edge to a point
def calcEdgeDist(edge, extraN):
    ba = [edge.node2.point[0]-edge.node1.point[0], edge.node2.point[1]-edge.node1.point[1]]
    pa = [extraN.point[0]-edge.node1.point[0], extraN.point[1]-edge.node1.point[1]]
    proj = numpy.dot(ba, pa)
    distSq = edge.distance*edge.distance
    attemptRange = proj/distSq
    cp = [0, 0]
    if (attemptRange <= 0):
        cp[0] = edge.node1.point[0]
        cp[1] = edge.node1.point[1]
    else:
        if (attemptRange >= 1):
            cp[0] = edge.node2.point[0]
            cp[1] = edge.node2.point[1]
        else:
            cp[0] = edge.node1.point[0]+(ba[0]*attemptRange)
            cp[1] = edge.node1.point[1]+(ba[1]*attemptRange)

    shortDist = math.dist(cp, extraN.point)

    return shortDist


# Determines which edge should be removed
def bestEdge(arrayEdge, node):
    shortest = calcEdgeDist(arrayEdge[0], node)
    chosen = arrayEdge[0]

    for i in arrayEdge:
        if (calcEdgeDist(i, node) < shortest):
            shortest = calcEdgeDist(i, node)
            chosen = i

    updateArrayEdges(arrayEdge, chosen, node)


# Appends a new edge that connects node1 of chosen to the new node and changes chosen node 2 to the new node
def updateArrayEdges(arrayEdge, chosen, node):
    arrayEdge.append(Edge(len(arrayEdge)-1, chosen.node2, node))
    chosen.setVars(chosen.name, chosen.node1, node)


# Main Method
if __name__ == '__main__':
    startIt = timeit.default_timer()

    # Initialize canvas
    matplotlib.use("TkAgg")
    root = Tk()
    figure = Figure(figsize=(7, 7), dpi=100)
    plot = figure.add_subplot(1, 1, 1)
    canvasInit(root, figure, plot)

    #Hard coded vertices
    v1 = Vertex(1, [87.951292, 2.658162])
    v2 = Vertex(2, [33.466597, 66.682943])
    v3 = Vertex(3, [91.778314, 53.807184])
    v4 = Vertex(4, [20.526749, 47.633290])
    v5 = Vertex(5, [9.006012, 81.185339])
    v6 = Vertex(6, [20.032350, 2.761925])
    v7 = Vertex(7, [77.181310, 31.922361])
    v8 = Vertex(8, [41.059603, 32.578509])
    v9 = Vertex(9, [18.692587, 97.015290])
    v10 = Vertex(10, [51.658681, 33.808405])
    v11 = Vertex(11, [44.563128, 47.541734])
    v12 = Vertex(12, [37.806330, 50.599689])
    v13 = Vertex(13, [9.961241, 20.337535])
    v14 = Vertex(14, [28.186895, 70.415357])
    v15 = Vertex(15, [62.129582, 6.183050])
    v16 = Vertex(16, [50.376904, 42.796106])
    v17 = Vertex(17, [71.285134, 43.671987])
    v18 = Vertex(18, [34.156316, 49.113437])
    v19 = Vertex(19, [85.201575, 71.837519])
    v20 = Vertex(20, [27.466659, 1.394696])
    v21 = Vertex(21, [97.985778, 44.746239])
    v22 = Vertex(22, [40.730003, 98.400830])
    v23 = Vertex(23, [73.799860, 61.076693])
    v24 = Vertex(24, [85.076449, 17.029328])
    v25 = Vertex(25, [16.052736, 11.899167])
    v26 = Vertex(26, [20.160527, 67.238380])
    v27 = Vertex(27, [22.730186, 99.725333])
    v28 = Vertex(28, [77.196570, 88.503677])
    v29 = Vertex(29, [18.494217, 31.971191])
    v30 = Vertex(30, [72.743919, 16.071047])
    v31 = Vertex(31, [4.153569, 41.981262])
    v32 = Vertex(32, [79.027680, 95.034639])
    v33 = Vertex(33, [14.145329, 40.690329])
    v34 = Vertex(34, [66.258736, 70.360424])
    v35 = Vertex(35, [22.656941, 52.076785])
    v36 = Vertex(36, [51.797386, 78.902954])
    v37 = Vertex(37, [59.477124, 54.852321])
    v38 = Vertex(38, [27.042484, 29.957806])
    v39 = Vertex(39, [43.790850, 15.189873])
    v40 = Vertex(40, [60.375817, 31.645570])

    # Draw vertices
    initPoint(plot, v1)
    initPoint(plot, v24)
    initPoint(plot, v30)

    # Initialize starting points
    e1 = Edge(1, v1, v24)
    e2 = Edge(2, v1, v30)
    e3 = Edge(3, v24, v30)

    # Initialize arrays
    arrayEdge = [e1, e2, e3]
    arrayVertex=[v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v25, v26, v27, v28, v29, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40]
    path=[v1, v24, v30]


    #Greedy algorithm loop
    while len(arrayVertex) != 0:
        tempDist=10000
        selectedVertex=[arrayVertex[0]]
        for x in arrayVertex:
            for y in arrayEdge:
                if calcEdgeDist(y, x) < tempDist:
                    tempDist=calcEdgeDist(y,x)
                    selectedVertex=x

        arrayVertex.remove(selectedVertex)
        path.append(selectedVertex)
        initPoint(plot, selectedVertex)
        bestEdge(arrayEdge, selectedVertex)

    # Draw edges
    plotEdge(plot, arrayEdge)

    # Calculating path cost
    totalDist = 0
    for i in arrayEdge:
        totalDist = i.distance+totalDist

    print("Cost: ", totalDist)

    # Calculating path
    runEdge=arrayEdge[0]
    runner=runEdge.node1.name
    text=''
    print("Path: " ,runner, end='')
    arrayEdge.remove(runEdge)

    while len(arrayEdge)!=0:
        for x in range(len(arrayEdge)):
            if runner==arrayEdge[x].node1.name:
                runEdge=arrayEdge[x]
                text=arrayEdge[x].node2.name
            if runner == arrayEdge[x].node2.name:
                runEdge=arrayEdge[x]
                text=arrayEdge[x].node1.name
        print("", text, end='')
        arrayEdge.remove(runEdge)
        runner=text

    print("", 1, end='')

    endIt = timeit.default_timer()
    print("\nTime in seconds: ", endIt - startIt)

    #displays gui
    root.mainloop()
