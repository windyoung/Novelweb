'''
@Date: 2020-07-31 11:13:27
@LastEditors: zhujian
@LastEditTime: 2020-07-31 11:27:22
@FilePath: /Novelweb/books_flask/main.py
'''
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world !'
    
if __name__ =='__main__':
    app.run(port=25000,host='0.0.0.0',debug=True)
    