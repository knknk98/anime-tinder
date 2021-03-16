# anime-tinder
2021/3/20, 21 サポーターズハッカソン制作物


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
