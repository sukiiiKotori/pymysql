import sys
import time
import datetime
from PyQt5.QtWidgets import QMainWindow,QApplication,QHeaderView
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from Ui_untitled import Ui_MainWindow_login
from Ui_sign_up import Ui_MainWindow_signup
from Ui_student import Ui_MainWindow

from Ui_manager import Ui_Manager
from Ui_surveyor import Ui_Form
from Thread_Mysql import Thread_mysql
import json
import datetime


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
                Student.init(username)
                Student.show()
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
        name=self.name_lineEdit_2.text()
        tno=self.tno_lineEdit.text()
        m_cno=self.manage_cno_lineEdit.text()
        password=self.password_lineEdit_2.text()
        password_confirm=self.password_confirm_lineEdit_2.text()
        if password!=password_confirm:
            self.label.setText('  两次输入的密码不一致\n             请重试')
        else:
            query="insert into teacher values ('{}','{}','{}','{}');".format(tno,password,m_cno,name)
            print(query)
            if Thread1.mysql.insert(query) == 1:
                self.label.setText('          注册成功！\n      请返回登陆界面')
            else:
                self.label.setText('          注册失败！\n       该用户已存在')

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
        self.report_button.clicked.connect(lambda:{self.tabWidget.setCurrentIndex(0)})
        self.leave_button.clicked.connect(lambda:{self.tabWidget.setCurrentIndex(1)})
        self.health_button.clicked.connect(lambda:{self.tabWidget.setCurrentIndex(2)})
        self.tube_button.clicked.connect(lambda:{self.tabWidget.setCurrentIndex(3)})
        self.health_show_button.clicked.connect(self.show_health_QRcode)
        self.get_report.clicked.connect(self.report)
        self.get_leave.clicked.connect(self.leave)
        self.get_report_2.clicked.connect(self.history_report)
        self.get_leave_2.clicked.connect(self.history_leave)
        self.tube_button_2.clicked.connect(self.history_test)
        self.init_data()
        self.init_ui()
        self.image.setScaledContents(True)
        self.tableWidget_report.verticalHeader().setVisible(False)
        self.tableWidget_leave.verticalHeader().setVisible(False)
        self.tableWidget_test.verticalHeader().setVisible(False)
        self.tableWidget_report.setColumnWidth(0,162)
        self.tableWidget_report.setColumnWidth(1,162)
        self.tableWidget_report.setColumnWidth(2,241)

        self.tableWidget_leave.setColumnWidth(0,180)
        self.tableWidget_leave.setColumnWidth(1,92)
        self.tableWidget_leave.setColumnWidth(2,200)
        self.tableWidget_leave.setColumnWidth(3,93)

        self.tableWidget_test.setColumnWidth(0,200)
        self.tableWidget_test.setColumnWidth(1,110)
        self.tableWidget_test.setColumnWidth(2,130)
        self.tableWidget_test.setColumnWidth(3,125)

    def init(self,sno:str):
        self.sno=sno
        self.adrress=''
        f=open('temp_QRcode.png','wb')
        sql="select QRcode from healthy where sno='{}'".format(self.sno)
        (num,cur)=Thread1.mysql.select(sql)
        if num==0:
            pass
        else:
            ImageByteStream=cur.fetchone()[0]
            f.write(ImageByteStream)

    def report(self):
        temperature=self.comboBox_tem.currentText()
        add_information=self.textEdit.toPlainText()
        date=datetime.datetime.now().strftime("%Y-%m-%d")
        sql="insert into report values('{}','{}','{}','{}','{}')"
        if self.adrress=='':
            self.label_report_1.setText('             未选择当前位置！')
        else:
            if Thread1.mysql.insert(sql.format(self.sno,date,temperature,self.adrress,add_information)) == 1:
                self.label_report_1.setText('            今日填报提交成功！')
            else:
                self.label_report_1.setText('             今日已提交填报！')
    
    def history_report(self):
        (num,cur)=Thread1.mysql.select("select rtime,rtemp,rarea from report where sno = '{}' order by rtime desc limit 7".format(self.sno))
        i=0
        for row in cur.fetchall():
            row_count=self.tableWidget_report.rowCount()
            self.tableWidget_report.insertRow(row_count)
            for j in range(3):
                self.tableWidget_report.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
            i+=1

    def leave(self):
        date=self.dateTimeEdit.dateTime().toString('yyyy-MM-dd HH:mm')
        time_lenth=self.lineEdit_leave.text()
        sql="insert into _leave_ values('{}','{}','{}','{}','否')"
        if time_lenth=='':
            self.label_leave_1.setText('       未填写请假时长！')
        elif self.address_leave=='':
            self.label_leave_1.setText('       未选择请假去向！')
        else:
            (flag,info)=Thread1.mysql.insert_for_trigger(sql.format(self.sno,date,time_lenth,self.address_leave))
            print(info)
        
    def history_leave(self):
        (_,cur)=Thread1.mysql.select("select date,time_lenth,area,is_approve from _leave_ where sno = '{}' order by date desc".format(self.sno))
        i=0
        for row in cur.fetchall():
            row_count=self.tableWidget_leave.rowCount()
            self.tableWidget_leave.insertRow(row_count)
            self.tableWidget_leave.setItem(i,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget_leave.setItem(i,1,QtWidgets.QTableWidgetItem(str(row[1])+'天'))
            for j in range(2,4):
                self.tableWidget_leave.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
            i+=1

    def history_test(self):
        (num,cur)=Thread1.mysql.select("select tetime,wno,teid from `stutest` where sno='{}' order by tetime desc".format(self.sno))
        i=0
        tid_list=[]
        for row in cur.fetchall():
            row_count=self.tableWidget_test.rowCount()
            self.tableWidget_test.insertRow(row_count)
            tid_list.append(row[2])
            for j in range(3):
                self.tableWidget_test.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
            i+=1
        for row in range(num):
            (num_in,cur_in)=Thread1.mysql.select("select `res` from `testtube` where `teid`='{}'".format(tid_list[row]))
            if num_in==0 :
                self.tableWidget_test.setItem(row, 3, QtWidgets.QTableWidgetItem('结果未出'))
            elif cur_in.fetchone()[0] == 0:
                self.tableWidget_test.setItem(row, 3, QtWidgets.QTableWidgetItem('阴性'))
            else:
                self.tableWidget_test.setItem(row, 3, QtWidgets.QTableWidgetItem('阳性'))
    
    def show_health_QRcode(self):
        self.image.setPixmap(QPixmap('temp_QRcode.png'))

    def init_data(self):
        # 读取json数据
        with open("./data.json", 'r', encoding='utf-8') as data:
            self.data_json = json.loads(data.read())

    def init_ui(self):
        for data in self.data_json:
            self.comboBox_province.addItem(data['Name'])
            self.comboBox_province_2.addItem(data['Name'])

        self.comboBox_province.currentTextChanged.connect(self.slot_province_click)
        self.comboBox_province_2.currentTextChanged.connect(self.slot_province_click_2)

        self.comboBox_city.currentTextChanged.connect(self.slot_city_click)
        self.comboBox_city_2.currentTextChanged.connect(self.slot_city_click_2)

        self.comboBox_county.currentTextChanged.connect(self.slot_county_click)
        self.comboBox_county_2.currentTextChanged.connect(self.slot_county_click_2)

    def slot_province_click(self):
        current_province = self.comboBox_province.currentText()
        if current_province.startswith('--') is False:
            for data in self.data_json:
                if data['Name'] == current_province:
                    self.current_city_data = data['Cities']
                    self.comboBox_city.clear()
                    for c in data['Cities']:
                        self.comboBox_city.addItem(c['Name'])
        else:
            self.comboBox_city.clear()
            self.comboBox_county.clear()
    
    def slot_province_click_2(self):
        current_province = self.comboBox_province_2.currentText()
        if current_province.startswith('--') is False:
            for data in self.data_json:
                if data['Name'] == current_province:
                    self.current_city_data = data['Cities']
                    self.comboBox_city_2.clear()
                    for c in data['Cities']:
                        self.comboBox_city_2.addItem(c['Name'])
        else:
            self.comboBox_city_2.clear()
            self.comboBox_county_2.clear()

    def slot_city_click(self):
        current_city = self.comboBox_city.currentText()
        if current_city.startswith('--') is False:
            for data in self.current_city_data:
                if data['Name'] == current_city:
                    self.comboBox_county.clear()
                    for c in data['Districts']:
                        self.comboBox_county.addItem(c['Name'])

    def slot_city_click_2(self):
        current_city = self.comboBox_city_2.currentText()
        if current_city.startswith('--') is False:
            for data in self.current_city_data:
                if data['Name'] == current_city:
                    self.comboBox_county_2.clear()
                    for c in data['Districts']:
                        self.comboBox_county_2.addItem(c['Name'])

    def slot_county_click(self):
        self.adrress=self.comboBox_province.currentText()+self.comboBox_city.currentText()+self.comboBox_county.currentText()
    def slot_county_click_2(self):
        self.address_leave=self.comboBox_province_2.currentText()+self.comboBox_city_2.currentText()+self.comboBox_county_2.currentText()


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
            mes = Thread1.mysql.commit_test(sno, teid, self.wno)
            self.label_4.setText(mes)
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
            mes = Thread1.mysql.code_commit(sno, state, massage)
            self.label_12.setText(mes)
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
            res = Thread1.mysql.commit_testtube(teid, res)
            self.label_5.setText(res)
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
            flag = Thread1.mysql.commit_riskarea(address)
            if flag == 1:
                self.label_6.setText('       '+str(datetime.datetime.now())+'：提交成功')
            else:
                self.label_6.setText('                            该地区已经被设置为风险地区')
    def remove_riskarea(self):
        if self.comboBox_p2.currentText() == '--请选择省':
            self.label_7.setText('                                     请选择省份信息')
        elif self.comboBox_c2.currentText() == '--请选择市':
            self.label_7.setText('                                     请选择城市信息')
        elif self.comboBox_ct2.currentText() == '--请选择县':
            self.label_7.setText('                                     请选择区县信息')
        else:
            address = self.comboBox_p2.currentText()+self.comboBox_c2.currentText()+self.comboBox_ct2.currentText()
            flag = Thread1.mysql.remove_riskarea(address)
            if flag == 1:
                self.label_7.setText('       '+str(datetime.datetime.now())+'：提交成功')
            else:
                self.label_7.setText('                                     不存在该风险地区')
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
    
    Sign_up=sign_up()
    Student=student()

    surWin = SurMainWindow()
    manWin = ManagerMainWindow()
    

    sys.exit(app.exec_())