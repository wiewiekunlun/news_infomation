from flask import Blueprint

# 1 创建蓝图对象
home_blu = Blueprint('home', __name__)

# 4 关联试图函数
from .views import *
