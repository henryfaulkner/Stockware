import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QSize
from requestData import requestData
from responseData import graphing
from timeSeriesPlot import timeSeriesPlot
from SMAPlot import SMAPlot

class Window_1(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Stock Analysis'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox =QLabel('Enter a stock',self)
        self.textbox.move(20,20)
        self.textbox.resize(280,40)

        self.textStuff = QLineEdit(self)
        self.textStuff.move(20,60)
        self.textStuff.resize(280,20)

        self.button1 = QPushButton('Analyze' ,self)
        self.button1.move(20,80)
        self.button1.resize(150,30)

        #connect button to function on_click
        self.button1.clicked.connect(self.on_click)
        self.show()

        
    def on_click(self):
        self.textboxValue = self.textStuff.text()
        self.dialog = Window_2(self.textboxValue)
        self.dialog.show()


class Window_2(QMainWindow):

    def __init__(self, stockValue):
        super().__init__()
        self.stockValue = stockValue
        self.title = "Another WindoWwww"
        self.left = 150
        self.top = 150
        self.width = 400
        self.height = 450
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLabel('Graphs for ' + self.stockValue, self)
        self.textbox.move(20,20)
        self.textbox.resize(150,30)

        self.graphButton1 = QPushButton('Line Graph', self)
        self.graphButton1.resize(150,30)
        self.graphButton1.move(20,60)

        self.graphButton2 = QPushButton('Time Series Plot', self)
        self.graphButton2.resize(150,30)
        self.graphButton2.move(20,90)


        self.graphButton3 = QPushButton('SMA Plot', self)
        self.graphButton3.resize(150,30)
        self.graphButton3.move(20,120)

        self.graphButton1.clicked.connect(self.graphButton_1)
        self.graphButton2.clicked.connect(self.graphButton_2)
        self.graphButton3.clicked.connect(self.graphButton_3)

    def graphButton_1(self):
        print('button1')
        daysList, openList,highList, lowList, closeList = requestData.weekly_OLH_Data(self.stockValue)
        graphing.past_week_open_low_high(self.stockValue, daysList, openList, highList, lowList, closeList)

    def graphButton_2(self):
        print('button2')
        timeSeriesPlot.timeSeriesPlot(self.stockValue)
        

    def graphButton_3(self):
        print('button3')
        SMAPlot.SMAPlot(self.stockValue)
        
        


        
