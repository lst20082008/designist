import os,datetime
from designist import db,app
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g
from designist.model.User import User
from designist.model.Post import Post
from designist.model.Category import Category

@app.route('/')
def index():
    posts = Post.query.limit(9).all()
    print(posts)
    return render_template('index.html',posts=posts)

@app.route('/show_regist')
def show_regist():
    return render_template('show_regist.html')

@app.route('/regist',methods=['POST'])
def regist():
    u = User(request.form['UserName'],request.form['Password'],request.form['telephone'],request.form['email'])
    print('尝试注册用户，名字：',u.username,'密码：',u.password,'电话：',u.telphone,'邮箱：',u.email)
    try:
        db.session.add(u)
        db.session.commit()
    except BaseException as e:
        print('注册失败:',e)
        return "注册失败"+e.__str__()
    return redirect(url_for('index'))

@app.route('/show_login')
def show_login():
    return render_template('show_login.html')

@app.route('/login',methods=['POST'])
def login():
    if request.form['Password'] == User.query.filter_by(username=request.form['UserName']).first().password:
        session['username']=request.form['UserName']
        print('登陆成功')
    else:
        print('登陆失败')
        return "登陆失败"
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route('/show_category')
def show_category():
    return render_template('show_category.html')

@app.route('/category',methods=['POST'])
def category():
    c = Category(request.form['name'],request.form['father_id'])
    try:
        db.session.add(c)
        db.session.commit()
    except BaseException as e:
        print('注册失败:',e)
        return "注册失败"+e.__str__()
    return redirect(url_for('index'))

@app.route('/show_add_post')
def show_add_post():
    return render_template('show_add_post.html')

@app.route('/post',methods=['POST'])
def post():
    p = Post(request.form['title'],request.form['abstract'],request.form['content'],datetime.datetime.now(),request.form['category_id'])
    f = request.files['image']
    print(os.path.join(os.path.abspath('.'),'designist/static/img/'+p.image))
    f.save(os.path.join(os.path.abspath('.'),'designist/static/img/'+p.image))
    try:
        db.session.add(p)
        db.session.commit()
    except BaseException as e:
        print('注册失败:',e)
        return "注册失败"+e.__str__()
    return redirect(url_for('index'))

@app.route('/show_post')
def show_post():
    fatherCategory = Category.query.filter_by(father_id='0').all()
    allCategory = Category.query.all()
    print(fatherCategory)
    print(allCategory)
    return render_template('show_post.html',fatherCategory=fatherCategory,allCategory=allCategory)