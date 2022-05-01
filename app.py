# app.py는 플라스크에서 기본적인 앱을 담을 수 있는 파일 이름이다.
# 플라스크도 하나의 패키지다. interpreiter에서 Flask를 install 하면 jinja도 다운된다.
# 탬플릿은 html을 저장할 수 있다.
# html파일이 어디있는지는 탬플릿 폴더 안에 가서 찾는다. templats다 s빠지면 안된다.

from flask import Flask, render_template

#플라스크 오브젝 만들기

app = Flask(__name__)

# 127.0.0.1:5000
# get방식으로 들어오면 하단의 함수를 실행 한다.
# methods다
# 127.0.0.1:5000/를 웹에 실행한다.

# url 호스트에서 html파일 불러 들이기

@app.route('/', methods=['GET'])
def index_page_randing():
    # render temlplate을 플라스크에서 가져온다
    # 탬플릿을 랜더링한다. 랜더링은 화면에 뿌려준다는 의미다.
    # 탬플릿 폴더 안에 html을 읽어 온다.
    return render_template('index.html')

# user name은 변수다 <>안에 들어가 있는 것 말이다.
# url 경로 설정하기
@app.route('/user/<username>')
def show_user_profile(username):
    return 'user name is %s' % username

#--------------------추가 test




# 프로그램의 흐름을 기술한다. 메인 프로세스의 시작이다.
if __name__ == '__main__':
    #플라스크 오브젝을 실행한다.
    app.run()
