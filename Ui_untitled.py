# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Py\Desktop\vscode\pymysql\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_login(object):
    def setupUi(self, MainWindow_login):
        MainWindow_login.setObjectName("MainWindow_login")
        MainWindow_login.resize(800, 600)
        MainWindow_login.setStyleSheet("background-color:rgb(255, 255, 255)")
        MainWindow_login.setIconSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow_login)
        self.centralwidget.setObjectName("centralwidget")
        self.signup = QtWidgets.QPushButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(50, 490, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.signup.setFont(font)
        self.signup.setStyleSheet("QPushButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(0, 170, 255)\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.signup.setObjectName("signup")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 50, 321, 111))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 18pt \"华文行楷\";")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(160, 170, 491, 251))
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
        self.username_lineEdit = QtWidgets.QLineEdit(self.student)
        self.username_lineEdit.setGeometry(QtCore.QRect(130, 40, 221, 41))
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
        self.password_lineEdit = QtWidgets.QLineEdit(self.student)
        self.password_lineEdit.setGeometry(QtCore.QRect(130, 100, 221, 41))
        self.password_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.login_stu = QtWidgets.QPushButton(self.student)
        self.login_stu.setGeometry(QtCore.QRect(180, 170, 121, 41))
        self.login_stu.setStyleSheet("QPushButton{\n"
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
        self.login_stu.setObjectName("login_stu")
        self.tabWidget.addTab(self.student, "")
        self.teacher = QtWidgets.QWidget()
        self.teacher.setObjectName("teacher")
        self.username_lineEdit_2 = QtWidgets.QLineEdit(self.teacher)
        self.username_lineEdit_2.setGeometry(QtCore.QRect(130, 40, 221, 41))
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
        self.password_lineEdit_2 = QtWidgets.QLineEdit(self.teacher)
        self.password_lineEdit_2.setGeometry(QtCore.QRect(130, 100, 221, 41))
        self.password_lineEdit_2.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit_2.setObjectName("password_lineEdit_2")
        self.login_tea = QtWidgets.QPushButton(self.teacher)
        self.login_tea.setGeometry(QtCore.QRect(180, 170, 121, 41))
        self.login_tea.setStyleSheet("QPushButton{\n"
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
        self.login_tea.setObjectName("login_tea")
        self.tabWidget.addTab(self.teacher, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.username_lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.username_lineEdit_3.setGeometry(QtCore.QRect(130, 40, 221, 41))
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
        self.password_lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.password_lineEdit_3.setGeometry(QtCore.QRect(130, 100, 221, 41))
        self.password_lineEdit_3.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit_3.setObjectName("password_lineEdit_3")
        self.login_sur = QtWidgets.QPushButton(self.tab)
        self.login_sur.setGeometry(QtCore.QRect(180, 170, 121, 41))
        self.login_sur.setStyleSheet("QPushButton{\n"
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
        self.login_sur.setObjectName("login_sur")
        self.tabWidget.addTab(self.tab, "")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 440, 281, 91))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        MainWindow_login.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_login)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_login)

    def retranslateUi(self, MainWindow_login):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_login.setWindowTitle(_translate("MainWindow_login", "校园疫情管理系统V0.1"))
        self.signup.setText(_translate("MainWindow_login", "没有账号？点我注册"))
        self.label.setText(_translate("MainWindow_login", "校园疫情管理系统V0.1"))
        self.username_lineEdit.setPlaceholderText(_translate("MainWindow_login", "学号"))
        self.password_lineEdit.setPlaceholderText(_translate("MainWindow_login", "密码"))
        self.login_stu.setText(_translate("MainWindow_login", "登陆"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student), _translate("MainWindow_login", "    学生登陆   "))
        self.username_lineEdit_2.setPlaceholderText(_translate("MainWindow_login", "工号"))
        self.password_lineEdit_2.setPlaceholderText(_translate("MainWindow_login", "密码"))
        self.login_tea.setText(_translate("MainWindow_login", "登陆"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teacher), _translate("MainWindow_login", "    班主任登陆   "))
        self.username_lineEdit_3.setPlaceholderText(_translate("MainWindow_login", "工号"))
        self.password_lineEdit_3.setPlaceholderText(_translate("MainWindow_login", "密码"))
        self.login_sur.setText(_translate("MainWindow_login", "登陆"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow_login", "核酸检测员登陆"))
        self.label_2.setText(_translate("MainWindow_login", "正在连接远程数据库\n"
"     请耐心等待......"))
