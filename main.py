import sys
import time
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5.QtWidgets import QApplication,QPushButton,QFileDialog
from PyQt5.QtCore import *
from PyQt5.Qt import *
from Ui_untitled import Ui_MainWindow_login
from Ui_sign_up import Ui_MainWindow_signup
from Ui_student import Ui_MainWindow
from remote import Mysql

class Thread_mysql(QThread):
    mysql_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        self.mysql=Mysql()
        self.mysql_signal.emit('远程数据库连接成功！')

class log_in(QMainWindow,Ui_MainWindow_login):
    def __init__(self, parent=None):
        super(log_in,self).__init__(parent)
        self.setupUi(self)
        self.login_stu.clicked.connect(self.login_display)
        self.signup.clicked.connect(self.switch_to_signup)
        self.show()

    def show_connect_success(self,data):
        self.label_2.setText(data)

    def login_display(self):
        username=self.username_lineEdit.text()
        password=self.password_lineEdit.text()
<<<<<<< HEAD
        (num,cur)=Thread1.mysql.select('select spassword from student where sno={}'.format(username))
        if num==0:
            self.label_2.setText('        登陆失败！\n账户不存在...请重试')

        else :
            password_fromDB=cur.fetchone()[0]
            if password_fromDB==password:
                self.close()
                Sign_up.show()
            else:
                self.label_2.setText('        登陆失败！\n  密码错误...请重试')

    def display_tea(self):
        username=self.username_lineEdit_2.text()
        password=self.password_lineEdit_2.text()
        (num,cur)=Thread1.mysql.select('select tpassword from teacher where tno={}'.format(username))
        if num==0:
            self.label_2.setText('        登陆失败！\n账户不存在...请重试')

        else :
            password_fromDB=cur.fetchone()[0]
            if password_fromDB==password:
                self.close()
                Sign_up.show()
            else:
                self.label_2.setText('        登陆失败！\n  密码错误...请重试')


    def display_sur(self):
        username=self.username_lineEdit_3.text()
        password=self.password_lineEdit_3.text()
        (num,cur)=Thread1.mysql.select('select supassword from surveyor where wno={}'.format(username))
        if num==0:
            self.label_2.setText('        登陆失败！\n账户不存在...请重试')

        else :
            password_fromDB=cur.fetchone()[0]
            if password_fromDB==password:
                self.close()
                Sign_up.show()
            else:
                self.label_2.setText('        登陆失败！\n  密码错误...请重试')
=======
        password_fromDB=self.Thread1.mysql.select_password(username)
        if password_fromDB==password:
            self.close()
            Sign_up.show()
        else:
            self.label_2.setText('        登陆失败！\n 请检查用户名或密码')
>>>>>>> 4be8371f7f5a1a7b6c9c0fa1aecd41042c030f6f

    def switch_to_signup(self):
        self.close()
        Sign_up.show()



        
class sign_up(QMainWindow,Ui_MainWindow_signup):
    def __init__(self, parent=None):
        super(sign_up,self).__init__(parent)
        self.setupUi(self)
        #self.pushButton_3.clicked.connect()
        

class student(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(student,self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Log_in=log_in()
    Thread1=Thread_mysql()
    Thread1.mysql_signal.connect(Log_in.show_connect_success)
    Thread1.start()
    

    Sign_up=sign_up()
    Student=student()
    
    
    Sign_up.pushButton_3.clicked.connect(
        lambda:{Sign_up.close(), Log_in.show(),}
    )
    sys.exit(app.exec_())