'''封装配置信息'''
from datetime import timedelta

import logging
from redis import StrictRedis


class Config():
    '''封装配置信息'''

    # 定义和配置同名的类属性
    # =======================基本配置和mysql配置================

    # 第一个位置为数据库类型  依次  数据库名称   密码  ip  端口  数据库名称
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/flask_test'  # 设置数据库连接地址
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪数据库变化

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # flask sqlalchemy 里面的init_app 中会有相关配置的介绍

    # =======================Redis配置================
    REDIS_HOST = '127.0.0.1'  # redis 的地址
    REDIS_PORT = 6379  # redis 的端口

    # =======================session存储配置================
    SESSION_TYPE = 'redis'  # session的存储形式
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 设置存储session的redis连接对象
    SESSION_USE_SIGNER = True  # 设置给session进行加密  需要设置应用密匙
    SECRET_KEY = 'yVJy5gV9lCpHhtPai+RuJ8BzRiS6sLzZaAFgBtL3hBnaiFPid/Of7fsKCInFcjhM'  # 应用密匙
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # 设置过期时间


# 不同的开发环境需要不同的配置
# 开发模式   继承父类
class DevelopmentConfig(Config):
    DEBUG = True  # 设置调试模式
    log_level = logging.DEBUG


# 生产模式
class ProductConfig(Config):
    DEBUG = False  # 设置调试模式
    log_level = logging.ERROR

config_dict = {
    'dev': DevelopmentConfig,
    'pro': ProductConfig

}