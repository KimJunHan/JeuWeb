from flask import Flask
# app.py로 만들어야 일반적으로 파일로 인식한다.

app = Flask(__name__)
# 네임은 메인 펑션을 받는다.
print(__name__)

# 골벵이표현은 데코레이터로 펑션 위에 항상 존재한다
# 어떤 평셩위에 해당평션에 맵핑돼서 플라스크에서
# 웹프로그램이라 웹요청이 들어오면
# client - server 사이에 요청과 반응이
# http request(url request), http response(html 페이지를 담아서 보낸다.)
# 요청과 반응사이에 데이터가 연결됐다 끊어지는데
# 클라이언트와 서버간에 파이프라인을 뚫어서 일정 시간 동안 연결을 유지하는데
# https를 이욯하는 절차는 비연결 지향이다.
# 요청은 브라우저에서 오는데 클라이언트는 브라우저고
# 우리는 지금 플라스크로 서버를 구현하고 있다.
# uniform resource loation 어떤 데이터가 위치했는지 확인 url 펑션과
# app. ~~이라는 @와 맵핑된다.
# http:// 도메인 네임이오고 path 정보가 오는데 파일 위치 페스정보고온다.
# 그 다음에 쿼리 스트링이온다 전달해줘야하는 파라미터가 있으면 ? 와 변수를 정의한다.
# 변수가 여러개면 &로 이어진다.
# url과 url에 대응하는 함수가 맵핑돼야한다.
#  * Debug mode: off이면 웹상에서 에러가 어디서 발생했는지 트레이싱할 수 없다.

#http://domain.name//(index.html)

@app.route('/')
def index():
    return "hello world"

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host = "127.0.0.1", port= 6000)