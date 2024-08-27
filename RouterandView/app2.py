from flask import Flask,request,render_template,make_response,session,redirect,url_for,abort,jsonify
from flask.views import MethodView
app = Flask(__name__)
app.secret_key = '123456'
#request对象参数
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        print("url is" + request.url)
        print("base_url is" + request.base_url)
        print("host url is" + request.host_url)
        print('path is' + request.path)
        print('headers is' + str(request.headers))
        print('cookies is' + str(request.cookies))
        print('......')
    return '0.0'

#
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        print('请求方式' + request.method)
        print("form " + str(request.form))
        print("form " + request.form["username"])
        print("form " + request.form.get("password"))
        return '1.1.1'

#response 对象实验 ,此外该方法也可返回渲染模板
@app.route('/index2',methods=['GET','POST'])
def index2():
    """
    temp = render_template("index2.html")
    re = make_response(temp,200)
    :return:
    """
    re = make_response("hello flask")
    re.mimetype = "text/plain"
    print(re.data)
    print(re.content_type)
    print(re.status_code)
    print(re.headers)
    return re

#cookie
@app.route('/set_cookie',methods=['GET','POST'])
def set_cookie():
    re = make_response("cokkie test")
    re.set_cookie("usrname","liyuan")
    re.set_cookie("password","123456",max_age=120)
    print(re.headers)
    return re
@app.route('/get_cookie',methods=['GET','POST'])
def get_cookie():
    re = request.cookies.get("usrname")
    print(re)

    return re
@app.route('/del_cookie',methods=['GET','POST'])
def del_cookie():
    re = make_response("del")
    re.delete_cookie("password")
    print(re.headers)

#session
@app.route('/index3',methods=['GET','POST'])
def index3():
    if 'username' in session:
        username = session.get('username')
        return '用户名:' + username + '<br>' + "<b><a href = '/logout1'>点击注销</a></b>"  # 对应/logout
    return "未登录， <br><a href = '/login1'></b>" + "点击登录</b></a>"  # 对应/login

@app.route('/login1',methods=['GET','POST'])
def login1():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
       <form action = "" method = "post">
          <p><input type ="text" name ="username"/></p>
          <p><input type ="submit" value ="登录"/></p>
       </form>
       '''
@app.route('/logout1',methods=['GET','POST'])
def logout1():
    session.pop('username',None)
    return redirect(url_for('index3'))

#试图处理函数 页面渲染
@app.route('/index4',methods=['GET','POST'])
def index4():
    data = {'name': 'liyuan','age': 23}
    return render_template('var.html',**data)
# 重定向 flask.redirect(location,code=302,Respone=None)

# abort 终止函数执行
@app.route('/test/<int:value>')
def test(value):
    if value < 10:
        abort(400)
    return f"error : {value}"

#自定义404
@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('404.html')

#返回json
@app.route('/data')
def get_data():
    data = {
        'name': 'liyuan',
        'age': 23,
        'sex': 'man'
    }
    return jsonify(data)

#视图类 methodview 可用于处理一类相同的请求方法
class UserView(MethodView):
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

usr_view = UserView.as_view('user')
app.add_url_rule('/user',view_func=usr_view,methods=['GET','POST'])

if __name__ == '__main__':
    app.run(debug=True)