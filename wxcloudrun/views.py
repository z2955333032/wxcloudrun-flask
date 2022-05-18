from datetime import datetime
import requests
import json
from flask import Response
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters,JDF,JDF33
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


@app.route('/getTempFileURL')
def getTempFileURL():
    url = 'http://api.weixin.qq.com/tcb/batchdownloadfile'
    date={
        "env": "prod-4gbn9qf2c1863879",
        "file_list": ["cloud://prod-4gbn9qf2c1863879.7072-prod-4gbn9qf2c1863879-1311495028/41b62073121f73537ff9532391f2f3e.jpg"]
            }
    res = requests.post(url=url,data=date)
    
    return make_succ_response(res) 

@app.route('/1')
def re():
    url = 'https://windows-7g06kkfp605c7962-1311495028.ap-shanghai.service.tcloudbase.com/api/v1.0/jdf'
    headers = {
        'Authorization': 'Bearer TUKBtYVT1FOqVOQ6rl7yTGcTpRwkyXFn3-scnJtYyaz4i4h9GNS0LpAdlHTla5w_0Iukv9tRC2KADQhhfuG7jbQ24F9XBHod929XGYOOAOSuENXE9eD3t5fvwhbnAzEb'}
    res = requests.get(url=url, headers=headers)
    d = res.json()['data']
    return render_template('1.html',DA=d)
@app.route('/api/jdf33', methods=['POST'])
def jdf33():
    #params = request.get_json()
    #print(params)
    jdf = JDF33()
    jdf.xm='params[xm]'
    jdf.sfzhm ='params[sfzhm]'
    insert_counter(jdf)
    return make_succ_response('JDF33') 

@app.route('/api/jdf', methods=['POST'])
def jdf():
    params = request.get_json()
    jdf = JDF()
    jdf.xm=params['xm']
    jdf.xb = params['xb']
    jdf.csny =params['csny']
    jdf.sfzhm =params['sfzhm']
    jdf.hk = params['hk']
    jdf.sjhm = params['sjhm']
    jdf.cjzhm = params['cjzhm']
    jdf.jtzz = params['jtzz']
    jdf.jhrxm = params['jhrxm']
    jdf.jhrzz = params['jhrzz']
    jdf.jtjjqk =params['jtjjqk']
    jdf.cjlb = params['cjlb']
    jdf.cjdj = params['cjdj']
    jdf.sqxm =params['sqxm']
    jdf.pic0 = params['pic0']
    jdf.pic1 = params['pic1']
    jdf.pic2 = params['pic2']
    jdf.QmPic = params['QmPic']
    insert_counter(jdf)
    return make_succ_response('123') 
