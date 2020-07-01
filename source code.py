from tkinter import filedialog, Tk
import shutil
import configparser
import os
import webbrowser
import win32con, win32api
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(485, 433)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.icontext = QtWidgets.QLabel(self.centralwidget)
        self.icontext.setGeometry(QtCore.QRect(40, 125, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.icontext.setFont(font)
        self.icontext.setTabletTracking(False)
        self.icontext.setObjectName("icontext")
        self.foldertext = QtWidgets.QLabel(self.centralwidget)
        self.foldertext.setGeometry(QtCore.QRect(40, 173, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.foldertext.setFont(font)
        self.foldertext.setObjectName("foldertext")
        self.iconbutton = QtWidgets.QPushButton(self.centralwidget)
        self.iconbutton.setGeometry(QtCore.QRect(160, 120, 75, 31))
        self.iconbutton.setObjectName("iconbutton")
        self.folderbutton = QtWidgets.QPushButton(self.centralwidget)
        self.folderbutton.setGeometry(QtCore.QRect(160, 170, 75, 31))
        self.folderbutton.setObjectName("folderbutton")
        self.setbutton = QtWidgets.QPushButton(self.centralwidget)
        self.setbutton.setGeometry(QtCore.QRect(50, 250, 91, 41))
        self.setbutton.setObjectName("setbutton")
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(340, 250, 91, 41))
        self.exitbutton.setObjectName("exitbutton")
        self.icondir = QtWidgets.QLabel(self.centralwidget)
        self.icondir.setGeometry(QtCore.QRect(240, 136, 190, 15))
        self.icondir.setObjectName("icondir")
        self.folderdir = QtWidgets.QLabel(self.centralwidget)
        self.folderdir.setGeometry(QtCore.QRect(240, 185, 190, 15))
        self.folderdir.setObjectName("folderdir")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(30, 20, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(32)
        self.heading.setFont(font)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(180, 260, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setEnabled(True)
        self.status.setGeometry(QtCore.QRect(120, 310, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.status.setFont(font)
        self.status.setText("")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setWordWrap(False)
        self.status.setObjectName("status")
        self.convertbtn = QtWidgets.QPushButton(self.centralwidget)
        self.convertbtn.setGeometry(QtCore.QRect(20, 360, 441, 23))
        self.convertbtn.setObjectName("convertbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCredits = QtWidgets.QMenu(self.menubar)
        self.menuCredits.setObjectName("menuCredits")
        self.menuDonate = QtWidgets.QMenu(self.menubar)
        self.menuDonate.setObjectName("menuDonate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionInstagram = QtWidgets.QAction(MainWindow)
        self.actionInstagram.setObjectName("actionInstagram")
        self.actionGitHub = QtWidgets.QAction(MainWindow)
        self.actionGitHub.setWhatsThis("")
        self.actionGitHub.setObjectName("actionGitHub")
        self.actionDonate = QtWidgets.QAction(MainWindow)
        self.actionDonate.setObjectName("actionDonate")
        self.actionConvert_to_ICON = QtWidgets.QAction(MainWindow)
        self.actionConvert_to_ICON.setObjectName("actionConvert_to_ICON")
        self.actionWebsite = QtWidgets.QAction(MainWindow)
        self.actionWebsite.setObjectName("actionWebsite")
        self.menuFile.addAction(self.actionConvert_to_ICON)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionExit)
        self.menuCredits.addAction(self.actionWebsite)
        self.menuCredits.addSeparator()
        self.menuCredits.addAction(self.actionInstagram)
        self.menuCredits.addAction(self.actionGitHub)
        self.menuDonate.addAction(self.actionDonate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCredits.menuAction())
        self.menubar.addAction(self.menuDonate.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.icontext.setText(_translate("MainWindow", "Select an ICON :"))
        self.foldertext.setText(_translate("MainWindow", "Select A Folder :"))
        self.iconbutton.setText(_translate("MainWindow", "Browse"))
        self.folderbutton.setText(_translate("MainWindow", "Browse"))
        self.setbutton.setText(_translate("MainWindow", "SET ICON"))
        self.exitbutton.setText(_translate("MainWindow", "Exit"))
        self.icondir.setText(_translate("MainWindow", "No File Selected"))
        self.folderdir.setText(_translate("MainWindow", "No Folder Selected"))
        self.heading.setText(_translate("MainWindow", "UNIVERSAL ICON SETTER"))
        self.convertbtn.setText(_translate("MainWindow", "If you don\'t have images with .ico format click here to convet any image to icon"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCredits.setTitle(_translate("MainWindow", "Author"))
        self.menuDonate.setTitle(_translate("MainWindow", "Donate"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit the window"))
        self.actionQuit.setWhatsThis(_translate("MainWindow", "Quit the window"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit"))
        self.actionExit.setWhatsThis(_translate("MainWindow", "Exit"))
        self.actionInstagram.setText(_translate("MainWindow", "Instagram"))
        self.actionInstagram.setStatusTip(_translate("MainWindow", "Visit Developer\'s IG Profile"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub"))
        self.actionGitHub.setStatusTip(_translate("MainWindow", "Visit Developer\'s Github Repository"))
        self.actionDonate.setText(_translate("MainWindow", "Paypal"))
        self.actionConvert_to_ICON.setText(_translate("MainWindow", "Convert to ICON"))
        self.actionWebsite.setText(_translate("MainWindow", "Website"))

        self.setbutton.clicked.connect(self.set)
        self.iconbutton.clicked.connect(self.iconfinder)
        self.folderbutton.clicked.connect(self.foldfinder)
        self.exitbutton.clicked.connect(self.exit)
        self.convertbtn.clicked.connect(self.cnvt)

        self.actionQuit.triggered.connect(self.exit)
        self.actionExit.triggered.connect(self.exit)
        self.actionInstagram.triggered.connect(self.insta)
        self.actionGitHub.triggered.connect(self.git)
        self.actionDonate.triggered.connect(self.pay)
        self.actionConvert_to_ICON.triggered.connect(self.cnvt)
        self.actionWebsite.triggered.connect(self.website)



    def iconfinder(self):
        print("iconfinder")
        self.progressBar.setProperty("value", 0)
        self.icon = filedialog.askopenfilename(initialdir = "/", title="Select a icon", filetypes=[("icon (*.ico)", "*.ico")])
        self.icondir.setText(self.icon)
        self.icondir.adjustSize()

    def foldfinder(self):
        print("folderfinder")
        self.folder = filedialog.askdirectory()
        self.folderdir.setText(self.folder)
        self.folderdir.adjustSize()

    def moveico(self):
        print("moveico", self.icon, self.destico)
        shutil.copy(self.icon, self.destico)

    def hideall(self):
        print("hideall")
        win32api.SetFileAttributes(self.destico, win32con.FILE_ATTRIBUTE_HIDDEN)
        win32api.SetFileAttributes(self.deskfile, win32con.FILE_ATTRIBUTE_HIDDEN)

    def createconfig(self):
            print("createconfig")
            config['.ShellClassInfo'] = {}
            config['.ShellClassInfo']['IconResource'] = 'icon.ico,0'
            with open(self.deskfile, 'w') as confile:
                config.write(confile)
            cmd = 'attrib +s "' + self.folder + '"'
            try:
                os.system('cmd /c ' + cmd)
            except:
                print("config in new mode")
            else:
                os.system(cmd)

    def set(self):
        try:
            self.deskfile = self.folder + '/desktop.ini'
            self.progressBar.setProperty("value", 10)
            self.destico = self.folder + '/icon.ico'
            self.progressBar.setProperty("value", 20)
            self.moveico()
            self.progressBar.setProperty("value", 50)
            self.createconfig()
            self.progressBar.setProperty("value", 80)
            self.hideall()
            self.progressBar.setProperty("value", 100)
        except:
            print("set failed")
            self.status.setText("FAILED")
            self.status.setStyleSheet('color: red')
            self.status.adjustSize()
        else:
            self.status.setText("SUCCESS")
            self.status.setStyleSheet('color: green')
            self.status.adjustSize()
            self.progressBar.setProperty("value", 100)

    def insta(self):
        webbrowser.open("https://www.instagram.com/_u.n__k.n.o.w.n_/")

    def git(self):
        webbrowser.open("https://github.com/rahulps1000")

    def pay(self):
        webbrowser.open("https://www.paypal.me/rahulps1000")

    def cnvt(self):
        webbrowser.open("https://universaliconsetter.000webhostapp.com/convert/index.html")

    def website(self):
        webbrowser.open("https://universaliconsetter.000webhostapp.com/")

    def exit(self):
        self.m.destroy()
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("UNIVERSAL ICON SETTER")
    MainWindow.setWindowIcon(QtGui.QIcon("images/icon.png"))
    m = Tk()
    m.withdraw()
    MainWindow.show()
    config = configparser.RawConfigParser()
    config.optionxform = str
    sys.exit(app.exec_())
