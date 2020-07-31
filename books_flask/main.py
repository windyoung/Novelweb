# !/usr/bin/env python3
# coding=utf-8

'''
@Date: 2020-07-31 11:13:27
@LastEditors: zhujian
@LastEditTime: 2020-07-31 17:13:37
@FilePath: /Novelweb/books_flask/main.py
'''


from flask import Flask
from books import Book 
"""
接口说明:
1,返回是json数据
2,,结构如下 
{
    rescode:0,#非0即错误 1 
    datadata: #数据位置一般为数组
    message:'对本次请求的说明'
}
"""
app=Flask(__name__)
app.config['JSON_AS_ASCII']=False

@app.route('/')
def hello_world():
    book = Book()
    res = book.get_books_infos_limit()
    return 'hello world ! \n {}'.format(res)
    
if __name__ =='__main__':
    app.run(port=25000,host='0.0.0.0',debug=True)

    