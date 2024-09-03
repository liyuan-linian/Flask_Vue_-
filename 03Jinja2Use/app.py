import flask
from flask import Flask, render_template,flash,url_for,redirect
app = Flask(__name__)
app.secret_key = '1234'

# 可以向jinja模板中传入各种参数，并在html中进行调用，其中变量用{{}}占位 列表与字典通过  list[0] dict.key 实现调用
@app.route('/',methods=['GET','POST'])
def var():
    username = 'liyuan'
    list = [1,2,'3',4,'5']
    dicts = {
        'name' : '123',
        'age' : '26',
        'sex' : 'man'
    }

    return  render_template('var.html',username=username,lists=list,dicts=dicts)

# {%  %} 可以表示模板的语法使用 常见的包括 {% if %} {% endif %} {% elif %}  {% for %} {% endfor %}
# 条件判断的运算符和 python相同 is in 等均可以使用
@app.route('/score/<int:value0>',methods=['GET','POST'])
def score0(value0):
    score = value0
    return render_template('score.html',score=score)

# 循环处理的模板还提供了 loop.index 获取循环次数(loop.index0) loop.first loop.last loop.length 等方法  也可以用loop.cycle 在一个序列中循环取值
@app.route('/forloop',methods=['GET','POST'])
def forloop():
    dict1 = {'书名': 'Flask+Vue.js开发', '价格': 80, '作者': '张三'}
    dict2 = {'书名': 'Python+ChatGPT开发', '价格': 90, '作者': '李四'}
    dict3 = {'书名': 'Django+Vue.js开发', '价格': 100, '作者': '王五'}
    lists = [dict1, dict2, dict3]
    return render_template('index.html', lists=lists)

# 模板过滤器 可以在jinja2 的html模板中对变量进行处理，具体过滤器内容见书本 此外还可以自定义过滤器 过滤器本质上就是一个python函数
@app.template_filter('liyuan_filter')
# 该函数的第一个参数来源于你使用的变量
def liyuan_filter(value,n):
    if len(value) > n :
        return  value[:n]
    else:
        return  value

@app.route('/filter',methods=['GET','POST'])
def filter():
    return render_template('filter.html')

#也可以通过如下装饰器 将函数变为全局函数 可以在jinja模板中直接调用
@app.template_global
def liyuan_filter_global(value,n):
    if len(value) > n :
        return  value[:n]
    else:
        return  value

#jinja2中的模板变量也可分为全局变量与局部变量
#通过如下的装饰器实现全局变量,返回一个字典
@app.context_processor
def global_var():
    user = {
        'name' : 'liyuan',
        'age' : '26'
    }
    return dict(user=user)
# 在jinja中 采用 {{ user.name }} {{ user.age }} 方法调用
#局部变量 在jinja中直接 {{ % set name = 'liyuan' % }} 设置该html文件有效的变量

#模板的继承  采用母版的设计 用jinja语法 {{ % bolck name %}} {{ % endblock %}} 实现分块的设计
@app.route('/module_base',methods=['GET','POST'])
def module_base():
    return  render_template('base.html')

#母版的继承 采用{{ extends "base.html" }} 语法继承相应内容 对于需要改变的内容 在相应block中重写 对于需要继承的内容 {{ super() }} 对于需要调用的内容 {{ self.blockname }}
@app.route('/module_base_1',methods=['GET','POST'])
def moudle_base_1():
    return render_template('base1.html')

#组件的设计 可以通过{{ include "index.html" }}语法引入其他的html设计
@app.route('/module_base_2',methods=['GET','POST'])
def moudle_base_2():
    return render_template('base2.html')

#可以通过 {{ macro funname(arg) }} 语法设置宏 宏本质可以视作一个函数

#通过flash 可以闪现消息 不过要由于flash消息设置与session中故要设置session 此外在jinja中使用get_flashes_messages() 可以实现对flash消息的调用
@app.route('/flash_test',methods=['GET','POST'])
def flash_test():
    flash('flash test!','info')
    return  redirect(url_for('flash_test1'))

@app.route('/flash_test1',methods=['GET','POST'])
def flash_test1():
    flash('a new flash test!','info')
    return render_template('flash.html')


if __name__ == '__main__':
    app.run(debug=True)