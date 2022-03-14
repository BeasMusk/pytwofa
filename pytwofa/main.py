from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from pytwofaui import Ui_pyTwoFa

import os.path
import sys
import pyotp


class MainUI(QWidget):
    def __init__(self):
        super(MainUI, self).__init__()

        self.uiPyTwoFa = Ui_pyTwoFa()
        self.uiPyTwoFa.setupUi(self)

        self.uiPyTwoFa.pbOk.clicked.connect(self.pbClicked)

        if os.path.exists("config.txt"):
            f = open("config.txt", "r")
            while True:
                line = f.readline().strip()
                if not line:
                    break
                self.uiPyTwoFa.cbStr.addItem(line)

    def pbClicked(self):
        getStr = self.uiPyTwoFa.cbStr.currentText()

        if ':' in getStr:
            getStr = getStr.split(':')[1]

        if getStr:
            try:
                totp = pyotp.TOTP(getStr)
                result = totp.now()
                self.uiPyTwoFa.teOutput.setHtml(
                    '<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">{'
                    '0}</span></p></body></html>'.format(result))
            except Exception as e:
                self.uiPyTwoFa.teOutput.setHtml(
                    '<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">{'
                    '0}</span></p></body></html>'.format(str(e)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = MainUI()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
