from flask import Flask
app = Flask(__name__)
@app.route('/') #주소 뒤에 붙는 이름?
def home():
    return 'Hello, World!'
@app.route('/html')
def html():
    return '''
    <h1> 안녕하세요 </h1>
    <a href="https://www.naver.com">네이버</a>
    '''
if __name__ == '__main__':
    app.run(debug=True, port=80) #port는 방호수 ! 한 호수에는 한 기능만 가능
    # 실행지킴 debug =True 수정할 경우에 수정을 반영하여 재 시작하는 것 