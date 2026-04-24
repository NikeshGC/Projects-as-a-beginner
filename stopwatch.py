from PyQt5.QtWidgets import QApplication, QLabel,QVBoxLayout,QWidget,QPushButton,QHBoxLayout
import sys
from PyQt5.QtCore import QTime, QTimer,Qt
from PyQt5.QtGui import QFont, QFontDatabase
class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.button1=QPushButton("start",self)
        self.button2=QPushButton("STOP",self)
        self.button3=QPushButton("RESET",self)
        self.lable1=QLabel("00:00:00.00",self)
        self.time=QTime(0, 0, 0, 0)
        self.timer=QTimer(self)
        self.initGUI()
    def initGUI(self):
     self.setGeometry(500,300,500,200)


     Vbox=QVBoxLayout()
     Vbox.addWidget(self.lable1)
     self.lable1.setAlignment(Qt.AlignCenter)
     self.setLayout(Vbox)
     self.lable1.setStyleSheet("font-size : 100px;"
                               "color : black;"
                               "font-family : Courier New")


     hbox=QHBoxLayout()
     hbox.addWidget(self.button1)
     hbox.addWidget(self.button2)
     hbox.addWidget(self.button3)
     Vbox.addLayout(hbox)

     self.button1.setFixedSize(200, 50)
     self.button2.setFixedSize(200, 50)
     self.button3.setFixedSize(200, 50)
     self.button1.setStyleSheet("background-color : hsl(119, 73%, 81%);")
     self.button2.setStyleSheet("background-color : hsl(338, 68%, 72%);")
     self.button3.setStyleSheet("background-color : hsl(220, 74%, 73%);")
   
     
    
     self.setStyleSheet("""QPushButton{
                        font-size : 30px;
                        border-radius : 40px;
                        color : hsl(136, 3%, 38%);
                        border : 2px solid;
                        border-radius : 15px;
                        color : black;

                       }
                        QWidget{
                        background-color : hsl(228, 2%, 70%);}
                         """)
     

     #font1=QFontDatabase.addApplicationFont("/Users/nikeshgc/Desktop/ptrhon/Orbitron-VariableFont_wght.ttf")
     #font_family=QFontDatabase.applicationFontFamilies(font1)[0]
     #my_font=QFont(font_family,200)
     #self.lable1.setFont(my_font)


     self.button1.clicked.connect(self.start)
     self.button2.clicked.connect(self.stop)
     self.button3.clicked.connect(self.reset)
     self.timer.timeout.connect(self.update_time)


    def start(self):
      self.timer.start(10)


    def stop(self):
       self.timer.stop()

    def reset(self):
       self.timer.stop()
       self.time=QTime(0,0,0,0)
       self.lable1.setText(self.formate_time(self.time))
       
    def formate_time(self,time):
       hours=time.hour()
       minuts=time.minute()
       seconds=time.second()
       milisecond=time.msec()//10
       return f"{hours:02}:{minuts:02}:{seconds:02}:{milisecond:02}"
    

    def update_time(self):
       self.time=self.time.addMSecs(10)
       self.lable1.setText(self.formate_time(self.time))
     
def main():
   app=QApplication(sys.argv)
   watch=stopwatch()
   watch.show()
   sys.exit(app.exec_())
if __name__=="__main__":
   main()