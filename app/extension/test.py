# from flask import Flask, request
# from flask_script import Manager,Shell
# from flask_mail import Mail,Message
# from threading import Thread
# import os
#
# app = Flask(__name__)
#
# app.config['DEBUG'] = True
#
#
# app.config['MAIL_SERVER'] = 'smtp.exmail.qq.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USERNAME'] = '260541530@qq.com'
# app.config['MAIL_PASSWORD'] = 'cqpljkvwphfjcbcj'
#
# manager = Manager(app)
# mail = Mail(app)
#
# ## 异步发送邮件
# def send_async_email(app,msg):
#     with app.app_context():
#         mail.send(msg)
#
# @app.route('/')
# def index():
#     msg = Message(subject='Email test by flask-email', sender="liuc1@xxx.com",recipients=['1052983996@qq.com'])
#     msg.body = 'hello 刘超'
#     msg.html = '<b>测试Flask发送邮件<b>'
#
#     thread = Thread(target=send_async_email, args=[app, msg])
#     thread.start()
#
#     # mail.send(msg)
#
#     return '<h1>邮件发送成功</h1>'
#
# if __name__ == '__main__':
#     manager.run()
#
