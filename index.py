from flask import Flask,render_template,request,jsonify,g,session
import sqlite3

app = Flask(__name__)
app.secret_key = '123' 
database = 'datafile.db'


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(database)
        g.sqlite_db.row_factory = sqlite3.Row
    return g.sqlite_db


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register',methods=['Get','POST'])  #註冊
def register():
    if request.method == 'POST':
        userName = request.form['userName']
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        try:
            db.execute('INSERT INTO users (userName , email, password) VALUES (?, ?, ?)', (userName, email, password))
            db.commit()
            return jsonify({'status': 'success', 'message': 'Registration successful!'})
        except sqlite3.IntegrityError:
            return jsonify({'status': 'failure', 'message': 'Email already registered!'})
    return render_template('register.html')


@app.route('/login',methods=['GET','POST'])  #登入
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE email = ? and password = ?', (email, password)).fetchone()
        if user:
            session['login'] =True
            session['userName'] = user['userName']
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'failure', 'message': 'Invalid email or password!'})
    return render_template('login.html')


@app.route('/myHome') # 個人端
def myHome():
    return render_template('Home.html')


@app.route('/AW') #加退選
def aw():
    return render_template('AW.html')


# @app.route("/info",methods=['post'])
# def returnSomething():
#     return jsonify({'info':'hello world'})


if __name__ == '__main__':
    app.run(debug=True)