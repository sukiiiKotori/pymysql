from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5 import QtWidgets
from Ui_manager import Ui_Manager
import sys
import json

class ManagerMainWindow(QMainWindow, Ui_Manager):
    def __init__(self,parent =None):
        super(ManagerMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.button1.clicked.connect(self.tab_change_0)
        self.button2.clicked.connect(self.tab_change_1)
        self.button3.clicked.connect(self.tab_change_2)
        self.init_data() # 初始化数据
        self.init_ui() # 初始化UI
    def tab_change_0(self):
        self.tabWidget.setCurrentIndex(0)
    def tab_change_1(self):
        self.tabWidget.setCurrentIndex(1)
    def tab_change_2(self):
        self.tabWidget.setCurrentIndex(2)
    def init_data(self):
        # 读取json数据
        with open("./data.json", 'r', encoding='utf-8') as data:
            self.data_json = json.loads(data.read())
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
        self.comboBox_ct1.currentTextChanged.connect(self.slot_county_click)
        self.comboBox_ct2.addItem("--请选择县")
        self.comboBox_ct2.currentTextChanged.connect(self.slot_county_click1)
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
            
    def slot_county_click(self):
        self.adrress=self.comboBox_p1.currentText()+self.comboBox_c1.currentText()+self.comboBox_ct1.currentText()
    def slot_county_click1(self):
        self.adrress=self.comboBox_p2.currentText()+self.comboBox_c2.currentText()+self.comboBox_ct2.currentText()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = ManagerMainWindow()
    manager.show()
    sys.exit(app.exec_())    