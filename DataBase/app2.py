import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
# 数据库 事务
base_dir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(base_dir,'data1.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_COMMIT_TEARDOWN']=True
db=SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    sex=db.Column(db.Integer,nullable=False,default=0)
    age = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False,default=0)
    createdate=db.Column(db.DateTime,nullable=False,server_default=text('CURRENT_TIMESTAMP'))

    def __repr__(self):
        return f"{self.id},{self.username}"

@app.route("/test")
def test():
    try:
        # 开始事务
        db.session.begin()
        # 执行一系列数据库操作
        user1 = User(username="test1", password="123456", age=35, status=1)
        db.session.add(user1)

        user2 = User(username="test2", age=35, status=1)
        db.session.add(user2)

        # 提交事务
        db.session.commit()
        return "事务执行成功"
    except Exception as e:
        # 回滚事务
        db.session.rollback()
        print(e)
        return "事务执行失败"
        raise e
#db.drop_all()
#db.create_all()
if __name__=="__main__":
    app.run()


