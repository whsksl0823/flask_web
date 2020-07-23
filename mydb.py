import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='myflaskapp')
db = pymysql.connect(
    host='localhost', 
    port=3306, 
    user='root', 
    passwd='1234', 
    db='myflaskapp')
cursor = db.cursor()
# sql = ''' 
#         CREATE TABLE users(
@@ -27,7 +32,7 @@
# db.commit()
# db.close()

sql_1 = 'SELECT * FROM users;'
sql_1 = 'SELECT name , email FROM users;'
sql_2=  '''
        INSERT INTO users(name, email , username, password) 
        VALUES ('PARK' ,'4@naver.com', 'PARK', '1234');
@@ -51,10 +56,24 @@
        INSERT INTO users(name, email , username, password) 
        VALUES (%s ,%s, %s,%s);
            '''

# cursor.execute(sql_3, (name, email , username, password))
# db.commit()
# db.close()

title='javascript'
body='프로토타입기반의 객체지향 프로그래밍 언어로, 스크립트 언어에 해당된다. 특수한 목적이 아닌 이상 모든 웹 브라우저에 인터프리터가 내장되어 있다. 오늘날 HTML, CSS와 함께 웹을 구성하는 요소 중 하나다. HTML이 웹 페이지의 기본 구조를 담당하고, CSS가 디자인을 담당한다면 JavaScript는 클라이언트 단에서 웹 페이지가 동작하는 것을 담당한다.'
author='Gary'
sql_7=  '''
        INSERT INTO topic(title, body , author) 
        VALUES (%s ,%s, %s);
            '''
# cursor.execute(sql_7 ,(title, body , author ) )
# db.commit()
# db.close()



sql_4='DELETE FROM `users` WHERE  `id`=5;'
# cursor.execute(sql_4)
# db.commit()
@@ -66,6 +85,13 @@
# db.close()

sql_6='UPDATE `users` SET `name`="PARK" WHERE  `id`=6;'
cursor.execute(sql_6)
db.commit()
db.close() 
# cursor.execute(sql_6)
# db.commit()
# db.close()


sql_8 = 'SELECT * FROM topic;'

cursor.execute(sql_8)
topics = cursor.fetchall()
print(topics) 