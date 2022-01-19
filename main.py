import sys
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('browsers.ui',self)

        self.creds = None
        self.default = False
        self.p = None
        self.output.setFont(QFont('Arial', 18))
        
        self.profile_btn.clicked.connect(self.browslogins)
        self.key_btn.clicked.connect(self.browskey)
        self.default_locations.clicked.connect(self.default_func)
        self.crack.clicked.connect(self.check)
        self.info_btn.clicked.connect(self.show_info)

    def default_func(self):
        self.default = True
        self.default_locations.setStyleSheet("background-color: #28F23C")

    def check(self):
        if self.default == True:
            self.backend()
            self.default == None
            self.default_locations.setStyleSheet("background-color: white")
            self.output.setText(self.p.stdout)
            self.progressBar.setValue(100)
        elif self.default == False:
            if not self.logins.text() or not self.key.text():
                dialog = QMessageBox()
                dialog.setText('Select Logins and key file')
                dialog.setWindowTitle('Error')
                dialog.setIcon(QMessageBox.Critical)
                dialog.exec_()
            else:
                self.backend2()
                self.default == None
                self.default_locations.setStyleSheet("background-color: white")
                self.output.setText(self.p.stdout)
                self.progressBar.setValue(100)

    def backend(self):
        if self.btn1.isChecked():
            self.p=subprocess.run('backend.exe -b chrome',shell=True,stdout=subprocess.PIPE,text=True)
        elif self.btn2.isChecked():
            self.p=subprocess.run('backend.exe -b firefox',shell=True,stdout=subprocess.PIPE,text=True)
        elif self.btn3.isChecked():
            self.p=subprocess.run('backend.exe -b edge',shell=True,stdout=subprocess.PIPE,text=True)
        elif self.btn4.isChecked():
            self.p=subprocess.run('backend.exe -b opera',shell=True,stdout=subprocess.PIPE,text=True)
        elif self.btn5.isChecked():
            self.p=subprocess.run('backend.exe -b brave',shell=True,stdout=subprocess.PIPE,text=True)

    def backend2(self):
        profile = self.profile_btn.text()
        key = self.key_btn.text()

        if self.btn1.isChecked():
            self.p=subprocess.run(f'backend.exe -b chrome -p {profile} -k {key}',shell=True,stdout=subprocess.PIPE,text=True)
        elif self.btn2.isChecked():
            self.p=subprocess.run(f'backend.exe -b firefox -p {profile} -k {key}',shell=True,stdout=subprocess.PIPE,text=True)
        elif self.btn3.isChecked():
            self.p=subprocess.run(f'backend.exe -b edge -p {profile} -k {key}',shell=True,stdout=subprocess.PIPE,text=True)
        elif self.btn4.isChecked():
            self.p=subprocess.run(f'backend.exe -b opera -p {profile} -k {key}',shell=True,stdout=subprocess.PIPE,text=True)
        elif self.btn5.isChecked():
            self.p=subprocess.run(f'backend.exe -b brave -p {profile} -k {key}',shell=True,stdout=subprocess.PIPE,text=True)

    def browslogins(self):
        fname = QFileDialog.getOpenFileName(self, 'Select File', 'C:\\')
        self.logins.setText(fname[0])

    def browskey(self):
        fname = QFileDialog.getOpenFileName(self, 'Select File', 'C:\\')
        self.key.setText(fname[0])

    def show_info(self):
        info = QMessageBox()
        info.setText('https://github.com/moonD4rk/HackBrowserData')
        info.setWindowTitle('INFO')
        info.setIcon(QMessageBox.Information)
        info.exec_()

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedSize(1116, 765)
widget.setWindowTitle('PwnBrowser')
widget.setWindowIcon(QIcon('icons/appicon.png'))
widget.show()
sys.exit(app.exec_())