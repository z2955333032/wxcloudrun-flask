from datetime import datetime
import requests
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)
@app.route('/api/test', methods=['GET'])
def test():
    """
    :return: 计数的值
    """
    data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'}
    return make_succ_response(data) 
@app.route('/api/test1', methods=['GET'])
def test1():
    r = requests.get("https://api.weixin.qq.com/wxa/getwxadevinfo")
    return make_succ_response(r.text)
@app.route('/api/zhfw', methods=['GET'])
def kffw():
    
    data = [{'title': '浙江省残联等六部门单位关于印发浙江省残疾儿童康复服务制度工作细则（修订版）的通知','author_name':'省残联','date': '2022-03-11 15:33','pageid': '11.html' },{'title': '关于公布残疾人基本型辅助器具目录（第二版）的通知','author_name': '省残联','date': '2021-12-16 17:04','pageid': '22.html'},
    {
        'title': '省残联等六部门单位关于印发浙江省残疾儿童定点康复机构协议管理办法（试行）的通知',
        'author_name': '省残联',
        'date': '2021-06-17 18:04',
        'pageid': '33.html'
    },
    {
        'title': '省残联等六部门单位关于推进全省残疾儿童定点康复机构规范化提升建设的通知',
        'author_name': '省残联',
        'date': '2021-06-18 08:55',
        'pageid': '44.html'
    },
    {
        'title': '浙江省残疾儿童康复服务制度工作细则（修订版）政策解读',
        'author_name': '省残联',
        'date': '2022-03-11 16:02',
        'pageid': '55.html'
    },
    {
        'title': '浙江省残联等六部门单位关于印发浙江省残疾儿童康复服务制度工作细则（修订版）的通知',
        'author_name': '省残联',
        'date': ' 2022-03-11 15:33',
        'pageid': '66.html'
    },]
    return make_succ_response(data) 
