import sys
from PyQt5.QtWidgets import (QApplication,QHBoxLayout,QVBoxLayout,
                             QLabel, QPushButton,QWidget,QLineEdit)
from PyQt5.QtCore import Qt
import requests
class main_app(QWidget):
 def __init__(self):
        super().__init__()
        self.label1=QLabel("Enter the city name",self)
        self.label2=QLineEdit(self)
        self.get_button=QPushButton("ENTER",self)
        self.emoje=QLabel(self)
        self.tempurature=QLabel(self)
        self.discription=QLabel(self)

        self.initGUI()
 def initGUI(self):
        
        self.setWindowTitle("Weather App")
        self.setGeometry(500,200,600,700)
        vbox=QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.get_button)
        vbox.addWidget(self.emoje)
        vbox.addWidget(self.tempurature)
        vbox.addWidget(self.discription)
        self.setLayout(vbox)

        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.emoje.setAlignment(Qt.AlignCenter)
        self.tempurature.setAlignment(Qt.AlignCenter)
        self.discription.setAlignment(Qt.AlignCenter)

        self.label1.setObjectName("label1")
        self.label2.setObjectName("label2")
        self.emoje.setObjectName("emoje")
        self.get_button.setObjectName("get_button")
        self.tempurature.setObjectName("temperature")
        self.discription.setObjectName("discription")
        self.label2.setFixedSize(700,60)
        

        self.setStyleSheet("""
                        
                             
                           QLabel#label1{
                           font-size: 50px;
                           }
                           QLineEdit#label2{
                           font-size : 40px;
                           }  
                           QPushButton#get_button{
                           font-family: italic;
                           font-size: 50px;
                           border-radius: 15px;
                           border: 3px solid;
                           }
                           QLabel#temperature{
                           font-size: 70px;}

                           QLabel#discription{
                           font-size: 30px;}

                           QLabel#emoje{
                           font-size: 60px;
                           font-family: "Apple Color Emoji";}
                    

                          """)
        self.get_button.clicked.connect(self.get_weather)

 def get_weather(self):
     api="a1270225b2b7e063e5c0d264347fd43a"
     city=self.label2.text()
     url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"  


     try:
       response=requests.get(url)
       response.raise_for_status()
       data=response.json()
       if data["cod"]==200:
            self.display(data)
     except requests.exceptions.HTTPError as http_error:
         match response.status_code:
             case 400:
                 self.error("Bad request\n please check your input")
             case 401:
                 self.error("unauthorized\n invalid AUI key")
            
             case 403:
                 self.error("Forbidden\n Access is denied")
             case 404:
                 self.error("Not found\n City is not found")
             case 500:
                 self.error("internal server error\n Please try agian later")
             case 502:
                 self.error("Bad Gateway\n invalid response from the server")
             case 503:
                 self.error("Serive unaviable\n Server is down")
             case 504:
                 self.error("Gateway timeout\n No response from the server")
             case _:
                 self.error(f"HTTP Error\n {http_error}")
     except requests.exceptions.ConnectionError:
         self.error("Connection error")
     except requests.exceptions.Timeout:
         self.error("Time Out")
     except requests.exceptions.TooManyRedirects:
         self.error("Too maney redirects")
     except requests.exceptions.RequestException as req_error:
         self.error(f"Request error\n {req_error}")

 def error(self,state):
      self.tempurature.setStyleSheet("font-size : 30px;")
      self.tempurature.setText(state)
      self.emoje.clear()
      self.discription.clear()
 def display(self,data):
      print(data)
      tempurature_1 = data["main"]["temp"] 
      tempurature_c=tempurature_1-273.15
      self.tempurature.setText(f"{tempurature_c:.0f}°C")
      dis=data["weather"][0]["description"]
      self.discription.setText(dis)
      emoje_id=data["weather"][0]["id"]
      self.emoje.setText(self.emojepicker(emoje_id))

 @staticmethod
 def emojepicker(emoje_id):
    if 200 <= emoje_id <= 232:
        return "⛈"
    elif 300 <= emoje_id <= 321:
        return "🌦️"
    elif 500 <= emoje_id <= 531:
        return "🌧️"
    elif 600 <= emoje_id <= 622:
        return "☃️"
    elif emoje_id == 762:
        return "🌋"
    elif emoje_id == 771:
        return "💨"
    elif emoje_id == 781:
        return "🌪️"
    elif 701 <= emoje_id <= 761 or 763 <= emoje_id <= 770:
        return "🌫️"
    elif emoje_id == 800:
        return "☀️"
    elif 801 <= emoje_id <= 804:
        return "☁️"
    else:
        return ""
    
        

def main():
    app=QApplication(sys.argv)
    weather_app=main_app()
    weather_app.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()


    