from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
import json
from src.database import init_db, db
from src.models import User,LikeUnlike,AnimeData
from requests_oauthlib import OAuth1Session
from urllib.parse import parse_qsl

# https://qiita.com/AndanteSysDes/items/a25acc1523fa674e7eda
# https://qiita.com/shirakiya/items/0114d51e9c189658002e
# https://qiita.com/kai_kou/items/5d73de21818d1d582f00
# https://qiita.com/voygerrr/items/4c78d156fc91111798d5

def create_app():

    app = Flask(__name__)
    app.config.from_object('src.config.Config') # configを別ファイルのオブジェクトから読み込む

    #login_manager = LoginManager()
    #login_manager.init_app(app)
    app.secret_key = b'\x17x\xf0\x83\x93i\x14\xa3\xec<7\x88A\xca\xb5G'

    init_db(app) # databaseの初期化を行う

    @app.route('/')
    def index():
        if 'name' in session:
            # セッション変数の取得
            name = session['name']
            return f'hello {name}'
        else:
            return redirect(url_for('login_test'))

    @app.route('/show')
    def show_users():
        if 'name' in session:
            all_user = User.query.all()
            number_of_user = len(all_user)
            if not number_of_user == 0:
                user_names_list = [user.name for user in all_user]
                strings = '\n'.join(str(user_names_list))
            else:
                strings = ''
            return f'こんにちは{session["name"]}. 今ユーザーは{number_of_user}人います. \n' + strings
        else:
            return '''ログインしてください.<a href="/login">ログインページ</a>'''

    @app.route('/add')
    def add_user():
        user = User(name='name', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        return 'ユーザーを増やしました'

    @app.route('/delete')
    def delete_user():
        user = User.query.first()
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return 'ユーザーを減らしました'
        else:
            return 'ユーザーはひとりもいません'

    @app.route('/login', methods=['POST', 'GET'])
    def login_test():
        if request.method == 'POST':
            name = request.form['user_name']
            email = request.form['email']
            # user情報を確認
            the_user = User.query.filter(User.email==email).all()
            print(the_user)
            if len(the_user) == 0:
                # 存在しないなら登録処理
                user = User(name=name, email=email)
                db.session.add(user)
                db.session.commit()
            else:
                # 存在するならOK（emailはユニークなので）
                name = the_user[0].name

            # セッション変数の設定
            session['name'] = name
            return redirect(url_for('index'))
        else:
            return '''
                    <form method="post">
                        <p><input type=text name=user_name required>
                        <p><input type=text name=email required>
                        <p><input type=submit value=login>
                    </form>
                    '''

    # 認証画面を返す
    @app.route('/user/login', methods=['GET'])
    def get_twitter_request_token():
        # twitter api key
        consumer_api_key = 'qOoxU6YUCvtlTu59IkrSMwrs7'
        consumer_secret_key = 'QAzP9tbdfUof711fcD7GhiMXJPO5aE3p7GPnVEoZye96pX3XDP'
        # Twitter api URLs
        request_token_url = 'https://api.twitter.com/oauth/request_token'
        authorization_url = 'https://api.twitter.com/oauth/authorize'
        access_token_url = 'https://api.twitter.com/oauth/access_token'

        try:
            # リクエストトークンを取得し, 認証urlを取得してリダイレクトする. 失敗したらトップページへのリンクを提示する.
            oauth_callback = "http://127.0.0.1:3000/callback"
            twitter = OAuth1Session(consumer_api_key, consumer_secret_key)
            twitter.fetch_request_token(request_token_url)
            auth_url = twitter.authorization_url(authorization_url)
            return redirect(auth_url, code=200)

        except Exception as e:
            print(e)
            return '''login failed. <a href="http://localhost:3000>top</a>'''

    @app.route('/user/callback')
    def callback():
        pass

    @app.route('/logout')
    def logout():
        # セッション変数の削除
        session.pop('name', None)
        return redirect(url_for('login_test'))

    return app


app = create_app()
