# !/usr/bin/env python3
# coding=utf-8

'''
@Date: 2020-07-31 11:13:27
LastEditors: zhujian
LastEditTime: 2020-08-26 05:46:48
FilePath: /Novelweb/books_flask/main.py
'''
from flask import Flask, jsonify
from books import Book
"""
接口说明:
1,返回是json数据
2,,结构如下
{
    "rescode":0,#非0即错误 1
    "data": #数据位置一般为数组
    "message":'对本次请求的说明'
}
"""
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/books_cates', methods=['GET'])
def get_books_cates():
    resData = {"rescode": 0,
               "data": [{"id": 0, "text": "首页", "url": "/"},
                        {"id": 1, "text": "玄幻", "url": "/xuanhuan"},
                        {"id": 2, "text": "修真", "url": "/xiuzhen"},
                        {"id": 3, "text": "都市", "url": "/dushi"},
                        {"id": 4, "text": "历史", "url": "/lishi"},
                        {"id": 5, "text": "网游", "url": "/wangyou"},
                        {"id": 6, "text": "科幻", "url": "/kehuan"},
                        {"id": 7, "text": "言情", "url": "/yanqing"},
                        {"id": 8, "text": "校园", "url": "/xiaoyuan"},
                        {"id": 9, "text": "其他", "url": "/qita"},
                        {"id": 10, "text": "完本", "url": "/wanben"}],
               "message": "对本次请求的说明"
               }
    return jsonify(resData)


@ app.route('/')
def hello_world():
    book = Book()
    res = book.get_books_infos_limit()
    return 'hello world ! \n {}'.format(res)


if __name__ == '__main__':
    app.run(port=25000, host='0.0.0.0', debug=True)
