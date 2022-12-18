# coding:utf-8
from PyQt5 import QtWidgets,QtCore
import sys
import json
class Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.setWindowTitle("省市县选择器（test）")
        self.init_data() # 初始化数据
        self.init_ui() # 初始化UI
    # 初始化数据
    def init_data(self):
        # 读取json数据
        with open("./data.json", 'r', encoding='utf-8') as data:
            self.data_json = json.loads(data.read())
    # 初始化UI
    def init_ui(self):
        # 省选择器
        self.province = QtWidgets.QComboBox()
        self.province.addItem("--请选择省")
        self.province.currentTextChanged.connect(self.slot_province_click)
        for data in self.data_json:
            self.province.addItem(data['Name'])
        # 市选择器
        self.city = QtWidgets.QComboBox()
        self.city.addItem("--请选择市")
        self.city.currentTextChanged.connect(self.slot_city_click)
        # 县选择器
        self.county = QtWidgets.QComboBox()
        self.county.addItem("--请选择县")
        self.county.currentTextChanged.connect(self.slot_county_click)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.province, 0, 0, 1, 1)
        self.layout.addWidget(self.city, 0, 1, 1, 1)
        self.layout.addWidget(self.county, 0, 2, 1, 1)
    # 省选择器点击响应
    def slot_province_click(self):
        current_province = self.province.currentText()
        if current_province.startswith('--') is False:
            for data in self.data_json:
                if data['Name'] == current_province:
                    self.current_city_data = data['Cities']
                    self.city.clear()
                    for c in data['Cities']:
                        self.city.addItem(c['Name'])
        else:
            self.city.clear()
            self.county.clear()
    # 市选择器点击响应
    def slot_city_click(self):
        current_city = self.city.currentText()
        if current_city.startswith('--') is False:
            for data in self.current_city_data:
                if data['Name'] == current_city:
                    self.county.clear()
                    for c in data['Districts']:
                        self.county.addItem(c['Name'])
            
    def slot_county_click(self):
        self.adrress=self.province.currentText()+self.city.currentText()+self.county.currentText()

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = Widget()
    gui.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()