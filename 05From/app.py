from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567980'

csrf = CSRFProtect(app)


@app.route('/ajax_login', methods=['GET', 'POST'])
def ajax_login():  # put application's code here
    return render_template('login.html')


@app.route('/ajax_login_data', methods=['GET', 'POST'])
def ajax_login_data():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "liyuan" and password == "123456":
        return jsonify({"code": 200, "msg": "success"})
    else:
        return jsonify({"code": 400, "msg": "fail"})


if __name__ == '__main__':
    app.run()
