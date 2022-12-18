# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Py\Desktop\vscode\pymysql\sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_signup(object):
    def setupUi(self, MainWindow_signup):
        MainWindow_signup.setObjectName("MainWindow_signup")
        MainWindow_signup.resize(800, 600)
        MainWindow_signup.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow_signup)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(170, 80, 461, 461))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("\n"
"QTabWidget::pane{\n"
"    border:none;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.student = QtWidgets.QWidget()
        self.student.setObjectName("student")
        self.sno_lineEdit = QtWidgets.QLineEdit(self.student)
        self.sno_lineEdit.setGeometry(QtCore.QRect(120, 100, 221, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.sno_lineEdit.setFont(font)
        self.sno_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.sno_lineEdit.setText("")
        self.sno_lineEdit.setObjectName("sno_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(self.student)
        self.password_lineEdit.setGeometry(QtCore.QRect(120, 220, 221, 41))
        self.password_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_comfirm_lineEdit = QtWidgets.QLineEdit(self.student)
        self.password_comfirm_lineEdit.setGeometry(QtCore.QRect(120, 280, 221, 41))
        self.password_comfirm_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_comfirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_comfirm_lineEdit.setObjectName("password_comfirm_lineEdit")
        self.cno_lineEdit = QtWidgets.QLineEdit(self.student)
        self.cno_lineEdit.setGeometry(QtCore.QRect(120, 160, 221, 41))
        self.cno_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.cno_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cno_lineEdit.setObjectName("cno_lineEdit")
        self.student_pushButton = QtWidgets.QPushButton(self.student)
        self.student_pushButton.setGeometry(QtCore.QRect(170, 350, 121, 41))
        self.student_pushButton.setStyleSheet("QPushButton{\n"
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
        self.student_pushButton.setObjectName("student_pushButton")
        self.username_lineEdit = QtWidgets.QLineEdit(self.student)
        self.username_lineEdit.setGeometry(QtCore.QRect(120, 40, 221, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.username_lineEdit.setText("")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.tabWidget.addTab(self.student, "")
        self.teacher = QtWidgets.QWidget()
        self.teacher.setObjectName("teacher")
        self.tno_lineEdit = QtWidgets.QLineEdit(self.teacher)
        self.tno_lineEdit.setGeometry(QtCore.QRect(120, 100, 221, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tno_lineEdit.setFont(font)
        self.tno_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.tno_lineEdit.setText("")
        self.tno_lineEdit.setObjectName("tno_lineEdit")
        self.password_lineEdit_2 = QtWidgets.QLineEdit(self.teacher)
        self.password_lineEdit_2.setGeometry(QtCore.QRect(120, 220, 221, 41))
        self.password_lineEdit_2.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit_2.setObjectName("password_lineEdit_2")
        self.manage_cno_lineEdit = QtWidgets.QLineEdit(self.teacher)
        self.manage_cno_lineEdit.setGeometry(QtCore.QRect(120, 160, 221, 41))
        self.manage_cno_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.manage_cno_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.manage_cno_lineEdit.setObjectName("manage_cno_lineEdit")
        self.password_confirm_lineEdit_2 = QtWidgets.QLineEdit(self.teacher)
        self.password_confirm_lineEdit_2.setGeometry(QtCore.QRect(120, 280, 221, 41))
        self.password_confirm_lineEdit_2.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_confirm_lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_confirm_lineEdit_2.setObjectName("password_confirm_lineEdit_2")
        self.teacher_pushButton = QtWidgets.QPushButton(self.teacher)
        self.teacher_pushButton.setGeometry(QtCore.QRect(170, 350, 121, 41))
        self.teacher_pushButton.setStyleSheet("QPushButton{\n"
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
        self.teacher_pushButton.setObjectName("teacher_pushButton")
        self.username_lineEdit_2 = QtWidgets.QLineEdit(self.teacher)
        self.username_lineEdit_2.setGeometry(QtCore.QRect(120, 40, 221, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.username_lineEdit_2.setFont(font)
        self.username_lineEdit_2.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.username_lineEdit_2.setText("")
        self.username_lineEdit_2.setObjectName("username_lineEdit_2")
        self.tabWidget.addTab(self.teacher, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.username_lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.username_lineEdit_3.setGeometry(QtCore.QRect(120, 40, 221, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.username_lineEdit_3.setFont(font)
        self.username_lineEdit_3.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.username_lineEdit_3.setText("")
        self.username_lineEdit_3.setObjectName("username_lineEdit_3")
        self.wno_lineEdit = QtWidgets.QLineEdit(self.tab)
        self.wno_lineEdit.setGeometry(QtCore.QRect(120, 100, 221, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.wno_lineEdit.setFont(font)
        self.wno_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.wno_lineEdit.setText("")
        self.wno_lineEdit.setObjectName("wno_lineEdit")
        self.password_lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.password_lineEdit_3.setGeometry(QtCore.QRect(120, 160, 221, 41))
        self.password_lineEdit_3.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit_3.setObjectName("password_lineEdit_3")
        self.password_confirm_lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.password_confirm_lineEdit_3.setGeometry(QtCore.QRect(120, 220, 221, 41))
        self.password_confirm_lineEdit_3.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_confirm_lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_confirm_lineEdit_3.setObjectName("password_confirm_lineEdit_3")
        self.surveyor_pushButton = QtWidgets.QPushButton(self.tab)
        self.surveyor_pushButton.setGeometry(QtCore.QRect(170, 290, 121, 41))
        self.surveyor_pushButton.setStyleSheet("QPushButton{\n"
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
        self.surveyor_pushButton.setObjectName("surveyor_pushButton")
        self.tabWidget.addTab(self.tab, "")
        MainWindow_signup.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_signup)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_signup)

    def retranslateUi(self, MainWindow_signup):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_signup.setWindowTitle(_translate("MainWindow_signup", "注册界面"))
        self.sno_lineEdit.setPlaceholderText(_translate("MainWindow_signup", "学号"))
        self.password_lineEdit.setPlaceholderText(_translate("MainWindow_signup", "密码"))
        self.password_comfirm_lineEdit.setPlaceholderText(_translate("MainWindow_signup", "确认密码"))
        self.cno_lineEdit.setPlaceholderText(_translate("MainWindow_signup", "班号"))
        self.student_pushButton.setText(_translate("MainWindow_signup", "注册"))
        self.username_lineEdit.setPlaceholderText(_translate("MainWindow_signup", "姓名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student), _translate("MainWindow_signup", "   学生注册  "))
        self.tno_lineEdit.setPlaceholderText(_translate("MainWindow_signup", "工号"))
        self.password_lineEdit_2.setPlaceholderText(_translate("MainWindow_signup", "密码"))
        self.manage_cno_lineEdit.setPlaceholderText(_translate("MainWindow_signup", "管理的班级号"))
        self.password_confirm_lineEdit_2.setPlaceholderText(_translate("MainWindow_signup", "确认密码"))
        self.teacher_pushButton.setText(_translate("MainWindow_signup", "注册"))
        self.username_lineEdit_2.setPlaceholderText(_translate("MainWindow_signup", "姓名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teacher), _translate("MainWindow_signup", "  班主任注册  "))
        self.username_lineEdit_3.setPlaceholderText(_translate("MainWindow_signup", "姓名"))
        self.wno_lineEdit.setPlaceholderText(_translate("MainWindow_signup", "工号"))
        self.password_lineEdit_3.setPlaceholderText(_translate("MainWindow_signup", "密码"))
        self.password_confirm_lineEdit_3.setPlaceholderText(_translate("MainWindow_signup", "确认密码"))
        self.surveyor_pushButton.setText(_translate("MainWindow_signup", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow_signup", "核酸检测员注册"))
