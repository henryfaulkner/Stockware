from responseData import graphing
from requestData import requestData
from timeSeriesPlot import timeSeriesPlot
from SMAPlot import SMAPlot
from GUI import Window_1, Window_2
import sys
from PyQt5.QtWidgets import QApplication

def main():
    print("welcome")

if __name__ == "__main__":
    main()
    app = QApplication(sys.argv)
    GUI = Window_1()
    app.exec_()
