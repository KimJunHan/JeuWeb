'''
request hook
- request가 발생하고, request 전/후 등에 이벤트를 트리거링 하여 콘트롤 할 수 있음
  예, request 전에 항상 user session을 checking
     reuqest 후에는 항상 DB 세션을 closing


application context
- from flask import g
- 자주사용되는 application context는 g와 current_app이 있으며,
  요청이 생성되고, 완료될 때 생성 및 제거 됨

  g는 global을 의미
  - g의 일반적 사용은 request 중 자원 관리용도로 사용됨
  - 각각의 request 내에서만 값이 유효한 스레드 로컬 변수이므로 각 request는 자원을 공유하지 않습니다.

  current_app
  - 활성화된 application을 위한 인스턴스(즉 앱과의 연결고리라고 생각하자)
  - 예를 들어, app인스턴스를 import 하지 않고도, app의 config정보를 조회할 수 있음

'''
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

app = Flask(__name__)

# logging.debug("debug")
# logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

# logging 핸들러에서 사용할 핸들러를 불러온다.
file_handler = RotatingFileHandler(
    'project.log', maxBytes=2000, backupCount=10)
file_handler.setLevel(logging.INFO)
# 어느 단계까지 로깅을 할지를 적어줌
# app.logger.addHandler() 에 등록시켜줘야 app.logger 로 사용 가능
app.logger.addHandler(file_handler)

@app.route('/')
def index():
    app.logger.warning("index calling")
    return 'hello world!!!!!!'

# '''
# Request Hook
# '''
# @app.before_first_request
# def befor_first_request():
#     app.logger.warning("befor_first_request")
#
# @app.before_request
# def befor_request():
#     app.logger.warning("befor_request")
#
# @app.after_request
# def after_request(response):
#     app.logger.warning("after_request")
#     return response
#
# @app.teardown_request
# def teardown_request(exception):
#     app.logger.warning("teardown_request")


'''
Request Hook and g, application_context
'''
from flask import g, current_app

@app.before_first_request
def befor_first_request():
    app.logger.warning("befor_first_request")

@app.before_request
def befor_request():
    #추가
    g.testing = "here" #하나의 ruqest에서만 생존하고 있는 변수라고 생각하면됩니다.
    app.logger.warning("befor_request")

@app.after_request
def after_request(response):
    #추가
    app.logger.error(f"g.testing : {g.testing}")
    app.logger.error(f"current_app.config : {current_app.config}")

    app.logger.warning("after_request")
    return response

@app.teardown_request
def teardown_request(exception):
    app.logger.warning("teardown_request")

#추가
@app.teardown_appcontext
def teardown_appcontext(exception):
    app.logger.error("teardown_context")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')
