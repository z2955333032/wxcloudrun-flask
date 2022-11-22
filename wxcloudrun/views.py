from wxcloudrun import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask import render_template, request,flash,make_response,send_file,session,redirect
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters,JDF,JDF33,KFSS,GXHFJ,USER
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
import json
str1 = 'https://7769-windows-7g06kkfp605c7962-1311495028.tcb.qcloud.la/'
str2 = 'cloud://windows-7g06kkfp605c7962.7769-windows-7g06kkfp605c7962-1311495028/'
#其他所有图片过滤器
@app.template_filter('showallpic')
def showallpic(li):
    strtemp = ''
    if li==None:
        return None
    else:
        temp_li = eval(li)
        list_len=len(temp_li)
        for index, s in enumerate(temp_li,1):
            if index==list_len and not list_len % 2==0:
                strtemp = strtemp + '<div class=\"page\"><img style=\"margin: 10px 0px;width: 680px;height: 500px;background-color:darkgrey;object-fit: contain;\" src=\"' + s.replace(str2, str1) + '\"></div>'
            elif not index % 2 == 0:
                strtemp = strtemp + '<div class=\"page\"><img style=\"margin: 10px 0px;width: 680px;height: 500px;background-color:darkgrey;object-fit: contain;\" src=\"' + s.replace(str2, str1) + '\">'
            else:
                strtemp = strtemp + '<img style=\"margin: 10px 0px;width: 680px;height: 500px;background-color:darkgrey;object-fit: contain;\" src=\"' + s.replace(str2, str1) + '\"></div>'
        return strtemp
#签名图片过滤器
@app.template_filter('showqmpic')
def showqmpic(li):
    try:
        return li.replace(str2, str1)
    except :
        return None
#发票过滤器
@app.template_filter('fp')
def fp(li):
    temp='< iframe src = \"test_pdf.pdf\" width = \"800\" height = \"600\" > < / iframe >'

    try:
        return li.replace(str2, str1)
    except :
        return None



#残疾类别选择过滤器
@app.template_filter('format_cjlb')
def format_cjlb(li):
    arr=['sl','tl','zt','yy','js','zl','dc']
    return arr[int(li)]




@app.route('/',methods=('GET', 'POST'))
def index():
    if session.get('username'):
        return redirect('/jdf/1')
    elif request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']  # 等同request.form.get('email')
        pw = request.form['pw']
        u = USER.query.filter_by(email=email, ).first()
        # print(generate_password_hash(pw)) 密码加密
        if check_password_hash(u.pw, pw):
            session['username'] = u.email  # 设置个session
            session['ssq'] = u.ssq
            # print(u.email,'222222222',u.ssq)
            return redirect('/jdf/1')
        else:
            return make_response("登录失败")

# 目前好像没有什么用
'''
@app.route('/login',methods=('GET', 'POST'))
def login():

    if request.method=='GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']  #等同request.form.get('email')
        pw = request.form['pw']
        u=USER.query.filter_by(email=email,).first()
        #print(generate_password_hash(pw)) 密码加密
        if check_password_hash(u.pw,pw):
            session['username']=u.email    #设置个session
            session['ssq'] = u.ssq
            #print(u.email,'222222222',u.ssq)
            return redirect('/jdf/1')
        else:
            return make_response("登录失败")


'''

@app.route('/pdf/<report_id>', methods=['GET'])
def post(report_id):
    headers = ("Content-Disposition", f"inline;filename={report_id}.pdf")#文件预览
    as_attachment = False
    # headers = (f"Content-Disposition", f"attachement;filename={report_id}.pdf")#文件下载
    # as_attachment = True
    file_path ='/static/bt.pdf'
        #.format(str(report_id))
    #print(file_path)
    response = make_response(send_file(filename_or_fp=file_path, as_attachment=as_attachment))
    response.headers[headers[0]] = headers[1]
    return response

 # 无用以后删除
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
    '''
    if request.method == 'POST':
        q = request.form['q']
        counter = Counters()
        counter.count = q
        counter.created_at = datetime.now()
        counter.updated_at = datetime.now()
        insert_counter(counter)
       '''
    return make_response('开发中。。。')
 # 无用以后删除
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
    jdf.ssq = params['ssq']
    jdf.pic0 = params['pic0']
    jdf.pic1 = params['pic1']
    jdf.pic2 = params['pic2']
    jdf.qmpic = params['qmpic']
    jdf._updateTime=params['_updateTime']
    '''
     jdf.xm = 'xm'
    jdf.xb = '1'
    jdf.csny = '1949-10-04'
    jdf.sfzhm = '123'
    jdf.hk ='1'
    jdf.sjhm = '110'
    jdf.cjzhm = '112'
    jdf.jtzz = '杭州市西湖区玉古路178号'
    jdf.jhrxm = 'jhrxm'
    jdf.jhrzz = '杭州市西湖区玉古路178号'
    jdf.jtjjqk = '0'
    jdf.cjlb = '2'
    jdf.cjdj = '3'
    jdf.sqxm = '1'
    jdf.pic0 = '[]'
    jdf.pic1 = '[]'
    jdf.pic2 = '[]'
    jdf.qmpic = ''
    jdf._updateTime = '2022-05-26'
    '''


    insert_counter(jdf)  #把以上数据插入数据库
    return make_succ_response('123')
 # 测试
@app.route('/api/jdf33', methods=['GET'])
def jdf33():

    D=JDF.query.all()
    for person in D:
        print(person.xm, person.sfzhm, person.pic1)
    payload = []
    content = {}
    for person in D:
        content = {'xm': person.xm, 'sfzhm': person.sfzhm}
        payload.append(content)
        content = {}
    return jsonify(payload)
 # 鉴定费列表
@app.route('/jdf/<int:page>')
def jdflist(page):
    ee=session.get('username')
    if not ee:
        return redirect('/login')

    #jdfbase = JDF.query.order_by(JDF.id.desc()).paginate(page=page, per_page=50)
    jdfbase = JDF.query.filter_by(ssq=session['ssq']).order_by(JDF.id.desc()).paginate(page=page, per_page=50)
    return render_template('list.html', infos=jdfbase.items, pagination=jdfbase)

@app.route('/jdf/context/<id>')
def context(id):
    ee = session.get('username')
    if not ee:
        return redirect('/login')
    content=JDF.query.get(id)
    if content.ssq==session['ssq']:
        return render_template('jdfsqb.html',content=content)
    else:
        return make_response('非法访问')
