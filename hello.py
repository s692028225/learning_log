from flask import Flask,render_template,flash
from search_letter import search_letter
import json

app = Flask(__name__)
app.secret_key = 'this is a secret key'
@app.route('/')
def hello():
    string = {'name':'bob','gender':'male','age':21}
    li = [1,2,3,4,5]
    flash('message')
    return render_template('entry.html',string = string,li = li)

''' 
flask路由是由装饰器实现的
默认以get方式发送，其他方式需要用methods方式定义后才行
'''
@app.route('/search',methods=['GET','POST'])

def search():
    contents = search_letter('lit this building')
    #只能return字符串
    return json.dumps(contents)

@app.route('/entry')
def entry():
    return render_template('entry.html',the_title='hello html')

@app.route('/order/<int:order_id>')
def get_order_id(order_id):
    return 'order_id is {}'.format(order_id)

app.run(debug= True)

