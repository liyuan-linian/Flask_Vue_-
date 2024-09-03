from xml.dom import ValidationErr

from wtforms import StringField, PasswordField, IntegerField, widgets, SelectField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import Length, DataRequired, NumberRange, EqualTo


class UserInfoForm(FlaskForm):
    # StringField 文本字段 用于字符串输入
    # label 字段的标签名称 就是这个框子的名字， validators 验证器字段 表示对输入内容 进行验证
    # render_kw 表示应用于该元素的ccs样式
    # 更多字段和验证器见书p99
    username = StringField(label='usrname',
                          validators=[DataRequired(message='用户名不能为空'),
                                      Length(min=2, max=20, message="用户名称长度在6-30位之间"),
                                      ],
                          render_kw={'class': 'form-control', 'placeholder': "请输入用户名称"})
    # PasswordField 也属于密码文本字段
    password = PasswordField(label='password',
                           validators=[DataRequired(message='密码不能为空'),
                                       Length(min=2, max=30, message="用户密码长度需要在6-30位之间")],
                           render_kw={'class': 'form-control', 'placeholder': "请输入用户密码"})
    # widget 一个用于覆盖html标签样式的部件（没理解） equalto验证器可以比较两个字段的植
    password_repeat = PasswordField(label="再次输入密码",
                                    validators=[Length(6, 30, message="6-30位"),
                                                EqualTo("password", message="两次密码输入不一致")],
                                    widget=widgets.PasswordInput())
    # IntegerField
    age = IntegerField(label='age', default=1,
                       validators=[NumberRange(min=1, max=100, message='1~100')],
                       render_kw={'class': 'form-control'})
    #
    mobile = StringField(label='手机号码',
                         validators=[DataRequired(message="手机不能为空"),
                                     Length(min=11, max=11, message="手机号码为11位")],
                         render_kw={'class': 'form-control', 'placeholder': "请输入手机号码"})
    #choice 字段是一个可以下拉选择的菜单选项 并绑定数据,以列表的形式
    #SelectField 可以在下拉选矿中选择一个
    status = [("-1", "请选择"), ("0", "正常"), ("1", "无效")]
    user_status = SelectField(label='status',
                             validators=[DataRequired(message='用户状态不能为空')],
                             choices=status)
    submit = SubmitField(label='submit')

    # 可以自定义验证器 通常正则
    def validate_mobile(self, value):
        if value > 0:
            pass
        else:
            raise ValidationErr('error')