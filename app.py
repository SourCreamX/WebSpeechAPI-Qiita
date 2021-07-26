import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def url_post():
    qiita_url = request.form.get('qiita_url')

    # スクレイピングするURLを指定しHTMLを取得  
    res = requests.get(str(qiita_url))

    # BeautifulSoupオブジェクトをつくる
    soup = BeautifulSoup(res.text, 'html.parser')

    # クラス名を指定して要素を取得
    speech_title = soup.find("h1",class_='css-cgzq40').get_text()
    speech_text = soup.find("section",class_='it-MdContent').get_text()

    context = {
        'title': speech_title,
        'text': speech_text
    }

    return render_template('index.html', context=context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')