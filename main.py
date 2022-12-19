import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from Ui_untitled import Ui_MainWindow_login
from Ui_sign_up import Ui_MainWindow_signup
from Ui_student import Ui_MainWindow
from Thread_Mysql import Thread_mysql

class log_in(QMainWindow,Ui_MainWindow_login):
    def __init__(self, parent=None):
        super(log_in,self).__init__(parent)
        self.setupUi(self)
        self.login_stu.clicked.connect(self.display_stu)
        self.login_tea.clicked.connect(self.display_tea)
        self.login_sur.clicked.connect(self.display_sur)
        self.signup.clicked.connect(self.switch_to_signup)
        self.show()

    def show_connect_success(self,data):
        self.label_2.setText(data)

    def switch_to_signup(self):
        self.close()
        Sign_up.show()

    def display_stu(self):
        username=self.username_lineEdit.text()
        password=self.password_lineEdit.text()
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


        
class sign_up(QMainWindow,Ui_MainWindow_signup):
    def __init__(self, parent=None):
        super(sign_up,self).__init__(parent)
        self.setupUi(self)
        self.return_to_login.clicked.connect(self.goto_login)
        self.student_pushButton.clicked.connect()
        self.teacher_pushButton.clicked.connect()
        self.surveyor_pushButton.clicked.connect()
    def goto_login(self):
        self.close()
        Log_in.show()

    def sign_stu(self):
        self.label.setText('  两次输入的密码不一致\n             请重试')
        pass
    def sign_tea(self):
        pass
    def sign_sur(self):
        pass
        

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
    

    sys.exit(app.exec_())