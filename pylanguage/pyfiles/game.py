# def buttonClicked(self):
# driver = self.driver  # Например, драйвер будет в поле AutoTestWindow
# query = self.line_edit_query.text()  # А запрос будет в виджете
# findelem(driver, query)
# if a4 in range(10,101):   
# if a4 in range (10,31):
# while sum(a1) in range(sum(x1), sum(x)):
# a=random.randint(-5,3)
# print ("sender.text() + ' was pressed,%d"%a)
# a1.append(a)
# elif a4 in range (31,51):
# while sum(a1) in range(sum(x1), sum(x)):
# a=random.randint(-3,3)
# print ("sender.text() + ' was pressed,%d"%a)
# a1.append(a)
# elif a4 in range (51,101):
# while sum(a1) in range(sum(x1), sum(x)):
# a=random.randint(-3,5)
# print ("sender.text() + ' was pressed,%d"%a)
# a1.append(a)     
# else:
# print("zhulie, game over")
# sys.exit()
# class Maximus (QWidget):
# def __init__(self):
# super().__init__()
# self.initUI()
# def initUI(self):
# self.setGeometry(300, 300, 400, 400)
# self.show()

# class Valina(QWidget):
# def __init__(self):
# super().__init__()
# self.initUI()
# def initUI(self):
# hbox=QHBoxLayout(self)
# pixmap=QPixmap("hex.png")
# ql=QLabel(self)
# ql.setPixmap(pixmap)
# hbox.addWidget(ql)
# self.setLayout(hbox)
# self.move(400,400)

# bt1 = QPushButton("left", self)
# bt1.move(0, 400)
# bt2 = QPushButton("middle", self)
# bt2.move(150, 400)        
# bt3 = QPushButton("right", self)
# bt3.move(300, 400)        

# bt1.clicked.connect(self.buttonClicked)
# bt2.clicked.connect(self.buttonClicked)
# bt3.clicked.connect(self.buttonClicked)
# self.setGeometry(300, 300, 290, 150)
# self.setWindowTitle('Labirintum')
# self.show()
# def buttonClicked(self):
# sender = self.sender()
# if a4 in range(10,101):   
# if a4 in range (10,31):
# while sum(a1) in range(sum(x1), sum(x)):
# a=random.randint(-5,3)
# print ("sender.text() + ' was pressed,%d"%a)
# a1.append(a)
# elif a4 in range (31,51):
# while sum(a1) in range(sum(x1), sum(x)):
# a=random.randint(-3,3)
# print ("sender.text() + ' was pressed,%d"%a)
# a1.append(a)
# elif a4 in range (51,101):
# while sum(a1) in range(sum(x1), sum(x)):
# a=random.randint(-3,5)
# print ("sender.text() + ' was pressed,%d"%a)
# a1.append(a)     
# else:
# print("zhulie, game over")
# sys.exit()
# def closeEvent(self, event):
# reply = QMessageBox.question(self, 'Message',
# "Are you sure to quit?", QMessageBox.Yes |
# QMessageBox.No, QMessageBox.No)
# if reply == QMessageBox.Yes:
# event.accept()
# else:
# event.ignore()

# if __name__ == '__main__':
# app = QApplication(sys.argv)
# ex = Valina()
# sys.exit(app.exec_())

# if __name__ == '__main__':
# app = QApplication(sys.argv)
# ex = Maximus()
# sys.exit(app.exec_())

# if sum(a)>= sum(a1):
# print ("vi proshli labirint")
# if sum(a)<= -sum(a1):
# print ("game over")



# ini = QSettings(iniFile, QSettings.IniFormat)
# ini.setIniCodec("utf-8")
# class :
# def __init__(self):
# super().__init__()
# self.initUI()
# def initUI(self):
# ex = Maximum()



# self.setWindowIcon(QIcon("wex.png"))

# def keyPressEvent(self,r):
# if r.key()==QTKey_r:
# reply=QMessageBox.question(self, 'Message', "Are you sure you want press r?",
# QMessageBox.Yes| QMessageBox.No, QMessageBox.No)
# if reply==QMessageBox.Yes:
# event.accept()
# choose=4
# elif reply==QMessageBox.No:
# event.ignore()

