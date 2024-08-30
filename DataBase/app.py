import os
from email.policy import default
from lib2to3.fixes.fix_input import context

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import distinct, func, and_, or_, not_
from flask import Flask
from datetime import datetime

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True

# flask 中所有的模型必须继承于model类
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.Integer, nullable=False, default=0)
    age = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=0)
    createdate = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"{self.id},{self.username}"


# 还没研究懂 总之是flask的一个上下文机制导致
app.app_context().push()

db.drop_all()
db.create_all()

# 新增数据
usr1 = User(username='liyuan', password='123456', sex=0, age=23, status=0, createdate=datetime.now())
db.session.add(usr1)  # 多条数据可以使用 db.session.add_all([ ])
db.session.commit()

# 查询数据 可以基于 query 或者 session对象 查询

# all() 查询所有数据  返回一个list 其中每一项都是一个dict
usr_find_all = db.session.query(User).all()
usr_find_all = User.query.all()
print(usr_find_all)
print(usr_find_all[0].username)

# get() 查询单条数据  根据主键
usr_find_get = User.query.get(1)

# with_entities() 可以给定字段查询
usr_find_entities = User.query.with_entities(User.username, User.password).all()
print(usr_find_entities)

# filter_by() 实现精确过滤  filter()实现条件过滤  此外可以通过逻辑表达式
usr_filter_by = User.query.filter_by(username="liyuan")
print(usr_filter_by)
usr_filter = User.query.filter(User.age > 18)
print(usr_filter)

usr_filter_and = User.query.filter(and_(User.age > 18, User.age == 0, User.username.contains('li'))).all()

# distinct() 去重
usr_distinct = db.session.query(User.username).distinct().all()
usr_distinct = User.query.with_entities(distinct(User.username)).all()

# order_by() 排序 默认按主键排序 可以指定其余排序
# groub_by() 分组查询

# 在查询中 调用函数 根据不同调换func后的函数即可
res = db.session.query(func.count(User.id)).scalar()

# limit() 返回前n条记录 offset() 表示从第几天数据开始取（跳过前n条数据）
# 此外 通过session方式 可以实现对多个数据table进行查询

# 数据修改 通过查询方式或者 update()方式
usr = User.query.get(1)
usr.username = 'liyuan123'
db.session.commit()

User.query.filter(User.age > 10).update({User.status : 1})
db.session.commit()

#数据删除
usr = User.query.get(1)
db.session.delete(usr)
db.session.commit()

usr = User.query.filter(User.age > 10).delete()
db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
