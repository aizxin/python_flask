# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import Admin, Tag, Auth, Role

class LoginForm(FlaskForm):
    """管理员登录表单"""
    username = StringField(
        validators=[
            DataRequired("请输入账号！")
        ]
    )
    password = PasswordField(
        validators=[
            DataRequired("请输入密码！")
        ]
    )
    def validate_username(self, field):
        username = field.data
        admin = Admin.query.filter_by(name=username).count()
        if admin == 0:
            raise ValidationError("账号不存在！")