# if __name__ == '__main__':

# app = QApplication(sys.argv)
# ex = Vanna()
# sys.exit(app.exec_())

# class Victori(QWidget):

# def __init__(self):
# super().__init__()
# self.initUI()

# def initUI(self):

# if __name__ == '__main__':
# app = QApplication(sys.argv)
# ex = Victori()
# sys.exit(app.exec_())
# class ikonostasia(QWidget):

# super().__init__()
# self.initUI
# if s2>=0:    
# def initUI:

# self.btn = QPushButton('Vvedi', self)
# self.btn.move(10, 0)
# self.btn.clicked.connect(self.showDialog)
# self.le = QLineEdit(self)
# self.le.move(100, 0)
# self.setGeometry(300, 300, 390, 150)
# self.setWindowTitle('Input dialog')

# bt1 = QPushButton("left", self)
# bt1.move(30, 300)
# bt2 = QPushButton("middle", self)
# bt2.move(150, 300)        
# bt3 = QPushButton("right", self)
# bt3.move(270, 300)
# bt4 = QPushButton("right", self)
# bt4.move(390, 300)     
# bt1.clicked.connect(self.buttonClicked)
# bt2.clicked.connect(self.buttonClicked)
# bt3.clicked.connect(self.buttonClicked)
# bt4.clicked.connect(self.buttonClicked)
# self.setGeometry(300, 300, 600, 500)
# self.setWindowTitle('Labirintum')
# self.show()

# def center(self):

# screen = QDesktopWidget().screenGeometry()
# size = self.geometry()
# self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2) 

# def paintEvent(self, event):    

# pa = QPainter(self)
# pa.begin(self)
# self.drawRectangles(pa)
# pa.end()

# def drawRectangles(self, pa):

# pa.setBrush(QColor(255,0,0))
# pa.drawRect(10, 25, 185, 250)
# pa.setBrush(QColor(0,255,0))
# pa.drawRect(150, 25, 185, 250)
# pa.setBrush(QColor(0,0,255))
# pa.drawRect(290, 25, 185, 250)
# pa.setBrush(QColor(125,125,125))
# pa.drawRect(330, 25, 185, 250)

# def showDialog(self):

# text, ok = QInputDialog.getText(self, 'Input Dialog', "vvedite koichestvo ochkov do kotorix budete igrat ot 10 do 30 - slojno, ot 31 do 50-normalno, ot 51 do 100-legko:")
# if ok:      
# self.le.setText(text)
# self.tt=int(text)

# def buttonClicked(self, event):

# sender=self.sender
# reply = QMessageBox.question(self, 'Vnimanie!',
# "Are you sure to press button?", QMessageBox.Yes |
# QMessageBox.No, QMessageBox.No)
# if reply == QMessageBox.Yes:
# mess= QMessageBox.information(self, 'Message', "you pressed button")
# while len(x)<self.tt+1:
# x.insert(0,1)
# while len(x1)<self.tt:
# x1.insert(0,-1)
# if self.tt in range (10,101):
# if self.tt in range (10,31):
# a1=[self.tt]
# if sum(a1) in range (sum(x1), sum(x)):
# a=random.randint(-5,3)
# print("button was pressed,%d"%a)        
# a1.append(a)
# elif self.tt in range (31,51):
# a1=[self.tt]
# if sum(a1) in range (sum(x1), sum(x)):
# a=random.randint(-3,3) 
# print("button was pressed,%d"%a)          
# a1.append(a)
# elif self.tt in range (51,101):
# a1=[self.tt]
# if sum(a1) in range (sum(x1), sum(x)):          
# a=random.randint(-3,5)
# print("button was pressed,%d"%a)
# a1.append(a) 
# if sum(a1)>= sum(x):
# mess= QMessageBox.information(self, 'Message', "vi proshli labirint")
# sys.exit(app.exec_())
# elif sum(a1)<= sum(x1):
# mess= QMessageBox.information(self, 'Message', "game over") 
# sys.exit(app.exec_())         
# else:
# mess= QMessageBox.warning(self, 'Ah ti',"zhulie, game over")
# sys.exit(app.exec_())
# event=True  
# else:
# mess= QMessageBox.information(self, 'Message', "you cancel pressing button")
# event=False

