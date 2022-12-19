import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from Ui_untitled import Ui_MainWindow_login
from Ui_sign_up import Ui_MainWindow_signup
from Ui_student import Ui_MainWindow
from Thread_Mysql import Thread_mysql
from Ui_manager import Ui_Manager
from Ui_surveyor import Ui_Form
import json
import datetime
from PyQt5 import QtWidgets

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
        (num,cur)=Thread1.mysql.select("select spassword from student where sno='{}'".format(username))
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
        (num,cur)=Thread1.mysql.select("select tpassword from teacher where tno='{}'".format(username))
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
        if username == 'admin' and password == 'admin':
            self.close()
            manWin.show()
        (num,cur)=Thread1.mysql.select("select supassword from surveyor where wno='{}'".format(username))
        if num==0:
            self.label_2.setText('        登陆失败！\n账户不存在...请重试')
        else :
            password_fromDB=cur.fetchone()[0]
            if password_fromDB==password:
                self.close()
                surWin.init(username)
                surWin.show()
            else:
                self.label_2.setText('        登陆失败！\n  密码错误...请重试')


        
class sign_up(QMainWindow,Ui_MainWindow_signup):
    def __init__(self, parent=None):
        super(sign_up,self).__init__(parent)
        self.setupUi(self)
        self.return_to_login.clicked.connect(self.goto_login)
        self.student_pushButton.clicked.connect(self.sign_stu)
        self.teacher_pushButton.clicked.connect(self.sign_tea)
        self.surveyor_pushButton.clicked.connect(self.sign_sur)
    def goto_login(self):
        self.close()
        Log_in.show()

    def sign_stu(self):
        name=self.name_lineEdit.text()
        sno=self.sno_lineEdit.text()
        cno=self.cno_lineEdit.text()
        password=self.password_lineEdit.text()
        password_confirm=self.password_comfirm_lineEdit.text()
        if password!=password_confirm:
            self.label.setText('  两次输入的密码不一致\n             请重试')
        else:
            query="insert into student values ('{}','{}','{}','{}');".format(sno,password,cno,name)
            print(query)
            if Thread1.mysql.insert(query) == 1:
                self.label.setText('          注册成功！\n      请返回登陆界面')
            else:
                self.label.setText('          注册失败！\n       该用户已存在')
        
    def sign_tea(self):
        pass
    def sign_sur(self):
        wname = self.name_lineEdit_3.text()
        wno = self.wno_lineEdit.text()
        password = self.password_lineEdit_3.text()
        password_confirm = self.password_confirm_lineEdit_3.text()
        if password != password_confirm:
            self.label.setText('  两次输入的密码不一致\n             请重试')
        else:
            query="insert into surveyor values ('{}','{}','{}')".format(wno, wname, password)
            if Thread1.mysql.insert(query) == 1:
                self.label.setText('          注册成功！\n      请返回登陆界面')
            else:
                self.label.setText('          注册失败！\n       该用户已存在')
        

