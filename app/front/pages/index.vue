<template>
  <div>


    <v-dialog
      v-model="dialog"
      max-width="380"
    >
      <v-card>
        <v-list disabled>
          <v-subheader>
            画像をスワイプするかボタンを押してね！
          </v-subheader>
          <v-list-item-group
            color="primary"
          >
            <v-list-item>
              <v-list-item-icon>
                <v-icon id="like-gradient">mdi-circle-outline</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>LIKE/すき😸</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon id="superlike-gradient">mdi-heart</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>SUPERLIKE/だいすき😻</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon id="nope-gradient">mdi-close</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>NOPE/きらい😾</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon color="red">mdi-arrow-right-thick</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>結果をみる🏃‍♀️</v-list-item-title>
                <v-list-item-subtitle>好きなタイミングで押してね！</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card>
    </v-dialog>



    <Loading v-show="loading"></Loading>
    <div class="box home-background" v-show="!loading">
      <VueTinder
        key-name="id"
        :queue.sync="animequeue"
        @submit="onSort"
        ref="tinder"
      >
        <div
          slot-scope="scope"
          class="pic vertical-gradient"
          :style="{
            'background-image': `url(${scope.data.image})`,
          }"
        >
          <h2 id="tinder-title">{{scope.data.title}}</h2>
          <h3 id="tinder-year">- {{scope.data.year}}</h3>
          <br>
          <h3 id="tinder-genre"># {{scope.data.genre}}</h3>
        </div>
      </VueTinder>
      <div id="buttons">
        <NopeButton @nope="decide(nope)"></NopeButton>
        <SuperLikeButton @superlike="decide(superlike)"></SuperLikeButton>
        <LikeButton @like="decide(like)"></LikeButton>
        <ResultButton @result="result"></ResultButton>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Loading from '@/components/Loading';
import NopeButton from '@/components/NopeButton';
import SuperLikeButton from '@/components/SuperLikeButton';
import LikeButton from '@/components/LikeButton';
import ResultButton from '@/components/ResultButton';
import VueTinder from 'vue-tinder';

export default {
  //middleware: 'authenticated',
  components: {
    Loading,
    NopeButton,
    SuperLikeButton,
    LikeButton,
    ResultButton,
    VueTinder,
  },
  data() {
    return {
      name: 'index',
      // これから選別されるアニメ
      animequeue: [],
      // 仕分けされたアニメ
      animesorted: [],
      loading: false,
      dialog: this.$store.state.accessed,
    }
  },
  head() {
    return {
      title: '',
    }
  },
  // 最初5件を取得
  mounted () {
    this.getData();
    this.$store.commit('setAccessed', false);
  },
  methods: {
    // 0:NOPE,1:LIKE,2:SUPERLIKE
    // ボタン
    decide: function (choice, id){
      switch (choice) {
        case 'nope': // 左
          animesorted.push({"id": id, "like": 0});
          break;
        case 'like': // 右
          animesorted.push({"id": id, "like": 1});
          break;
        case 'superlike': // 上
          animesorted.push({"id": id, "like": 2});
          break;
      }
      // 残り1枚になったら5件取得
      if (this.animequeue.length < 2) {
        this.getData();
      }
      // カードをめくる
      this.$refs.tinder.decide(choice, id);
    },

    // フリック
    onSort: function (choice, id) {
      switch (choice) {
        case 'nope': // 左
          animesorted.push({"id": id, "like": 0});
          break;
        case 'like': // 右
          animesorted.push({"id": id, "like": 1});
          break;
        case 'superlike': // 上
          animesorted.push({"id": id, "like": 2});
          break;
      }
      // 残り1枚になったら5件取得
      if (this.animequeue.length < 2) {
        this.getData();
      }
    },
    // 5件を取得
    getData () {
      const list = [
        {
          "company": "MAPPA",
          "description": "人間の負の感情から生まれる化け物・呪霊を呪術を使って祓う呪術師の闘いを描いた、ダークファンタジー・バトル漫画。",
          "genre": "カテゴリ1",
          "id": 1,
          "image": "https://pbs.twimg.com/media/Epkl6M8VoAAGZAP.jpg",
          "title": "呪術廻戦",
          "year": "2020秋"
        },
        {
          "company": "ufotable",
          "description": "大正時代を舞台に主人公が鬼と化した妹を人間に戻す方法を探すために戦う姿を描く和風剣戟奇譚",
          "genre": "剣劇 ダーク・ファンタジー",
          "id": 2,
          "image": "https://animeanime.jp/imgs/p/jtKDOVlKAvjRrNw8SXAVejagI61Nrq_oqaqr/359929.jpg",
          "title": "五等分の花嫁",
          "year": "2019"
        },
        {
          "company": "MAPPA",
          "description": "人間の負の感情から生まれる化け物・呪霊を呪術を使って祓う呪術師の闘いを描いた、ダークファンタジー・バトル漫画。",
          "genre": "ダーク・ファンタジー",
          "id": 3,
          "image": "https://eiga.k-img.com/images/anime/news/112498/photo/a8c42bc0e5f54dc2/320.jpg?1607668254",
          "title": "リゼロ",
          "year": "2020冬"
        },
        {
          "company": "ProductionI.G",
          "description": "Production I.G制作による日本のオリジナルテレビアニメ作品、および、これを原作としたメディアミックス作品。",
          "genre": "SF アクション クライムサスペンス",
          "id": 4,
          "image": "https://dengekionline.com/images/U6Eo/iVNf/gAfD/JWlv/Vkjtk62p9OOmOlk5ovvHfnSD7BsrhFp0IYEPVWKXQjNE4bjLhjQ2ETa8nvAKQkPdow0ld9prCOr91ahW.jpg",
          "title": "PSYCHO-PASS サイコパス 3",
          "year": "2019秋"
        },
        {
          "company": "ufotable",
          "description": "大正時代を舞台に主人公が鬼と化した妹を人間に戻す方法を探すために戦う姿を描く和風剣戟奇譚",
          "genre": "剣劇 ダーク・ファンタジー",
          "id": 5,
          "image": "https://animeanime.jp/imgs/p/jtKDOVlKAvjRrNw8SXAVejagI61Nrq_oqaqr/359929.jpg",
          "title": "鬼滅の刃",
          "year": "2019"
        },
      ];
      // 5件変更
      this.animequeue = this.animequeue.concat(list);
    },
    // APIを叩いて結果を表示
    result: function(){
      // API叩く
      this.$router.replace({ name: 'result' });
    },
  },
};
</script>