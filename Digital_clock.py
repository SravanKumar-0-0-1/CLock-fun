#Digital Clock: 
# This is a simple digital clock that displays the current time in hours, minutes, and seconds. 
# The clock is updated every 300 milliseconds. 
# The clock is displayed in a large font size and the font used is DS-DIGIT.TTF. 
# The clock is displayed in the center of the window and the background color of the window is black. 
#  The icon of the window is set to fear.png. The window title is set to Digital Clock. 
# The Update_time method gets the current time using the QTime.currentTime() method. 

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QIcon,QFont,QFontDatabase
from PyQt5.QtCore import QTimer,QTime,Qt

class DigitalClock(QWidget):
    def __init__(self):
          super().__init__()
          self.time_label=QLabel(self)
          self.timer=QTimer(self)
          self.clockUI()

    def clockUI(self):
         self.setWindowTitle("Digital Clock")
         self.setGeometry(600,400,300,100)
         self.setWindowIcon(QIcon("C:/python full course/GUI_with_python/fear.png"))
         vbox=QVBoxLayout()
         vbox.addWidget(self.time_label)
         self.setLayout(vbox)
         self.time_label.setAlignment(Qt.AlignCenter)
         self.time_label.setStyleSheet("font-size:150px;"
                                       "color:#26ff00")
         self.setStyleSheet("Background-color:Black")
         font_id=QFontDatabase.addApplicationFont("C:/python full course/Clock_fun/DS-DIGIT.TTF")
         font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
         my_font=QFont(font_family,150)
         self.time_label.setFont(my_font)
         self.timer.timeout.connect(self.Update_time)
         self.timer.start(300)
         self.Update_time()
    def Update_time(self):
         current_time=QTime.currentTime().toString("hh:mm:ss AP")
         self.time_label.setText(current_time)
if __name__=="__main__":
     app=QApplication(sys.argv)
     window=DigitalClock()
     window.show()
     sys.exit(app.exec_())
