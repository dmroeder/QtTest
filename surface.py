from PyQt5 import QtGui, uic

qtSurfaceFile = "surface.ui"
ui_surface, base_surface = uic.loadUiType(qtSurfaceFile)

class Surface(base_surface, ui_surface):
    
    def __init__(self):
        super(base_surface,self).__init__()
        self.setupUi(self)

        self.painter = QtGui.QPainter()
        self.Shapes = []
        
        #------------------
        # this is just temporary
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor('orange'))
        self.setPalette(p)
        #------------------
        
    def addShape(self, shape, x, y):
        self.Shapes.append(shape)
        s = shape
        s.setParent(self.widget)
        s.move(x,y)
        return
