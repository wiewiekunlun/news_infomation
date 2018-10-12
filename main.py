from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from info import cerate_app

app = cerate_app('dev')

# 创建管理器  脚本启动
mgr = Manager(app)

# 添加迁移命令
mgr.add_command('yf', MigrateCommand)


if __name__ == '__main__':
    mgr.run()