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
├── api-document.yaml ... API仕様書
└── app ... フロントエンド
    ├── Dockerfile
    └── front ... Nuxtのプロジェクト
        ├── assets
        ├── components
        ├── layouts
        ├── middleware
        ├── node_modules
        ├── nuxt.config.js
        ├── package.json
        ├── pages
        ├── plugins
        ├── README.md
        ├── static
        ├── store
        └── yarn.lock
```

## フロントエンド(Nuxt)
### 実行
`docker-compose up` コンテナを起動。自動的に`yarn run dev` が実行されるようになっている

http://localhost:3000 にページが表示される

`Ctrl+C`で終了

## API仕様書
swaggerを用いた。yaml形式で記述されている。

`api-document.yaml`をhttps://editor.swagger.io/ などで開く。
