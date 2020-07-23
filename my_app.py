# Flask - server 띄우기
# render_template - template render 해줌 - html 문서를 html 형식으로 변환해서 날려줌
from flask import Flask , render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from data import Articles
import pymysql

app = Flask(__name__)
app.debug=True

# config MySQL
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='myflaskapp'
app.config['MYSQL_CURSORCLASS']='DictCursor'

db = pymysql.connect(host='localhost',
                port=3306,
                user='root',
                passwd='1234',
                db='myflaskapp')

cursor = db.cursor()

sql_1 = 'SELECT * FROM users;'
# sql_2 = '''
#         INSERT INTO users(name, email, username, password)
#         VALUES ('Lee', '3@naver.com', 'Lee', '1234');
#             '''
# result = cursor.execute(sql_2)
# db.commit()
# db.close()

# print(result)
# users = cursor.fetchall()
# print(users[0][1])
cursor.execute(sql_1)
users = cursor.fetchall()
print(users)


# # init mysql
# mysql = MySQL(app)
# cur = mysql.connection.cursor()
# result = cur.execute("SELECT * FROM users;")

# users = cur.fetchall()
# print(users)
# print(result)





# @ : 데코레이터
# route : 중계 - 서버의 경로 요청에 따라 무엇을 할지 결정 - 경로 지정
@app.route('/')
def index():
    # print("Success")
    # return "TEST"
    return render_template('home.html', hello = "Kkkkkkkkim")

@app.route('/about')
def about():
    # print("Success")
    # return "TEST"
    return render_template('about.html', hello = "Kimmmm")

@app.route('/articles', methods=['GET', 'POST'])
def articles():
    # print("Success")
    # return "TEST"
    articels = Articles()
    print(len(articels[0]))
    return render_template('articles.html', articles = articels)

@app.route('/test')
def show_image():
    return render_template('image.html')

# 경로를 params로 받기 - <string:id> or <int:id>
@app.route('/article/<int:id>')
def article(id):
    print(id)
    articles = Articles()[id-1]
    print(articles)
    return render_template('article.html', data = articles)
    # return "Success"


#local host ip address 127.0.0.1
if __name__ == '__main__' :
    # app.run(host = '0.0.0.0', port='6000')
    app.run()