class student(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(student,self).__init__(parent)
        self.setupUi(self)

class SurMainWindow(QMainWindow, Ui_Form):
    def __init__(self,parent=None):
        super(SurMainWindow,self).__init__(parent)
        self.setupUi(self)
    def init(self, wno:str):
        self.wno = wno
        self.welcome_massage()
        self.button1.clicked.connect(self.tab_change_0)
        self.button2.clicked.connect(self.tab_change_1)
        self.button3.clicked.connect(self.commit_test)
        self.button4.clicked.connect(self.get_data)
    def tab_change_0(self):
        self.tabWidget.setCurrentIndex(0)
        self.label_4.setText('请输入数据后点击提交')
    def tab_change_1(self):
        self.tabWidget.setCurrentIndex(1)
    def commit_test(self):
        sno = str(self.lineEdit.text())
        teid = str(self.lineEdit_2.text())
        if sno == '':
            self.label_4.setText('请输入学号后再提交！')
        elif teid == '':
            self.label_4.setText('请输入试管编号后再提交！')
        else:
            Thread1.mysql.commit_test(sno, teid, self.wno)
            self.label_4.setText('提交成功！')
            self.lineEdit.clear()
            self.lineEdit_2.clear()
    def get_data(self):
        data = Thread1.mysql.get_test_record(self.wno)
        cur = self.textBrowser.textCursor()
        for line in data:
            text = '学号：' + line[0] + '，试管号：' + line[1] + '，时间：' + str(line[3]) + '\n'
            cur.insertText(text)
        self.textBrowser.setTextCursor(cur)
        self.textBrowser.ensureCursorVisible()
    def welcome_massage(self):
        cur = self.textBrowser_2.textCursor()
        name = Thread1.mysql.get_wname(self.wno)
        name = name[0]
        text = 'Welcome!     ' + str(name)
        cur.insertText(text)
        self.textBrowser_2.setTextCursor(cur)
        self.textBrowser_2.ensureCursorVisible()

class ManagerMainWindow(QMainWindow, Ui_Manager):
    def __init__(self,parent =None):
        super(ManagerMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.set_welcome_massage()
        self.button1.clicked.connect(self.tab_change_0)
        self.button2.clicked.connect(self.tab_change_1)
        self.button3.clicked.connect(self.tab_change_2)
        self.button4.clicked.connect(self.commit_riskarea)
        self.button5.clicked.connect(self.remove_riskarea)
        self.button6.clicked.connect(self.tubecommit)
        self.button7.clicked.connect(self.code_change)
        self.init_data() # 初始化数据
        self.init_ui() # 初始化UI
    def code_change(self):
        sno = self.lineEdit_2.text()
        state = self.comboBox_2.currentText()
        addi = self.lineEdit_3.text()
        if sno == '':
            self.label_12.setText("请输入学号再点击提交！")
        else:
            massage = '学号：' + sno + '\n' + '健康状态：' + state
            if addi != '':
                massage = massage + '\n' + '备注信息：' + addi
            Thread1.mysql.code_commit(sno, massage)
            self.label_12.setText("提交成功！")
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
    def set_welcome_massage(self):
        cur = self.textBrowser.textCursor()
        text = 'Welcome! Manager'
        cur.insertText(text)
        self.textBrowser.setTextCursor(cur)
        self.textBrowser.ensureCursorVisible()
    def tab_change_0(self):
        self.tabWidget.setCurrentIndex(0)
        self.label_12.setText("请输入信息后点击提交")
    def tab_change_1(self):
        self.tabWidget.setCurrentIndex(1)
    def tab_change_2(self):
        self.tabWidget.setCurrentIndex(2)
        self.label_5.setText('请输入数据后点击提交')
    def init_data(self):
        # 读取json数据
        with open("./data.json", 'r', encoding='utf-8') as data:
            self.data_json = json.loads(data.read())
    def tubecommit(self):
        teid = self.lineEdit.text()
        res = self.comboBox.currentText()
        if teid == '':
            self.label_5.setText('请输入试管编号后再提交！')
        else:
            Thread1.mysql.commit_testtube(teid, res)
            self.label_5.setText('提交成功！')
            self.lineEdit.clear()
    def commit_riskarea(self):
        if self.comboBox_p1.currentText() == '--请选择省':
            self.label_6.setText('                                     请选择省份信息')
        elif self.comboBox_c1.currentText() == '--请选择市':
            self.label_6.setText('                                     请选择城市信息')
        elif self.comboBox_ct1.currentText() == '--请选择县':
            self.label_6.setText('                                     请选择区县信息')
        else:
            address = self.comboBox_p1.currentText()+self.comboBox_c1.currentText()+self.comboBox_ct1.currentText()
            Thread1.mysql.commit_riskarea(address)
            self.label_6.setText('       '+str(datetime.datetime.now())+'：提交成功')
    def remove_riskarea(self):
        if self.comboBox_p2.currentText() == '--请选择省':
            self.label_7.setText('                                     请选择省份信息')
        elif self.comboBox_c2.currentText() == '--请选择市':
            self.label_7.setText('                                     请选择城市信息')
        elif self.comboBox_ct2.currentText() == '--请选择县':
            self.label_7.setText('                                     请选择区县信息')
        else:
            address = self.comboBox_p2.currentText()+self.comboBox_c2.currentText()+self.comboBox_ct2.currentText()
            Thread1.mysql.remove_riskarea(address)
            self.label_7.setText('       '+str(datetime.datetime.now())+'：提交成功')
    # 初始化UI
    def init_ui(self):
        # 省选择器
        self.comboBox_p1.addItem("--请选择省")
        self.comboBox_p1.currentTextChanged.connect(self.slot_province_click)
        self.comboBox_p2.addItem("--请选择省")
        self.comboBox_p2.currentTextChanged.connect(self.slot_province_click1)
        for data in self.data_json:
            self.comboBox_p1.addItem(data['Name'])
            self.comboBox_p2.addItem(data['Name'])
        # 市选择器
        self.comboBox_c1.addItem("--请选择市")
        self.comboBox_c1.currentTextChanged.connect(self.slot_city_click)
        self.comboBox_c2.addItem("--请选择市")
        self.comboBox_c2.currentTextChanged.connect(self.slot_city_click1)
        # 县选择器
        self.comboBox_ct1.addItem("--请选择县")
        # self.comboBox_ct1.currentTextChanged.connect(self.slot_county_click)
        self.comboBox_ct2.addItem("--请选择县")
        # self.comboBox_ct2.currentTextChanged.connect(self.slot_county_click1)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.comboBox_p1, 0, 0, 1, 1)
        self.layout.addWidget(self.comboBox_c1, 0, 1, 1, 1)
        self.layout.addWidget(self.comboBox_ct1, 0, 2, 1, 1)
        self.layout.addWidget(self.comboBox_p2, 0, 0, 1, 1)
        self.layout.addWidget(self.comboBox_c2, 0, 1, 1, 1)
        self.layout.addWidget(self.comboBox_ct2, 0, 2, 1, 1)
    # 省选择器点击响应
    def slot_province_click(self):
        current_province = self.comboBox_p1.currentText()
        if current_province.startswith('--') is False:
            for data in self.data_json:
                if data['Name'] == current_province:
                    self.current_city_data = data['Cities']
                    self.comboBox_c1.clear()
                    for c in data['Cities']:
                        self.comboBox_c1.addItem(c['Name'])
        else:
            self.comboBox_c1.clear()
            self.comboBox_ct1.clear()
    # 省选择器点击响应2
    def slot_province_click1(self):
        current_province = self.comboBox_p2.currentText()
        if current_province.startswith('--') is False:
            for data in self.data_json:
                if data['Name'] == current_province:
                    self.current_city_data = data['Cities']
                    self.comboBox_c2.clear()
                    for c in data['Cities']:
                        self.comboBox_c2.addItem(c['Name'])
        else:
            self.comboBox_c2.clear()
            self.comboBox_ct2.clear()
    # 市选择器点击响应
    def slot_city_click(self):
        current_city = self.comboBox_c1.currentText()
        if current_city.startswith('--') is False:
            for data in self.current_city_data:
                if data['Name'] == current_city:
                    self.comboBox_ct1.clear()
                    for c in data['Districts']:
                        self.comboBox_ct1.addItem(c['Name'])
    # 市选择器点击响应2
    def slot_city_click1(self):
        current_city = self.comboBox_c2.currentText()
        if current_city.startswith('--') is False:
            for data in self.current_city_data:
                if data['Name'] == current_city:
                    self.comboBox_ct2.clear()
                    for c in data['Districts']:
                        self.comboBox_ct2.addItem(c['Name'])
            
    # def slot_county_click(self):
    #     self.adrress=self.comboBox_p1.currentText()+self.comboBox_c1.currentText()+self.comboBox_ct1.currentText()
    # def slot_county_click1(self):
    #     self.adrress=self.comboBox_p2.currentText()+self.comboBox_c2.currentText()+self.comboBox_ct2.currentText()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Log_in=log_in()
    Thread1=Thread_mysql()
    Thread1.mysql_signal.connect(Log_in.show_connect_success)
    Thread1.start()
    
    surWin = SurMainWindow()
    manWin = ManagerMainWindow()
    Sign_up=sign_up()
    Student=student()
    

    sys.exit(app.exec_())