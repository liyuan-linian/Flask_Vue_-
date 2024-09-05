import flask
from flask import Flask,render_template

#templates 用于放置html文件  static 用于img css js 文件
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='static')

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)