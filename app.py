# Flask - server 띄우기
# render_template - template render 해줌 - html 문서를 html 형식으로 변환해서 날려줌
from flask import Flask , render_template
from data import Articles

app = Flask(__name__)
app.debug=True

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
    articles = Articles()
    return render_template('article.html', data = [articles, id])


#local host ip address 127.0.0.1
if __name__ == '__main__' :
    # app.run(host = '0.0.0.0', port='6000')
    app.run()