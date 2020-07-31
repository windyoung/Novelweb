# !/usr/bin/env python3
# coding=utf-8
'''
@Date: 2020-07-31 16:43:53
@LastEditors: zhujian
@LastEditTime: 2020-07-31 17:06:10
@FilePath: /Novelweb/books_flask/books.py
'''

from pymysql import  connect
from pymysql.cursors import DictCursor
class Book(object):
    def __init__(self):
        self.conn=connect(
            host='127.0.0.1',
            port=23308,
            user='bookweb',
            database='books',
            password='Zxcv1234.',
            charset='utf8'
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
