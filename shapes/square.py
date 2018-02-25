from PyQt5 import QtCore, QtGui, uic, QtWidgets

ui_square, base_square = uic.loadUiType("shapes/square.ui")

class Init(base_square, ui_square):
    
    def __init__(self):
        super(base_square,self).__init__()
        self.setupUi(self)
        self.painter = QtGui.QPainter()
        self.pen = QtGui.QPen(QtGui.QColor('blue'))

        # change the background to white
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor('white'))
        self.setPalette(p)
        
        self.adjustSize()
        
    def getSize(self):
        return self.geometry().width(), self.geometry().height()
    
    def paintEvent(self, event):

        #instruction width
        w = self.geometry().width()-30
        h = self.geometry().height()-20

        # draw a rectangle
        self.painter.begin(self)
        self.painter.setPen(self.pen)
        self.painter.drawRect(15,10,w,h)
        self.painter.end()
