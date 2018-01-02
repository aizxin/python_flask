#coding:utf8

from flask import render_template, jsonify, request,session
from . import admin
from app.models import Admin,Tag,Adminlog,Oplog
from app.admin.forms import LoginForm,TagForm
from app import db

def errors_first(errors):
    k = ''
    for v in errors:
        k = errors[v][0]
        break
    return k

@admin.route("/")
def index():
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=1, per_page=10)
    print(page_data)
    return render_template("admin/index.html")

# 登录
@admin.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            admin = Admin.query.filter_by(name=data["username"]).first()
            if not admin.check_pwd(data["password"]):
                return jsonify({ 'code': False,'message': "账号密码错误！"})
            session["admin"] = data["username"]
            session["admin_id"] = admin.id
            adminlog = Adminlog(
                admin_id=admin.id,
                ip=request.remote_addr,
            )
            db.session.add(adminlog)
            db.session.commit()
            return jsonify({ 'code': True,'message': "登录成功！"})
        else:
            return jsonify({'code': False,'message': errors_first(form.errors) })
    return render_template("admin/login.html",form=form)
# 标签
@admin.route("/tag/", methods=["GET", "POST"])
def tag():    
    return render_template("admin/tag/index.html")

# 标签添加或修改
@admin.route('/tag/create/', defaults={'id': 0})
@admin.route('/tag/create/<int:id>/', methods=["GET", "POST"])
def tag_create(id=0):g
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            if data["id"] > 0:
                tag = Tag.query.filter_by(name=data["name"]).count()
                if tag == 1:
                    return jsonify({'code': False,'message': '名称已经存在！' })
                tag = Tag(
                    name=data["name"]
                )
                db.session.add(tag)                
            else:

            db.session.commit()
            oplog = Oplog(
                admin_id=session["admin_id"],
                ip=request.remote_addr,
                reason="添加标签%s" % data["name"]
            )
            db.session.add(oplog)
            db.session.commit()
            return jsonify({ 'code': True,'message': "添加标签成功！"})
        else:
            return jsonify({'code': False,'message': errors_first(form.errors) })
    return render_template("admin/tag/create.html",form=form)