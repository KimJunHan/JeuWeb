'''
프레임웍은 web application이다
클라이언트가 브라우저면
브라우저에서 http request 요청이 들어온다.

맨처음 request와 response를 뿌려주는 임무를 하는 것을 web server라한다.
http의 규약을 처리한것을 웹서버라한다.

클라이언트에서 요청이오면 function을 구현하는것을 web application이라한다.
weeb application구현을 flask django다.

웹 애플리케이션과 웹서버를 명확히 구별해야한다.

웺서버는 아파치와 Ngix라한다.
아파치는 전통적으로 멀티프로세스로 구현하는 서번데
요청이 들어오면 프로세스를 만든다. 멀티프로세스 방식이다.

ngix는 멀티 스레드방식으로 만든다.

'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!!!!!!'

'''
HTTP Method
- GET, POST 
https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data

'''
from flask import request, jsonify

#아래 테스팅할 때(POSTMAN 이용) --> 구글검색 : POSTMAN Download
#POSTMAN 설정 방식
#GET 선택 : 127.0.0.1:5000/test/method/1?test='a'
#POST 선택 : 127.0.0.1:5000/test/method/1 --> Error발생, POST method를 처리하겠다고 선언하지 않았기 때문
@app.route('/test/method/<id>')
def test(id):
    return jsonify({
        'request.method':request.method,
        'request.args':request.args,
        'request.form':request.form,
        'request.json':request.json,
    })

#POST 선택 : 127.0.0.1:5000/test/method2/1, Body--> Key : test , Value : True
#POST 선택 : 127.0.0.1:5000/test/method2/1, Body--> row : { "id":"001", "name":"mk" }, 맨끝 text --> json 선택
@app.route('/test/method2/<id>', methods=['GET', 'POST'])
def test2(id):
    return jsonify({
        'request.method':request.method,
        'request.args':request.args,
        'request.form':request.form,
        'request.json':request.json,
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')