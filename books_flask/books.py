# !/usr/bin/env python3
# coding=utf-8
'''
@Date: 2020-07-31 16:43:53
@LastEditors: zhujian
@LastEditTime: 2020-07-31 17:21:38
@FilePath: /Novelweb/books_flask/books.py
'''

from pymysql import  connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_DATABASE,MYSQL_PASSWORD,MYSQL_CHARSET
class Book(object):
    def __init__(self):
        self.conn=connect(
            host=MYSQL_HOST,
            port=int(MYSQL_PORT.encode('utf-8').decode()),
            user=MYSQL_USER,
            database=MYSQL_DATABASE,
            password=MYSQL_PASSWORD,
            charset=MYSQL_CHARSET
            )
        self.cursor=self.conn.cursor(DictCursor)
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    def get_books_infos_limit(self):
        sql='select * from book_infos limit 3 '
        self.cursor.execute(sql)
        data=[]
        for tmp in self.cursor.fetchall():
            print(tmp)
            data.append(tmp)
        return data
