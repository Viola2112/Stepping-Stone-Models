# Stepping Stone Model 1.1

# Last edited: 3/19/2020

# Improvements since Stepping Stone Model 1.0:
    # Created a subclass "BorderStepStone" in which colors can't
    # cross borders to the other side

# Possible Future Work:
    # Finding stats using non-Visual StepStone models
        # Creating a separate stats module to show histograms & stuff
        # Finding relationship between size & time to run
        # Comparing BorderStepStone times w/ StepStone times
    # Creating rectangular StepStone models and comapring w/ square models
    # Creating a text-based interface and/or GUI
    

from graphics import *
from random import *
from time import sleep

def randElement(aList):
    return aList[randrange(len(aList))]

class Cell:

    def __init__(self,ulx,uly,size,color,xnum,ynum,window,isVisual=True):
        self.xNum = xnum
        self.yNum = ynum
        self.rect = Rectangle(Point(ulx,uly),Point(ulx+size,uly+size))
        self.col = color
        self.rect.setFill(self.col)
        self.win = window
        self.isVis = isVisual

    def getColor(self):
        return self.col

    def setColor(self,aColor):
        self.col = aColor
        #self.rect.undraw()
        self.rect.setFill(aColor)
        #self.draw()

    def draw(self):
        if self.isVis:
            self.rect.draw(self.win)


class StepStone:

    def __init__(self,ulx,uly,cellSize,cellsPerSide,colors,window,isVis=True):
        self.win = window
        self.cells = []
        for row in range(cellsPerSide):
            self.cells.append([])
            for col in range(cellsPerSide):
                self.cells[row].append(Cell(ulx+col*cellSize,uly+row*cellSize,
                                            cellSize,randElement(colors),
                                            col,row,window,isVis))
                self.cells[row][col].draw()
                                            

    def randNeighbor(self,xNum,yNum):
        possOffset = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        actOffset = randElement(possOffset)
        newPos = [xNum+actOffset[0],yNum+actOffset[1]]
        for i in range(2):
            if newPos[i] < 0:
                newPos[i] += len(self.cells)
            if newPos[i] >= len(self.cells):
                newPos[i] -= len(self.cells)
        return self.cells[newPos[0]][newPos[1]]

    def update(self,pause=0):
        aCell = randElement(randElement(self.cells))
        aCell.setColor(self.randNeighbor(aCell.xNum,aCell.yNum).getColor())
        sleep(pause)

    def run(self,numTimes,pause=0):
        for i in range(numTimes):
            self.update(pause)

    def isUniform(self):
        firstColor = self.cells[0][0].getColor()
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                if firstColor != self.cells[row][col].getColor():
                    return False
        return True

    def runUntilUniform(self,checkEvery,pause=0):
        count = 0
        while not self.isUniform():
            count += checkEvery
            self.run(checkEvery,pause)
        return count


class BorderStepStone(StepStone):

    def randNeighbor(self,xNum,yNum):
        possOffset = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        validNeighbor = False
        actOffset = randElement(possOffset)
        newPos = [xNum+actOffset[0],yNum+actOffset[1]]
        while not validNeighbor:
            actOffset = randElement(possOffset)
            newPos = [xNum+actOffset[0],yNum+actOffset[1]]
            validNeighbor = True
            for i in range(2):
                if newPos[i] < 0 or newPos[i] >= len(self.cells):
                    validNeighbor = False
                    break
        return self.cells[newPos[0]][newPos[1]]



g1 = GraphWin("Stepping Stone Model 1",500,500)
s1 = StepStone(50,50,20,20,["red","blue","green","yellow","brown"
                           ,"black","white","orange","purple","gray"],g1)
# squick can be used for stats tests b/c it's very quick
gq = GraphWin("Quick Stepping Stone Model",500,500)
squick = StepStone(50,50,20,20,["red","blue","green","yellow","brown"
                           ,"black","white","orange","purple","gray"],gq,False)
gb = GraphWin("Bordered Stepping Stone Model",500,500)
sborder = BorderStepStone(50,50,20,20,["red","blue","green","yellow","brown"
                           ,"black","white","orange","purple","gray"],gb)

if __name__ == "__main__":
    s1.runUntilUniform(1)
        
