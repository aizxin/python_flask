#coding:utf8

from . import home
from flask import render_template

@home.route("/")
def index():
    return "<h1>this is home</h1>"
@home.route("/login")
def login():
    return render_template("home/login.html")
