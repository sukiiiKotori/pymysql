from PyQt5.QtCore import QThread,pyqtSignal
from remote import Mysql

class Thread_mysql(QThread):
    mysql_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        self.mysql=Mysql()
        self.mysql_signal.emit('远程数据库连接成功！')