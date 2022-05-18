from flask import Flask
app = Flask(__name__)
@app.route('/') #주소 뒤에 붙는 이름?
def home():
    return 'Hello, World!'
@app.route('/user/<user_id>/<user_pw>')
def user(user_id, user_pw):
    return 'ID : {}, PW: {}'.format(user_id, user_pw)
    #return f'ID : {user_id}, PW: {user_pw}'

@app.route('/html')
def html():
    return '''
    <h1> 안녕하세요 </h1>
    <a href="https://www.naver.com">네이버</a>
    '''

if __name__ == '__main__':
    app.run(debug=True) 