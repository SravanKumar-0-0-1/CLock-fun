#StopWatch using PyQt5: 
# This is a simple stopwatch that displays the time in hours, minutes, seconds, and milliseconds.
# The stopwatch has three buttons: Start, Stop, and Reset.

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import QFont,QFontDatabase

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time=QTime(0,0,0,0)
        self.time_label=QLabel("00:00:00:00",self)
        self.start_button=QPushButton("Start",self)
        self.stop_button=QPushButton("Stop",self)
        self.reset_button=QPushButton("Reset",self)
        self.timer=QTimer()
        self.WatchUI()
    def WatchUI(self):
        self.setWindowTitle("SRA1! Stopwatch")
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        hbox=QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton,QLabel{
                           padding:20px;
                           font-weight:bold;
                            border-radius:20px;
                           }
            QPushButton{
                           font-size:50px;
                           background-color:#ff0000;
                            color:white;
                           }
            QLabel{
                           font-size:120px;
                           color:#26ff00;
                           background-color:black;
                           }
                           """)
        font_id=QFontDatabase.addApplicationFont("C:/python full course/Clock_fun/DS-DIGIT.TTF")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family,50)
        self.time_label.setFont(my_font)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

       
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))
    def format_time(self,time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        milliseconds=time.msec()//10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"
    def update_display(self):
        self.time=self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__=="__main__":
     app=QApplication(sys.argv)
     watch=Stopwatch()
     watch.show()
     sys.exit(app.exec_())


    