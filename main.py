import sys
import os
from InstallWindow import InstallWindow
from PyQt5.QtWidgets import QApplicaction
from PyQt5.QtGui import QPixmap

class MainScreen():
    def showSplashScreen(self):
        self.pix=QPixmap("**pendiente de poner imagen")
        self.splassh=QSplashScreen(self.pix,Qt.WindowStaysOnTopHint)
        self.splassh.show()
        


def showSetupWindow():
    mainScreen.splassh.close()
    installWindow.show()
    
def showLoginWindow():
    print("Login")

app=QApplicaction(sys.argv)
mainScreen=MainScreen()
mainScreen.showSplashScreen()
installWindow=InstallWindow()

if os.path.exists("./config.json"):
    QTimer.singleShot(3000,showLoginWindow)
else:
    QTimer.singleShot(3000,showSetupWindow)

sys.exit(app.exec_())