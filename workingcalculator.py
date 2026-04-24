import sys
from PyQt5.QtWidgets import ( QApplication,QWidget,
                             QPushButton,QLineEdit,QGridLayout)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator
class calculator_app(QWidget):
    def __init__(self):
        super().__init__()
        self.history_value=[]
        self.display_box=QLineEdit(self)
        self.label1=QPushButton("1",self)
        self.label2=QPushButton("2",self)
        self.label3=QPushButton("3",self)
        self.label4=QPushButton("4",self)
        self.label5=QPushButton("5",self)
        self.label6=QPushButton("6",self)
        self.label7=QPushButton("7",self)
        self.label8=QPushButton("8",self)
        self.label9=QPushButton("9",self)
        self.label0=QPushButton("0",self)
        self.label_add=QPushButton("+",self)
        self.label_sub=QPushButton("-",self)
        self.label_mul=QPushButton("X",self)
        self.label_div=QPushButton("÷",self)
        self.equals=QPushButton("=",self)
        self.factroial=QPushButton("%",self)
        self.clear=QPushButton("AC",self)
        self.cross=QPushButton("de",self)
        self.dot=QPushButton(".",self)
        self.history=QPushButton("his",self)

        
        

        self.initGUI()
    def initGUI(self):
        self.setGeometry(500,200,450,600)
        regx=QRegExp(r"[1-9//-+/%*0]*")
        validator=QRegExpValidator(regx)
        self.display_box.setValidator(validator)
        hbox=QGridLayout()
        hbox.addWidget(self.display_box,0,0,1,4)

        hbox.addWidget(self.factroial,3,2)
        hbox.addWidget(self.clear,3,1)
        hbox.addWidget(self.label_div,3,3)
        hbox.addWidget(self.cross,3,0)


        hbox.addWidget(self.label7,4,0)
        hbox.addWidget(self.label8,4,1)
        hbox.addWidget(self.label9,4,2)
        hbox.addWidget(self.label_mul,4,3)

        hbox.addWidget(self.label4,5,0)
        hbox.addWidget(self.label5,5,1)
        hbox.addWidget(self.label6,5,2)
        hbox.addWidget(self.label_sub,5,3)

        hbox.addWidget(self.label1,6,0)
        hbox.addWidget(self.label2,6,1)
        hbox.addWidget(self.label3,6,2)
        hbox.addWidget(self.label_add,6,3)
        
        hbox.addWidget(self.history,7,0)
        hbox.addWidget(self.label0,7,1)
        hbox.addWidget(self.dot,7,2)
        hbox.addWidget(self.equals,7,3)
        self.setLayout(hbox)
        self.display_box.setFixedHeight(80)
        self.clear.setObjectName("clear")
        self.display_box.setObjectName("display_box")
        self.label_add.setObjectName("add")
        self.label_sub.setObjectName("sub")
        self.label_mul.setObjectName("mul")
        self.label_div.setObjectName("div")
        self.factroial.setObjectName("fac")
        self.equals.setObjectName("equals")
        self.display_box.setAlignment(Qt.AlignRight)

        
        self.setStyleSheet("""
                          QPushButton{
                           font-size: 40px;
                           font-weight: bold;
                           background-color: hsl(279, 5%, 16%);
                           border-radius:15px;
                           border:1px solid;
                           color:white;
                           }
                           QPushButton#clear{
                           background-color:hsl(359, 90%, 43%);
                           
                           }
                            QPushButton#add{
                           background-color: hsl(18, 94%, 49%)
                           }
                            QPushButton#sub{
                           background-color: hsl(18, 94%, 49%)
                           }
                            QPushButton#mul{
                           background-color: hsl(18, 94%, 49%)
                           }
                            QPushButton#div{
                           background-color: hsl(18, 94%, 49%)
                           }
                            QPushButton#fac{
                           background-color: hsl(18, 94%, 49%)
                           }
                           QPushButton#equals{
                           background-color: hsl(18, 94%, 49%)
                           }
                           QLineEdit#display_box{
                           border-radius:15px;
                           border:3px solid;
                           font-size: 40px}
                            """)
        self.label0.clicked.connect(lambda: self.compute("0"))
        self.label1.clicked.connect(lambda: self.compute("1"))
        self.label2.clicked.connect(lambda: self.compute("2"))
        self.label3.clicked.connect(lambda: self.compute("3"))
        self.label4.clicked.connect(lambda: self.compute("4"))
        self.label5.clicked.connect(lambda: self.compute("5"))
        self.label6.clicked.connect(lambda: self.compute("6"))
        self.label7.clicked.connect(lambda: self.compute("7"))
        self.label8.clicked.connect(lambda: self.compute("8"))
        self.label9.clicked.connect(lambda: self.compute("9"))

        self.label_add.clicked.connect(lambda: self.buttons_red("+"))
        self.label_div.clicked.connect(lambda: self.buttons_red("÷"))
        self.label_mul.clicked.connect(lambda: self.buttons_red("×"))
        self.label_sub.clicked.connect(lambda: self.buttons_red("-"))
        self.factroial.clicked.connect(lambda: self.buttons_red("%"))
        self.dot.clicked.connect(lambda: self.buttons_red("."))
        self.history.clicked.connect(self.get_history)



        self.clear.clicked.connect(self.cleare)
        self.equals.clicked.connect(self.display)
        self.cross.clicked.connect(self.delete)
        
    def display(self):
      try:
            value=self.display_box.text()
            value1=""
            for i in value:
                if i == "×":
                    i ="*"
                elif i == "÷":
                    i="/"
                value1+=i 
            result= eval(value1)
            
            self.history_value.append(value+"="+f"{str(result)}")
            self.display_box.setText(str(result))
      except ZeroDivisionError:
          self.display_box.setText("Cant divide with zero")
      except:
          self.display_box.clear()
       

    def compute(self,value):
        current=self.display_box.text()
        self.display_box.setText(current+value)
    def cleare(self):
        self.display_box.clear()
    def delete(self):
        value=self.display_box.text()
        if value:
            value = value[:-1]
        if value == "":
           self.display_box.clear()
        self.display_box.setText(value)
    def buttons_red(self,value):
        operator=["+", "-" ,"÷", "×","%","."]
        text = self.display_box.text()
        if  not text and value in operator:
            return
 
        if value in operator:
         if text and text[-1] in operator:
            text=text[:-1]
        self.display_box.setText(text+value)
    def get_history(self):
        try:
            if not self.history_value:
                self.display_box.setText("No history found")
            for all_history in self.history_value:
                self.display_box.setText(f"{all_history}")
          
        except:
            pass
def main():
    app=QApplication(sys.argv)
    calculator=calculator_app()
    calculator.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()
        

