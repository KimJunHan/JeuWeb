from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "andThenSome"

# url에서 페스부분을 정하자.
# <>안은 변수명이다. 변수로 받겠다.
# 웹상에서 url이 서버 요청 리퀘스트고 브라우저화면이 리스폰이다.서버응답이다.
from markupsafe import escape
@app.route('/test/<title>') # 127.0.0.1/test/abcdef
def title(title):
    # 타이틀 바다엇 포맷스트링으로 브라우저로 전송하자.
    return f"title is {title}, {escape(type(title))}"

@app.route('/test/<int:id>')
def id(id):
    return f"id is {id}, {escape(type(id))}"
# json은 {} 이런 데이터 타입을 갖게되는데 dictionary된다 제이순만들면 직렬화할 수 있다. json 스트링으로 바꿔준다.
# json으로 바꿔주는 라이브러르는 Jsonifgy로 리스폰스로 (지금은 return으로 연결된다.) json으로 연결하자.
# 네트웍 타고 나갈때에 직렬화할수있다. 복원하는입장에서 받은 순서대로 직렬화된다.
# 직렬화 병렬화는 직렬화는 시리얼라이저블이라한다.
# 제이순으로 데이터파이을 전달하는게 묵시적 표준이다.

from flask import jsonify
@app.route('/test/json')
def json():
    # 반응으로 json 덩어리를 던지면된다.
    return jsonify({
        'id': '1',
        'name': 'andThensome',
        'addr': 'Seoul'

    })

# 페스를 받을때 우리들의 서버에서
# 우리들이 서비스하는 기능이 있는데
# 클라이언트와 서버가 있고 클라이언트가 리퀘스트에서 어떤 페스가들어왔을때 127.0.0.1 domain name or ip version4가오고 다음으로
# path가 오는데 서버에서 받아서 리스폰스 보낼때 패스정보를 통해서 요청자가 원하는 문서에 접근을 하는데
# 문서에 경로가 다른곳으로 또는 다른 서버로 이전을하면 요청을 바꿔서 전달해야하는데
# 이런 과정을 리다이렉션이라한다.
from flask import redirect

@app.route('/test/path/<path:redirect_path>')
def path(redirect_path):
    return redirect_path


@app.route('/test/redirect/<path:redirect_path>')
def redirect_url(redirect_path):
    return redirect(redirect_path)

'''
url_for(함수명, path 파라미터)
파라미터에 전달받은 path를 함수명에 전달한다.
'''

from flask import url_for
@app.route('/test/urlfor/<path:testpath>')
def urlfor(testpath):
    return redirect(url_for('path', rediect_path=testpath))

# 서버 내에서 받은 요청에 대해 로그 정보를 계속 기록할 수 있는 방법과
# 리퀘스트 리스폰스과정에서 서버에서 생존하는 변수를 만들 수 있다
# 부가적인 정보를 글러벌 베리어블을 G라고하는 어플레이케이션 컨텍스트가 가지는 정보를 확인하는 정보를 알아볼수 있다.

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host = "127.0.0.1", port= 7000)