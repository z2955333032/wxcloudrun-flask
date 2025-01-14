from datetime import datetime

from wxcloudrun import db
#数据库对应的模型

# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())

class JDF33(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'jdf33'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    xm = db.Column(db.String(12))
    pic1=db.Column(db.String(10))
    _updateTime = db.Column(db.String(10))
    sfzhm = db.Column(db.String(99))
    qmpic=db.Column(db.String(99))

class USER(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'user'
    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(12))
    pw = db.Column(db.String(12))
    ssq = db.Column(db.String(12))


class JDF(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'jdf'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    xm = db.Column(db.String(99),index=True)
    xb = db.Column(db.String(99))
    csny = db.Column(db.String(99))
    sfzhm = db.Column(db.String(99),index=True)
    hk = db.Column(db.String(99))
    sjhm = db.Column(db.String(99))
    cjzhm = db.Column(db.String(99))
    jtzz = db.Column(db.String(99))
    jhrxm = db.Column(db.String(99))
    jhrzz = db.Column(db.String(99))
    jtjjqk = db.Column(db.String(99))
    cjlb = db.Column(db.String(99))
    cjdj = db.Column(db.String(99))
    sqxm = db.Column(db.String(99))
    pic0 = db.Column(db.String(99))
    pic1 = db.Column(db.String(99))
    pic2 = db.Column(db.String(99))
    qmpic = db.Column(db.String(99))
    _updateTime = db.Column(db.String(99))
    ssq = db.Column(db.String(99))
    openid = db.Column(db.String(99),index=True)

class KFSS(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'kfss'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    xm = db.Column(db.String(99),index=True)
    xb = db.Column(db.String(99))
    csny = db.Column(db.String(99))
    sfzhm = db.Column(db.String(99),index=True)
    hk = db.Column(db.String(99))
    sjhm = db.Column(db.String(99))
    cjzhm = db.Column(db.String(99))
    jtzz = db.Column(db.String(99))
    jhrxm = db.Column(db.String(99))
    jhrzz = db.Column(db.String(99))
    jtjjqk = db.Column(db.String(99))
    cjlb = db.Column(db.String(99))
    cjdj = db.Column(db.String(99))
    sqxm = db.Column(db.String(99))
    pic0 = db.Column(db.String(99))
    pic1 = db.Column(db.String(99))
    pic2 = db.Column(db.String(99))
    pic3 = db.Column(db.String(99))
    pic4 = db.Column(db.String(99))
    qmpic = db.Column(db.String(99))
    _updateTime = db.Column(db.String(99))
    openid = db.Column(db.String(99),index=True)


class GXHFJ(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'gxhfj'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    xm = db.Column(db.String(99),index=True)
    xb = db.Column(db.String(99))
    csny = db.Column(db.String(99))
    sfzhm = db.Column(db.String(99),index=True)
    hk = db.Column(db.String(99))
    sjhm = db.Column(db.String(99))
    cjzhm = db.Column(db.String(99))
    jtzz = db.Column(db.String(99))
    jhrxm = db.Column(db.String(99))
    jhrzz = db.Column(db.String(99))
    jtjjqk = db.Column(db.String(99))
    cjlb = db.Column(db.String(99))
    cjdj = db.Column(db.String(99))
    sqxm = db.Column(db.String(99))
    pic0 = db.Column(db.String(99))
    pic1 = db.Column(db.String(99))
    pic2 = db.Column(db.String(99))
    pic3 = db.Column(db.String(99))
    pic4 = db.Column(db.String(99))
    qmpic = db.Column(db.String(99))
    _updateTime = db.Column(db.String(99))
    openid = db.Column(db.String(99),index=True)