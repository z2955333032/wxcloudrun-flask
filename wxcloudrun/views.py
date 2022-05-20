from wxcloudrun import db
from datetime import datetime
from flask import render_template, request,flash,make_response
from run import app
from wxcloudrun.dao import query_byid,delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters,JDF,JDF33
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
import json

#其他所有图片过滤器
@app.template_filter('showallpic')
def showallpic(li):
    str1 = 'https://7769-windows-7g06kkfp605c7962-1311495028.tcb.qcloud.la/'
    str2 = 'cloud://windows-7g06kkfp605c7962.7769-windows-7g06kkfp605c7962-1311495028/'
    strtemp = ''
    if li==None:
        return strtemp
    else:
        temp_li = eval(li)
        for index, s in enumerate(temp_li):
            if index % 2 == 0:
                strtemp = strtemp + '<div class=\"page\"><img style=\"margin: 10px 0px;width: 680px;height: 500px;background-color:darkgrey;object-fit: contain;\" src=\"' + s.replace(str2, str1) + '\">'
            else:
                strtemp = strtemp + '<img style=\"margin: 10px 0px;width: 680px;height: 500px;background-color:darkgrey;object-fit: contain;\" src=\"' + s.replace(str2, str1) + '\"></div>'
        return strtemp
#签名图片过滤器
@app.template_filter('showqmpic')
def showqmpic(li):
    str1 = 'https://7769-windows-7g06kkfp605c7962-1311495028.tcb.qcloud.la/'
    str2 = 'cloud://windows-7g06kkfp605c7962.7769-windows-7g06kkfp605c7962-1311495028/'
    try:
        return li.replace(str2, str1)
    except :
        return None






@app.template_filter('format_cjlb')
def format_cjlb(li):

    arr=['sl','tl','zt','yy','js','zl','dc']
    return arr[int(li)]




@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return make_succ_response('index.html')


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

@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        q = request.form['q']
        counter = Counters()
        counter.count = q
        counter.created_at = datetime.now()
        counter.updated_at = datetime.now()
        insert_counter(counter)
    return make_succ_response(counter.count)

@app.route('/api/count', methods=['GET'])
def get_count():
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)
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
    jdf.qmpic = params['qmpic']
    insert_counter(jdf)
    return make_succ_response('123')

@app.route('/api/jdf33', methods=['GET'])
def jdf33():
    D=JDF33.query.all()
    return render_template('1.html', DA=D)

@app.route('/jdf/<int:page>')
def jdflist(page):
    D = JDF.query.order_by(JDF.id.desc()).limit(50)
    return render_template('list.html',DA=D,page=page)

@app.route('/jdf/context/<id>')
def context(id):
    content=JDF.query.get(id)
    return render_template('kfssbz.html',content=content)
