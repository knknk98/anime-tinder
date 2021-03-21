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
          class="pic"
          :style="{
            'background-image': `url(data:image/jpg;base64,${scope.data.image})`,
          }"
        >
          <div class="gradient-black">
            <br><br><br><br>
            <h2 id="tinder-title">{{scope.data.title}}</h2>
            <br>
            <h3 id="tinder-year">- {{scope.data.year}}</h3>
            <br>
            <h3 id="tinder-genre" v-for="item in scope.data.genre" :key="item">#{{item}}</h3>
          </div>
        </div>
        <img class="like-pointer" slot="like" src="@/assets/image/LIKE.png">
        <img class="nope-pointer" slot="nope" src="@/assets/image/NOPE.png">
        <img class="super-pointer" slot="super" src="@/assets/image/SUPERLIKE.png">
      </VueTinder>
      <div id="buttons">
        <NopeButton @nope="decide('nope')"></NopeButton>
        <SuperLikeButton @superlike="decide('super')"></SuperLikeButton>
        <LikeButton @like="decide('like')"></LikeButton>
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
  middleware: 'authenticated',
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
      // 仕分けされたがまだpostされていないアニメ
      animeid: [],
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
    decide: function (choice){
      // カードをめくる(onSortをよぶ)
      this.$refs.tinder.decide(choice);
    },

    // フリック
    onSort: function (choice) {
      const id = this.animequeue[0].id;
      var res = {};
      switch (choice.type) {
        case 'nope': // 左
          res = {"animeId": id, "like": 0};
          break;
        case 'like': // 右
          res = {"animeId": id, "like": 1};
          break;
        case 'super': // 上
          res = {"animeId": id, "like": 2};
          break;
      }
      this.animesorted.push(res);
      this.animeid.push(id);
      // 残り1枚になったら5件取得
      if (this.animequeue.length < 2) {
        this.getData();
      }
    },
    // 5件を取得
    getData: async function() {
      this.loading = true,
      await axios.post(this.$config.serverURL+'/app/recs', {
        num: 5, 
        sessionID: this.$store.state.authUser,
        animeId: this.animeid,
      }).then(res => {
        // 5件追加→配列空に
        this.animequeue = this.animequeue.concat(res.data.animes);
        this.loading = false;
      }).catch(err => {
      });
    },
    // APIを叩いて結果を表示
    result: async function(){
      this.loading = true,
      await axios.post(this.$config.serverURL+'/app/rslts', {
        animes: this.animesorted, 
        sessionID: this.$store.state.authUser,
      }).then(res => {
        this.$router.push({  path: `/result/${res.data.animes[0].id}`  });
      }).catch(err => {
      });
    },
  },
};
</script>