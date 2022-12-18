import pymysql

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
        return self.cursor

    def sign_in_db(self,username:str,password:str):
        pass



    def close(self):
        self.cursor.close()
        self.con.close()

