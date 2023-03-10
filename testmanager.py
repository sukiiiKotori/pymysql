from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5 import QtWidgets
from Ui_manager import Ui_Manager
import sys
import json
from remote import Mysql
import datetime

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
        self.init_data() # 初始化数据
        self.init_ui() # 初始化UI
    def set_welcome_massage(self):
        cur = self.textBrowser.textCursor()
        text = 'Welcome! Manager'
        cur.insertText(text)
        self.textBrowser.setTextCursor(cur)
        self.textBrowser.ensureCursorVisible()
    def tab_change_0(self):
        self.tabWidget.setCurrentIndex(0)
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
        mysql = Mysql()
        teid = self.lineEdit.text()
        res = self.comboBox.currentText()
        if teid == '':
            self.label_5.setText('请输入试管编号后再提交！')
        else:
            mysql.commit_testtube(teid, res)
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
            mysql = Mysql()
            address = self.comboBox_p1.currentText()+self.comboBox_c1.currentText()+self.comboBox_ct1.currentText()
            mysql.commit_riskarea(address)
            self.label_6.setText('       '+str(datetime.datetime.now())+'：提交成功')
    def remove_riskarea(self):
        if self.comboBox_p2.currentText() == '--请选择省':
            self.label_7.setText('                                     请选择省份信息')
        elif self.comboBox_c2.currentText() == '--请选择市':
            self.label_7.setText('                                     请选择城市信息')
        elif self.comboBox_ct2.currentText() == '--请选择县':
            self.label_7.setText('                                     请选择区县信息')
        else:
            mysql = Mysql()
            address = self.comboBox_p2.currentText()+self.comboBox_c2.currentText()+self.comboBox_ct2.currentText()
            mysql.remove_riskarea(address)
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
    manager = ManagerMainWindow()
    manager.show()
    sys.exit(app.exec_())    