from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout,QWidget
from PyQt5.QtCore import Qt, QTime,QTimer
import sys
from PyQt5.QtGui import QFont, QFontDatabase

class digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.label1=QLabel("12:00:00",self)
        self.timer=QTimer()
        self.initGUI()



    def initGUI(self):
     self.setGeometry(500,300,500,200)
     vbox=QVBoxLayout()
     vbox.addWidget(self.label1)
     self.setLayout(vbox)
     self.label1.setAlignment(Qt.AlignCenter)
     self.label1.setStyleSheet("font-size : 120px;"
                                 "color : hsl(136, 3%, 38%);"
                                 )
     #font1=QFontDatabase.addApplicationFont("/Users/nikeshgc/Desktop/ptrhon/digital-7 (italic).ttf")
     #font_family=QFontDatabase.applicationFontFamilies(font1)[0]
     #my_font=QFont(font_family,150)

     #self.label1.setFont(my_font)
     
     
     self.timer.timeout.connect(self.display_time)
     self.timer.start(1000)
    def display_time(self):
       current_time=QTime.currentTime().toString("hh:mm:ss AP")
       self.label1.setText(current_time)
       


def main():
   app=QApplication(sys.argv)
   clock=digital_clock()
   clock.show()
   sys.exit(app.exec_())



if __name__=="__main__":
   main()