# def keyPressEvent(self, e):

# if e.key() == Qt.Key_Escape:
# self.close()

# def closeEvent(self, event):

# reply = QMessageBox.question(self, 'Message',
# "Are you sure to quit?", QMessageBox.Yes |
# QMessageBox.No, QMessageBox.No)
# if reply == QMessageBox.Yes:
# event.accept()
# else:
# event.ignore()
# else:
# if __name__ == '__main__': 
# app = QApplication(sys.argv)
# ex = ikonostasia()
# sys.exit(app.exec_())
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
  bt1.move(30, 300)
  bt2 = QPushButton("middle", self)
  bt2.move(150, 300)        
  bt3 = QPushButton("right", self)
  bt3.move(270, 300)
  bt4 = QPushButton("right", self)
  bt4.move(390, 300)     
  bt1.clicked.connect(self.buttonClicked)
  bt2.clicked.connect(self.buttonClicked)
  bt3.clicked.connect(self.buttonClicked)
  bt4.clicked.connect(self.buttonClicked)
  self.setGeometry(300, 300, 600, 500)
  self.setWindowTitle('Labirintum')
  self.show()

  def paintEvent(self, event):    

    pa = QPainter(self)
    pa.begin(self)
    self.drawRectangles(pa)
    pa.end()

  def drawRectangles(self, pa):

    pa.setBrush(QColor(255,0,0))
    pa.drawRect(10, 25, 185, 250)
    pa.setBrush(QColor(0,255,0))
    pa.drawRect(150, 25, 185, 250)
    pa.setBrush(QColor(0,0,255))
    pa.drawRect(290, 25, 185, 250)
    pa.setBrush(QColor(125,125,125))
    pa.drawRect(330, 25, 185, 250)

  def showDialog(self):

    text, ok = QInputDialog.getText(self, 'Input Dialog', "vvedite koichestvo ochkov do kotorix budete igrat ot 10 do 30 - slojno, ot 31 do 50-normalno, ot 51 do 100-legko:")
    if ok:      
      self.le.setText(text)
      self.tt=int(text)

  def buttonClicked(self, event):

    sender=self.sender
    reply = QMessageBox.question(self, 'Vnimanie!',
    "Are you sure to press button?", QMessageBox.Yes |
    QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
      mess= QMessageBox.information(self, 'Message', "you pressed button")
      while len(x)<self.tt+1:
        x.insert(0,1)
        while len(x1)<self.tt:
          x1.insert(0,-1)
          if self.tt in range (10,101):
            if self.tt in range (10,31):
              a1=[self.tt]
              if sum(a1) in range (sum(x1), sum(x)):
                a=random.randint(-5,3)
                print("button was pressed,%d"%a)        
                a1.append(a)
            elif self.tt in range (31,51):
              a1=[self.tt]
              if sum(a1) in range (sum(x1), sum(x)):
                a=random.randint(-3,3) 
                print("button was pressed,%d"%a)          
                a1.append(a)
            elif self.tt in range (51,101):
              a1=[self.tt]
              if sum(a1) in range (sum(x1), sum(x)):          
                a=random.randint(-3,5)
                print("button was pressed,%d"%a)
                a1.append(a) 
                if sum(a1)>= sum(x):
                  mess= QMessageBox.information(self, 'Message', "vi proshli labirint")
                  sys.exit(app.exec_())
                elif sum(a1)<= sum(x1):
                  mess= QMessageBox.information(self, 'Message', "game over") 
                  sys.exit(app.exec_())         
            else:
              mess= QMessageBox.warning(self, 'Ah ti',"zhulie, game over")
              sys.exit(app.exec_())
              event=True  
          else:
            mess= QMessageBox.information(self, 'Message', "you cancel pressing button")
            event=False

  def center(self):

    screen = QDesktopWidget().screenGeometry()
    size = self.geometry()
    self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2) 

  def closeEvent(self, event):
    reply = QMessageBox.question(self, 'Message',
    "Are you sure to quit?", QMessageBox.Yes |
    QMessageBox.No, QMessageBox.No)
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