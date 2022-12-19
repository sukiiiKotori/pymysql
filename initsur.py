from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from Ui_surveyor import Ui_Form
import sys
from remote import Mysql

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
        mysql = Mysql()
        sno = str(self.lineEdit.text())
        teid = str(self.lineEdit_2.text())
        if sno == '':
            self.label_4.setText('请输入学号后再提交！')
        elif teid == '':
            self.label_4.setText('请输入试管编号后再提交！')
        else:
            mysql.commit_test(sno, teid, self.wno)
            self.label_4.setText('提交成功！')
            self.lineEdit.clear()
            self.lineEdit_2.clear()
    def get_data(self):
        mysql = Mysql()
        data = mysql.get_test_record(self.wno)
        cur = self.textBrowser.textCursor()
        for line in data:
            text = '学号：' + line[0] + '，试管号：' + line[1] + '，时间：' + str(line[3]) + '\n'
            cur.insertText(text)
        self.textBrowser.setTextCursor(cur)
        self.textBrowser.ensureCursorVisible()
    def welcome_massage(self):
        cur = self.textBrowser_2.textCursor()
        mysql = Mysql()
        name = mysql.get_wname(self.wno)
        name = name[0]
        text = 'Welcome!     ' + str(name)
        cur.insertText(text)
        self.textBrowser.setTextCursor(cur)
        self.textBrowser.ensureCursorVisible()

# test
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     surWin = SurMainWindow('12')
#     surWin.show()
#     sys.exit(app.exec_())    