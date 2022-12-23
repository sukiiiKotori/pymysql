import pymysql
import datetime
import qrcode
from PIL import Image
from io import BytesIO

class Mysql:
    def __init__(self) :
        self.con = pymysql.Connect(
            host='101.43.243.139',  # mysql的主机ip
            port=3306,  # 端口
            user='root',  # 用户名
            passwd='fyy&pyy',  # 数据库密码
            db='work',  # 数据库名
            charset='utf8',  # 字符集
        )
        self.cursor = self.con.cursor()
        
    def select(self,query:str):
        self.cursor.execute(query)
        print(f"一共查找到：{self.cursor.rowcount}")
        return (self.cursor.rowcount,self.cursor)

    def insert(self,query:str):
        try:
            self.cursor.execute(query)
            self.con.commit()
            return 1
        except:
            return 0

    def insert_for_trigger(self,query:str):
        try:
            self.cursor.execute(query)
            self.con.commit()
            return 'OK'
        except BaseException as e:
            return e.args[1]

    def sign_in_db(self,username:str,password:str):
        pass

    def commit_test(self, sno:str, teid:str, wno:str):
        sql = f'insert into stutest(sno, teid, wno, tetime) values(%s, %s, %s, %s)'
        self.cursor.execute(sql, (sno, teid, wno, datetime.datetime.now()))
        self.con.commit()
    
    def get_test_record(self, wno:str):
        sql = f'select * from stutest where wno = %s'
        self.cursor.execute(sql, wno)
        data = self.cursor.fetchall()
        return data
    
    def get_wname(self, wno:str):
        sql = f'select wname from surveyor where wno = %s'
        self.cursor.execute(sql, wno)
        data = self.cursor.fetchone()
        return data
    
    def commit_testtube(self, teid:str, res:str):
        inres = 0
        if res == '阳性':
            inres = 1
        sql = f'insert into testtube(teid, res) values(%s, %s)'
        self.cursor.execute(sql, (teid, str(inres)))
        self.con.commit()

    def commit_riskarea(self, address:str):
        sql1 = f'select * from riskarea where area = %s'
        self.cursor.execute(sql1, address)
        print(self.cursor.rowcount)
        if self.cursor.rowcount == 1:
            return 0
        else:
            sql2 = f'insert into riskarea values(%s)'
            self.cursor.execute(sql2, address)
            self.con.commit()
            return 1
    
    def remove_riskarea(self, address:str):
        sql1 = f'select * from riskarea where area = %s'
        self.cursor.execute(sql1, address)
        if self.cursor.rowcount == 0:
            return 0
        else:
            sql2 = f'delete from riskarea where area = %s'
            self.cursor.execute(sql2, address)
            self.con.commit()
            return 1

    def code_commit(self, sno: str, state: str, massage: str):
        qr = qrcode.QRCode()
        qr.add_data(massage)
        if state == '健康':
            img = qr.make_image(fill_color='green')
        elif state == '存疑':
            img = qr.make_image(fill_color='yellow')
        else:
            img = qr.make_image(fill_color='red')
        img_byte = BytesIO()
        img.save(img_byte, format='PNG')
        binary = img_byte.getvalue()
        sql1 = f'select * from healthy where sno = %s'
        self.cursor.execute(sql1, sno)
        if self.cursor.rowcount == 0:
            try:
                sql2 = f'insert into healthy values(%s, %s)'
                self.cursor.execute(sql2, (sno, binary))
            except BaseException as e:
                return e.args[1]
        else:
            sql2 = f'update healthy set QRcode = %s where sno = %s'
            self.cursor.execute(sql2, (binary, sno))
        self.con.commit()
        return '提交成功'

    def close(self):
        self.cursor.close()
        self.con.close()

# if __name__ == '__main__':
#     sql = Mysql()
#     # sql.commit_test('1', 'as', '12')
#     # sql.commit_test('2', '2324', '12')
#     # sql.commit_test('3', 'fasdf', '12')
#     sql.get_test_record('12')