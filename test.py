from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from Ui_surveyor import Ui_Form
import sys
from remote import Mysql

class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self,wno,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.button1.clicked.connect(self.tab_change_0)
        self.button2.clicked.connect(self.tab_change_1)
        self.button3.clicked.connect(lambda:self.commit_test(wno))
        self.button4.clicked.connect(lambda:self.get_data(wno))
    def tab_change_0(self):
        self.tabWidget.setCurrentIndex(0)
        self.label_4.setText('请输入数据后点击提交')
    def tab_change_1(self):
        self.tabWidget.setCurrentIndex(1)
    def commit_test(self, wno:str):
        mysql = Mysql()
        sno = str(self.lineEdit.text())
        teid = str(self.lineEdit_2.text())
        if sno == '':
            self.label_4.setText('请输入学号后再提交！')
        elif teid == '':
            self.label_4.setText('请输入试管编号后再提交！')
        else:
            mysql.commit_test(sno, teid, wno)
            self.label_4.setText('提交成功！')
            self.lineEdit.clear()
            self.lineEdit_2.clear()
    def get_data(self, wno:str):
        mysql = Mysql()
        data = mysql.get_test_record(wno)
        cur = self.textBrowser.textCursor()
        for line in data:
            text = '学号：' + line[0] + '，试管号：' + line[1] + '，时间：' + str(line[3]) + '\n'
            cur.insertText(text)
        self.textBrowser.setTextCursor(cur)
        self.textBrowser.ensureCursorVisible()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow('12')
    myWin.show()
    sys.exit(app.exec_())    