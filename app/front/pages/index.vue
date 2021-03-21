<template>
  <div>
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
            'background-image': `data:image/jpg;base64,${scope.data.image}`,
          }"
        >
          <h2 id="tinder-title">{{scope.data.title}}</h2>
          <h3 id="tinder-year">- {{scope.data.year}}</h3>
          <br>
          <h3 id="tinder-genre"># {{scope.data.genre}}</h3>
        </div>
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
      console.log(this.animequeue[0].image);
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