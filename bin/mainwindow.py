# -*- coding: utf-8 -*-
#python3
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
# Developed by Raveen S Rathnayake
# Updated on 2017-05-20

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    """
    setting up the labels and the interface of the display
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 513)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(380, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.firstName = QtWidgets.QLabel(self.centralWidget)
        self.firstName.setGeometry(QtCore.QRect(210, 170, 381, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.firstName.setFont(font)
        self.firstName.setAlignment(QtCore.Qt.AlignCenter)
        self.firstName.setObjectName("firstName")
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(310, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.shopName = QtWidgets.QLabel(self.centralWidget)
        self.shopName.setGeometry(QtCore.QRect(290, 220, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.shopName.setFont(font)
        self.shopName.setAlignment(QtCore.Qt.AlignCenter)
        self.shopName.setObjectName("shopName")
        self.label3 = QtWidgets.QLabel(self.centralWidget)
        self.label3.setGeometry(QtCore.QRect(370, 250, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label3.setFont(font)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.itemName = QtWidgets.QLabel(self.centralWidget)
        self.itemName.setGeometry(QtCore.QRect(220, 280, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.itemName.setFont(font)
        self.itemName.setAlignment(QtCore.Qt.AlignCenter)
        self.itemName.setObjectName("itemName")
        self.lblPicture = QtWidgets.QLabel(self.centralWidget)
        self.lblPicture.setGeometry(QtCore.QRect(350, 30, 100, 100))
        self.lblPicture.setText("")
        self.lblPicture.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop) #QtCore.Qt.AlignCenter
        self.lblPicture.setObjectName("lblPicture")
        self.lblProdPic = QtWidgets.QLabel(self.centralWidget)
        self.lblProdPic.setGeometry(QtCore.QRect(350, 310, 100, 100))
        self.lblProdPic.setText("")
        self.lblProdPic.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblProdPic.setObjectName("lblProdPic")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(180, 0, 20, 441))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(610, 0, 20, 441))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setGeometry(QtCore.QRect(190, -10, 431, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(190, 430, 431, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 864, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuSmart_Billboard_System = QtWidgets.QMenu(self.menuBar)
        self.menuSmart_Billboard_System.setObjectName("menuSmart_Billboard_System")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuSmart_Billboard_System.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Hi!</span></p></body></html>"))
        self.firstName.setText(_translate("MainWindow", "Person first name"))
        self.label2.setText(_translate("MainWindow", "please visit our store"))
        self.shopName.setText(_translate("MainWindow", "shopName"))
        self.label3.setText(_translate("MainWindow", "to buy"))
        self.itemName.setText(_translate("MainWindow", "itemNo"))
        self.menuSmart_Billboard_System.setTitle(_translate("MainWindow", "Smart Billboard System"))

    """Updates the labels when a new customer has arrived near to the display
    self: this object
    cusName: Name of the new customer
    shopName: Name of the Shop
    item:the matching item
    pixmap1: the profile picture of the customer
    pixmap2: the picture of the item(which matches with the shop item and the  customer wishlist item)
    """
    def updateLabelsUI(self,cusName,shopName,item,pixmap1,pixmap2):
        self.label1.setText("Hi")
        self.firstName.setText(cusName)
        self.label2.setText("please visit")
        self.shopName.setText(shopName)
        self.label3.setText("to buy")
        self.itemName.setText(item)
        self.lblPicture.setPixmap(pixmap1)
        self.lblProdPic.setPixmap(pixmap2)

    """Display nothing if no new customer is near by the display
    self:this object
    """
    def displayNone(self):
        self.label1.setText("")
        self.firstName.setText("")
        self.label2.setText("")
        self.shopName.setText("")
        self.label3.setText("")
        self.itemName.setText("")
        self.lblPicture.setText(" ")
        self.lblProdPic.setText(" ")
