
import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #주소 뒤에 붙는 이름?
@app.route('/cover')
def test():
    return render_template('cover.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/album')
def album():
    return render_template('album.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/todo')
def todo():
    return render_template('ToDoList.html')



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000")
    app.run(host="0.0.0.0", port=port)