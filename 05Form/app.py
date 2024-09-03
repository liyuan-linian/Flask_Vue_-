import flask
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for,flash
from form import UserInfoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "1234567890"

# 通过html表单提交数据 利用request接收数据
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            if username == 'liyuan' and password == '123456':
                return render_template('login.html', messages = "success")
            else:
                return render_template('login.html', messages = "fail")
        else:
            return render_template('login.html', messages = "fail,please enter your username and password")
    else:
        return render_template('login.html')

#上传文件  由于secure原因 上传文件仅保留ascll码
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    path = os.path.join(os.path.dirname(__file__), 'media/upload/')
    if not os.path.exists(path):
        os.makedirs(path)
    if request.method == 'POST':
        file = request.files['myfile']
        if file :
            filename = secure_filename(file.filename)
            file.save(os.path.join(path, filename))
    return render_template('upload.html')

@app.route('/userinfo', methods=['GET', 'POST'])
def userinfo():
    form = UserInfoForm()
    if request.method == 'GET':
        return render_template('userinfo.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            usrname = form.usrname.data
            password = form.password.data
            return redirect('/')
        else:
            return render_template('userinfo.html', form=form)




if __name__ == "__main__":
    app.run(debug=True)