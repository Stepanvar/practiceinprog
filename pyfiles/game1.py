from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys 
import random
class Maximus (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.show()

class Valina(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        hbox=QHBoxLayout(self)
        pixmap=QPixmap("hex.png")
        ql=QLabel(self)
        ql.setPixmap(pixmap)
        hbox.addWidget(ql)
        self.setLayout(hbox)
        self.move(400,400)

        self.btn = QPushButton('Vvedi', self)
        self.btn.move(10, 0)
        self.btn.clicked.connect(self.showDialog)
        self.le = QLineEdit(self)
        self.le.move(100, 0)
        self.setGeometry(300, 300, 390, 150)
        self.setWindowTitle('Input dialog')

        bt1 = QPushButton("left", self)
        bt1.move(45, 300)
        bt2 = QPushButton("middle", self)
        bt2.move(235, 300)        
        bt3 = QPushButton("right", self)
        bt3.move(425, 300)     
        bt1.clicked.connect(self.buttonClicked)
        bt2.clicked.connect(self.buttonClicked)
        bt3.clicked.connect(self.buttonClicked)
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Labirintum')
        self.show()

    def paintEvent(self, event):
        # sender = self.sender()
        # typebutton = "h"
        # if sender != None:
        #     typebutton = sender.text()
        pa = QPainter(self)
        pa.begin(self)
        list1 = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
        # print (typebutton)
        # if typebutton != "left" or typebutton != "middle" or typebutton != "right":
        #     rand_list_index = random.randint(0,2)
        #     color_choose1 = list1.pop(rand_list_index)
        #     pa.setBrush(QColor(color_choose1[0], color_choose1[1], color_choose1[2]))
        #     pa.drawRect(10, 40, 185, 250)
        #     rand_list_index = random.randint(0,1)
        #     color_choose2 = list1.pop(rand_list_index)
        #     pa.setBrush(QColor(color_choose2[0], color_choose2[1], color_choose2[2]))
        #     pa.drawRect(200, 40, 185, 250)
        #     color_choose3 = list1[0]
        #     pa.setBrush(QColor(color_choose3[0], color_choose3[1], color_choose3[2]))
        #     pa.drawRect(390, 40, 185, 250)
        # else:
        pa.setBrush(QColor(list1[0][0], list1[0][1], list1[0][2]))
        pa.drawRect(10, 40, 185, 250)
        pa.setBrush(QColor(list1[1][0], list1[1][1], list1[1][2]))
        pa.drawRect(200, 40, 185, 250)
        pa.setBrush(QColor(list1[2][0], list1[2][1], list1[2][2]))
        pa.drawRect(390, 40, 185, 250)
        pa.end()
        

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', "enter amount of points at the beginning:")
        if ok:      
            self.le.setText(text)
            self.life=int(text)

    def buttonClicked(self, event):
        reply = QMessageBox.question(self, 'Vnimanie!',
        "Are you sure to press button?", QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            mess = QMessageBox.information(self, 'Message', "you pressed button")
            if self.life in range (0, 100):
                self.life += random.randint(-3,3)
                result = QMessageBox.information(self, 'Message', "your points : %d" %self.life)
            else:
                mess= QMessageBox.information(self, 'Message', "game over") 
                sys.exit(app.exec_())
                  
        else:
            mess= QMessageBox.information(self, 'Message', "you cancel pressing button")
            event=False
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2) 
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Valina()
  sys.exit(app.exec_())
if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Maximus()
  sys.exit(app.exec_())