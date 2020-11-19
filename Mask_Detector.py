from PyQt5 import QtCore, QtGui, QtWidgets
import pict_rc
import sys
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img , img_to_array
import numpy as np

model =load_model('model.h5')

def Success_Message(code):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setWindowTitle("Face Mask Detector")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    if code == 0:
    	msg.setText("Error Occurred While Trying To Open Web Camera")
    elif code == 1:
    	msg.setText("Problem In Handling Video")
    else:
    	msg.setIcon(QtWidgets.QMessageBox.Information)
    	msg.setText("Video Saved As 'output.avi' In The Current Directory")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()

def classify_video(code):
	global model
	if not os.path.exists("input"):
		os.makedirs("input")
	img_width , img_height = 150,150

	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	if code == "0":
		try:
			cap = cv2.VideoCapture(0)
			if (cap.isOpened() == False):
				Success_Message(0)
				os.rmtree
				return
		except:
			Success_Message(0)
			return
	else:
		try:
			cap = cv2.VideoCapture(code)
		except:
			Success_Message(1)
			return
	try:
		result = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), int(cap.get(cv2.CAP_PROP_FPS)), (1280,720))

		img_count_full = 0

		font = cv2.FONT_HERSHEY_SIMPLEX
		org = (1,1)
		class_label = ''
		fontScale = 1
		color = (255,0,0)
		thickness = 2

		while True:
			img_count_full += 1
			response , color_img = cap.read()

			if response == False:
				break


			scale = 50
			dim = (1280,720)

			color_img = cv2.resize(color_img, dim ,interpolation= cv2.INTER_AREA)

			gray_img = cv2.cvtColor(color_img,cv2.COLOR_BGR2GRAY)

			faces = face_cascade.detectMultiScale(gray_img, 1.1, 6)

			img_count = 0
			for (x,y,w,h) in faces:
				org = (x-10,y-10)
				img_count += 1
				color_face = color_img[y:y+h,x:x+w]
				cv2.imwrite('input/%d%dface.jpg'%(img_count_full,img_count),color_face)
				img = load_img('input/%d%dface.jpg'%(img_count_full,img_count),target_size=(img_width,img_height))
				img = img_to_array(img)
				img = np.expand_dims(img,axis=0)
				prediction = model.predict(img)


				if prediction==0:
					class_label = "Mask"
					color = (255,0,0)

				else:
					class_label = "No Mask"
					color = (0,255,0)


				cv2.rectangle(color_img,(x,y),(x+w,y+h),(0,0,255),3)
				cv2.putText(color_img, class_label, org, font ,fontScale, color, thickness,cv2.LINE_AA)

			result.write(color_img)
			cv2.imshow('Face mask detection', color_img)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		cap.release()
		result.release()
		cv2.destroyAllWindows()
	except:
		Success_Message(1)
		return
	else:
		Success_Message(2)
		return

def file_opener():
	fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', '',"Video files (*.mp4 *.avi)")
	return fname[0]

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

        self.home_button.clicked.connect(self.go_to_home)
        self.video_button.clicked.connect(self.from_computer)
        self.web_cam.clicked.connect(self.handle_web_camera)

        self.retranslateUi(After_Splash)
        QtCore.QMetaObject.connectSlotsByName(After_Splash)

    def handle_web_camera(self):
    	try:
    		classify_video("0")
    	except:
    		Success_Message(1)

    def from_computer(self):
    	VIDEO_name = file_opener()
    	if VIDEO_name != "":
    		try:
    			classify_video(VIDEO_name)
    		except:
    			Success_Message(1)

    def go_to_home(self):
    	global ui
    	ui.setupUi(SplashScreen)
    	SplashScreen.show()
    	After_Splash.hide()

    def retranslateUi(self, After_Splash):
        _translate = QtCore.QCoreApplication.translate
        After_Splash.setWindowTitle(_translate("After_Splash", "Face Mask Detector | Menu"))
        self.home_button.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Get Back To Home</span></p></body></html>"))
        self.video_button.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Choose Video From Computer</span></p></body></html>"))
        self.web_cam.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Detect From Web Camera</span></p></body></html>"))


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(1280, 720)
        SplashScreen.setMinimumSize(QtCore.QSize(1280, 720))
        SplashScreen.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/Splash_Screen.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.enter_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(490, 610, 321, 91))
        self.enter_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.enter_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.enter_button.setIcon(icon1)
        self.enter_button.setObjectName("enter_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 680, 441, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        SplashScreen.setCentralWidget(self.centralwidget)

        self.enter_button.clicked.connect(self.go_to_menu)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def go_to_menu(self):
    	global ui1
    	ui1.setupUi(After_Splash)
    	After_Splash.show()
    	SplashScreen.hide()

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "Face Mask Detector | Home"))
        self.enter_button.setToolTip(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Get Started</span></p></body></html>"))
        self.label.setToolTip(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Software Developed By Suraj Vijay [INDIA]</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    After_Splash = QtWidgets.QMainWindow()
    ui1 = Ui_After_Splash()

    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    
    SplashScreen.show()
    
    sys.exit(app.exec_())