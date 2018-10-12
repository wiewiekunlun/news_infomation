''''''
import logging
from logging.handlers import RotatingFileHandler

from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from redis import StrictRedis
from flask_migrate import Migrate
from config import config_dict

# 数据库对象全局化
db = None  # type: SQLAlchemy
sr = None  # type: StrictRedis


def setup_log():  # 将日志保存到文件中
    # 设置日志的记录等级
    logging.basicConfig(level=logging.DEBUG)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)  # （我们创建logs文件夹 解释器会创建文件  并满且backupCount的意思是文件满十个之后， 会删除第一个文件的内容，在第一个里面写）
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(pathname)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def cerate_app(env):
    # 创建应用
    app = Flask(__name__)

    # 根据类型取出 不同模式 配置
    class_config = config_dict[env]

    # 从对象中加载配置信息
    app.config.from_object(class_config)

    global db, sr

    # 创建关系型数据库链接  数据库配置也封装到配置类中
    db = SQLAlchemy(app)

    # 创建redis数据库的连接
    sr = StrictRedis(host=class_config.REDIS_HOST, port=class_config.REDIS_PORT)

    # 创建session存储对象  flask 内置的
    Session(app)

    # 初始化迁移器
    Migrate(app, db)

    # 配置日志
    # setup_log(config_class.LOG_LEVEL)

    # 关联models
    from info import models

    # 注册蓝图对象
    from info.home import home_blu
    app.register_blueprint(home_blu)

    # 返回app
    return app