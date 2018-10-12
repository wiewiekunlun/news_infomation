
from . import home_blu

# 使用蓝图
@home_blu.route('/')
def index():
    return 'index'

