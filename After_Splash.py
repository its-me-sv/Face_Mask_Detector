# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'After_Splash.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_After_Splash(object):
    def setupUi(self, After_Splash):
        After_Splash.setObjectName("After_Splash")
        After_Splash.resize(1280, 720)
        After_Splash.setMinimumSize(QtCore.QSize(1280, 720))
        After_Splash.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        After_Splash.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(After_Splash)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Selection_Screen.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.home_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(1164, 610, 71, 91))
        self.home_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.home_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setObjectName("home_button")
        self.video_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.video_button.setGeometry(QtCore.QRect(90, 150, 521, 341))
        self.video_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.video_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.video_button.setText("")
        self.video_button.setIcon(icon1)
        self.video_button.setObjectName("video_button")
        self.web_cam = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.web_cam.setGeometry(QtCore.QRect(760, 110, 361, 421))
        self.web_cam.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.web_cam.setFocusPolicy(QtCore.Qt.NoFocus)
        self.web_cam.setText("")
        self.web_cam.setIcon(icon1)
        self.web_cam.setObjectName("web_cam")
        After_Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(After_Splash)
        QtCore.QMetaObject.connectSlotsByName(After_Splash)

    def retranslateUi(self, After_Splash):
        _translate = QtCore.QCoreApplication.translate
        After_Splash.setWindowTitle(_translate("After_Splash", "Face Mask Detector | Menu"))
        self.home_button.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Get Back To Home</span></p></body></html>"))
        self.video_button.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Choose Video From Computer</span></p></body></html>"))
        self.web_cam.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Detect From Web Camera</span></p></body></html>"))

import pict_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    After_Splash = QtWidgets.QMainWindow()
    ui = Ui_After_Splash()
    ui.setupUi(After_Splash)
    After_Splash.show()
    sys.exit(app.exec_())

