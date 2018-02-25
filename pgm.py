import sys
from PyQt5 import QtGui, uic, QtWidgets
import surface
from shapes import *
import time
 
qtCreatorFile = "window.ui" # Enter file here.
ui_main, base_main = uic.loadUiType(qtCreatorFile)

class Window(base_main, ui_main):
    
    def __init__(self):
        super(base_main,self).__init__()
        self.setupUi(self)
        
        #------------------
        # this is just temporary
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor('purple'))
        self.setPalette(p)
        #------------------
        
        # create some shape surfaces
        self.surfaces = [self.addSurface() for i in range(3)]
        
        # add some squares to our surfaces
        for index, surface in enumerate(self.surfaces):
            x = 0
            for i in range(7):
                # create a square
                s = square.Init()
                # add it to the current surface
                surface.addShape(s,x,0)
                # get the size so we can add another
                # one next to it
                w,h = s.getSize()
                pos = s.pos()
                x = pos.x() + w + 6
                if index % 2:
                    t = square.Init()
                    surface.addShape(t,0,120)
            
    def addSurface(self):
        # add a shape surface
        s = surface.Surface()
        self.verticalLayout.addWidget(s)
        return s

       
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

