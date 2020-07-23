import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='myflaskapp')
cursor = db.cursor()

##########################################################################################
# # # # # # # # # # # # # # # # sql : 테이블 추가  # # # # # # # # # # # # # # # # # # # # #
##########################################################################################
# sql = '''
#         CREATE TABLE users(
#             id INT(11) AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(100),
#             email VARCHAR(100),
#             username VARCHAR(30),
#             password VARCHAR(100),
#             register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
#             ENGINE=InnoDB DEFAULT CHARSET=utf8;
#     '''

# sql = '''
#     CREATE TABLE `topic` (
# 	    `id` int(11) NOT NULL AUTO_INCREMENT,
# 	    `title` varchar(100) NOT NULL,
# 	    `body` text NOT NULL,
# 	    `author` varchar(30) NOT NULL,
#         `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# 	    PRIMARY KEY (id)
# 	    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#     '''
# cursor.execute(sql)
# db.commit()
# db.close()

##########################################################################################
# # # # # # # # # # # # # # # # sql_1 : 조회 & sql_2 : 추가 # # # # # # # # # # # # # # # #
##########################################################################################
# sql_1 = 'SELECT * FROM users;'
# sql_2 = '''
#         INSERT INTO users(name, email, username, password)
#         VALUES ('PARK', '4@naver.com', 'PARK', '1234');
#             '''

# cursor.execute(sql_2)
# # INSERT 할 때는 commit() 해야됨
# # close()는 해도되고 안해도됨
# db.commit()
# db.close()

# print(result)
# users = cursor.fetchall()
# print(users[0][1])
# # SELECT는 fetchall() 해야됨
# # fetchall()하고 저장해야됨
# cursor.execute(sql_1)
# users = cursor.fetchall()
# print(users)

##########################################################################################
# # # # # # # # # # # # # # # # # sql_3 : 변수 활용 # # # # # # # # # # # # # # # # # # # #
##########################################################################################
# name = ['SONG', 'GANGNAM']
# email = ['5@naver.com', '6@naver.com']
# username = ['SONG', 'GANGNAM']
# password = ['1234', '1234']
# sql_3 = '''
#         INSERT INTO users(name, email, username, password)
#         VALUES (%s, %s, %s, %s);
#             '''

# cursor.execute(sql_3, (name[1], email[1], username[1], password[1]))
# db.commit()
# db.close()

##########################################################################################
# # # # # # # # # # # # # # # # # sql_4 : 데이터 삭제(id) # # # # # # # # # # # # # # # # #
##########################################################################################

# sql_4 = 'DELETE FROM `users` WHERE  `id`=`4`;'
# cursor.execute(sql_4)
# db.commit()
# db.close()

##########################################################################################
# # # # # # # # # # # # # # # # # sql_5 : 데이터 삭제(이름) # # # # # # # # # # # # # # # #
##########################################################################################
# sql_5 = 'DELETE FROM `users` WHERE  `name`="SONG";'
# cursor.execute(sql_5)
# db.commit()
# db.close()

##########################################################################################
# # # # # # # # # # # # # # # # # sql_6 : 데이터 수정(이름) # # # # # # # # # # # # # # # #
##########################################################################################
# sql_6 = 'UPDATE `users` SET `name`="PARK" WHERE  `id`=2;'
# cursor.execute(sql_6)
# db.commit()
# db.close()