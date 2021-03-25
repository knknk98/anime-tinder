# オタクとアニメのマッチングサービス「Toonder」
TinderライクなUIで機械学習を用いたアニメのマッチングアプリです。<br>
2021年3月に開催されたサポーターズ様の[初めてのハッカソン～オンライン開発合宿vol.1～](https://talent.supporterz.jp/events/337ce715-9813-41d4-a995-e3504dc8e719/)にて制作し、努力賞を頂きました🎉
<table>
    <tr>
        <td><img src="https://pbs.twimg.com/media/Ew_79wEU8AM7d7J.jpg"></td>
        <td><img src="https://pbs.twimg.com/media/Ew_79wFVEAMcwp_.jpg"></td>
        <td><img src="https://pbs.twimg.com/media/Ew_79wGVIAYwQ4F.jpg"></td>
    </tr>
</table>

ハッカソン成果発表会での発表スライドは[こちら](https://docs.google.com/presentation/d/1aiErRkm83ym6V2uRRhRt45-jKRs2o5iybhF9H1DCkes/edit?usp=sharing)


<table>
  <tr>
    <th width="60px">アプリ名</th><td>Toonder</td>
  </tr>
  <tr>
    <th>開発人数</th><td>4人<br>
        <b><a><a href="https://github.com/knknk98"><img src="https://github.com/knknk98.png" width="50px;" style="border-radius: 50%;" /></a></b>
        <b><a><a href="https://github.com/koukiNAGATA" target="_blank"><img src="https://github.com/koukiNAGATA.png" width="50px;" /></a></b>
        <b><a><a href="https://github.com/littleIkawa" target="_blank"><img src="https://github.com/littleIkawa.png" width="50px;" /></a></b>
        <b><a><a href="https://github.com/hoppiece" target="_blank"><img src="https://github.com/hoppiece.png" width="50px;" /></a></b></td>
  </tr>
  <tr>
    <th>担当</th><td>フロントエンド：@knknk98 @koukiNAGATA<br>
    バックエンド（API作成）：@litteleIkawa、
    バックエンド（レコメンドアルゴリズム）：@hoppiece</td>
  </tr>
  <tr>
    <th>開発期間</th><td>約1週間</td>
  </tr>
  <tr>
    <th>使用技術</th>
    <td><img src="https://user-images.githubusercontent.com/65712721/112453423-0481e100-8d9b-11eb-830a-b394215beddf.png" width="70%"></td>
  </tr>
</table>

## 構成
- Docker ... バージョン管理
- flask ... サーバサイドフレームワーク
- Nuxt.js ... フロントエンドフレームワーク
- Vuetify ... UIライブラリ
- figma ... ワイヤーフレーム
- swagger ... API仕様書

## ディレクトリ構成
```
anime-tinder
├── README.md
├── docker-compose.yml
├── Dockerfile ... python用のDockerfile
├── api-document.yaml ... API仕様書
├── app ... フロントエンド
│   ├── Dockerfile
│   └── front ... Nuxtのプロジェクト
│       ├── assets
│       ├── components
│       ├── layouts
│       ├── middleware
│       ├── node_modules
│       ├── nuxt.config.js
│       ├── package.json
│       ├── pages
│       ├── plugins
│       ├── README.md
│       ├── static
│       ├── store
│       └── yarn.lock
├── mysql ... データベース
│    ├── Dockerfile
│    ├── my.cnf
│    └── sqls
│        └── initialize.sql ... 初回起動時実行されるSQL
└── src ... pythonのコード
```

## フロントエンド(Nuxt)
### 実行
`docker-compose up` コンテナを起動。自動的に`yarn run dev` が実行されるようになっている

http://localhost:3000 にページが表示される

`Ctrl+C`で終了

## バックエンド（flask）
### 実行
`docker-compose up -d` でバックグラウンド実行. `flask run -h 0.0.0.0`が実行される（`0.0.0.0`で外部からの受付、実行ファイルは`Dockerfile`で指定している）. http://localhost:5000 でバックエンドに接続できる.

## API仕様書
swaggerを用いた。yaml形式で記述されている。

`api-document.yaml`をhttps://editor.swagger.io/ などで開く。

サーバに接続した状態で各APIの"Try it out"を押してパラメータやらリクエストの値やらを入力し"Execute"するとちゃんとAPIが動作してるかチェックできる。
