# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\kural\Desktop\pymysql\manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Manager(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(584, 412)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(170, 70, 411, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 411, 321))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button4 = QtWidgets.QPushButton(self.tab_4)
        self.button4.setGeometry(QtCore.QRect(140, 200, 111, 31))
        self.button4.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.button4.setObjectName("button4")
        self.comboBox_ct1 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_ct1.setGeometry(QtCore.QRect(280, 70, 91, 21))
        self.comboBox_ct1.setObjectName("comboBox_ct1")
        self.comboBox_p1 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_p1.setGeometry(QtCore.QRect(70, 70, 101, 21))
        self.comboBox_p1.setObjectName("comboBox_p1")
        self.comboBox_c1 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_c1.setGeometry(QtCore.QRect(180, 70, 91, 21))
        self.comboBox_c1.setObjectName("comboBox_c1")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.button5 = QtWidgets.QPushButton(self.tab_5)
        self.button5.setGeometry(QtCore.QRect(140, 200, 111, 31))
        self.button5.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.button5.setObjectName("button5")
        self.comboBox_p2 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_p2.setGeometry(QtCore.QRect(68, 70, 101, 21))
        self.comboBox_p2.setObjectName("comboBox_p2")
        self.comboBox_c2 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_c2.setGeometry(QtCore.QRect(178, 70, 91, 21))
        self.comboBox_c2.setObjectName("comboBox_c2")
        self.comboBox_ct2 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_ct2.setGeometry(QtCore.QRect(280, 70, 91, 21))
        self.comboBox_ct2.setObjectName("comboBox_ct2")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(30, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(150, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(150, 170, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.button6 = QtWidgets.QPushButton(self.tab_3)
        self.button6.setGeometry(QtCore.QRect(130, 230, 111, 31))
        self.button6.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.button6.setObjectName("button6")
        self.tabWidget.addTab(self.tab_3, "")
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setGeometry(QtCore.QRect(20, 160, 121, 41))
        self.button1.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(Form)
        self.button2.setGeometry(QtCore.QRect(20, 220, 121, 41))
        self.button2.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(Form)
        self.button3.setGeometry(QtCore.QRect(20, 280, 121, 41))
        self.button3.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.button3.setObjectName("button3")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.label_3.setText(_translate("Form", "地区"))
        self.button4.setText(_translate("Form", "提交"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "        添加风险地区        "))
        self.label_4.setText(_translate("Form", "地区"))
        self.button5.setText(_translate("Form", "提交"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "        移除风险地区       "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.label.setText(_translate("Form", "检测管编号"))
        self.label_2.setText(_translate("Form", "检测结果"))
        self.comboBox.setItemText(0, _translate("Form", "阴性"))
        self.comboBox.setItemText(1, _translate("Form", "阳性"))
        self.button6.setText(_translate("Form", "提交"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Tab 3"))
        self.button1.setText(_translate("Form", "健康码处理"))
        self.button2.setText(_translate("Form", "风险地区调整"))
        self.button3.setText(_translate("Form", "核酸结果上传"))