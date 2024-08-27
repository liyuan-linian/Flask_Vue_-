from flask import Flask ,url_for

app = Flask(__name__)

#基本的路由绑定
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

#同一视图函数可以使用不同的路由，即不同的路由可以指向同一试图函数
@app.route('/index')
@app.route('/flask')
def hello():
    return '可以将不同路由绑定至同一试图函数中'

#通过这种方法 可以随时改变路由下的视图函数
def hello2():
    return '不采用装饰器的动态路由绑定'
app.add_url_rule('/hello',view_func=hello2)

#可以使用带参数的试图函数处理 多个同类请求 相当于把多个id的路由绑到一起去
#<>参数支持五种类型转化
@app.route('/book/<id>')
def showBook(id):
    return 'book id'

#采用url_for函数 可以动态获得指向某函数的路由地址
@app.route('/get_url')
def show_url():
    url1 = url_for('hello') #只能解析到最下面一层
    url2 = url_for('hello2')
    url3 = url_for('showBook',id=1)

    return f" 复数路由解析 '{url1}' 单一路由解析 '{url2}' 动态路由解析 '{url3}'"

#用这种方法查看所有路由规则
print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
