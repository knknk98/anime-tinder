<template>
  <div>
    <v-app-bar
      class="horizontal-gradient"
      dark
      dense
      flat
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" ></v-app-bar-nav-icon>
      <v-toolbar-title>Page title</v-toolbar-title>
    </v-app-bar>

    <!--左の三ボタン押したら開くやつ-->
    <v-navigation-drawer
    app
    v-model="drawer"
    clipped
    class="accent-4"
    >
    <!--Twitterアイコン関連-->
    <v-list-item dark class="horizontal-gradient-reverse" id="nav-user" v-on:click="open">
      <v-list-item-content>
        <v-list-item-title>
          <img :src="userImage" class="nav-icon-line">
          <h3 class="nav-icon-line">&nbsp;@{{$store.state.userName}}</h3>
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-list-item dark class="horizontal-gradient-reverse" id="nav-logout" :class="{ isOpen }" v-on:click="logout">
      <v-list-item-content>
        <v-list-item-title>
          <h3 class="nav-icon-line">Logout</h3>
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>

    <!--最近の診断結果-->
    <h3 id="recent-title">最近の診断結果</h3>
        <v-row justify="center">
            <v-col
                v-for="item in items"
                :key="item.id"
                cols=5
                class="d-flex child-flex">
                <v-img :src="item.image"  @click="openResult(item.id)"></v-img>
            </v-col>
        </v-row>
    </v-navigation-drawer>

  </div>
</template>


<script>
import axios from 'axios';
export default {
  data() {
      return {
          drawer: false,
          group: null,
          isOpen: false,
          userImage: this.$store.state.userImage,
          items: [
            { id: 1, image: "https://animeanime.jp/imgs/p/jtKDOVlKAvjRrNw8SXAVejagI61Nrq_oqaqr/359929.jpg"},
            { id: 2, image: "https://pbs.twimg.com/media/Epkl6M8VoAAGZAP.jpg"},
            { id: 3, image: "https://eiga.k-img.com/images/anime/news/112498/photo/a8c42bc0e5f54dc2/320.jpg?1607668254"},
            { id: 4, image: "https://assets.numan.tokyo/media/articles/images/000/008/367/large/b5b3dba5-f3a8-41af-b775-0bf08c1b7346.jpg?1584837573"},
            { id: 5, image: "https://dengekionline.com/images/U6Eo/iVNf/gAfD/JWlv/Vkjtk62p9OOmOlk5ovvHfnSD7BsrhFp0IYEPVWKXQjNE4bjLhjQ2ETa8nvAKQkPdow0ld9prCOr91ahW.jpg"},
            { id: 6, image: "https://media.image.infoseek.co.jp/isnews/photos/eigacom/eigacom_20201222001_0.jpg"}
          ],
      }
  },
  // 最近の診断結果を10件まで取得
  async mounted() {
    await axios.get(this.$config.serverURL+'/user/recent', {
      params: {
        "num" : 10,
        "sessionID": this.$store.state.authUser,
      }
    }).then(res => {
      this.items = this.items.concat(res.data.animes);
    }).catch(err => {
    });
  },
  watch: {
    group () {
      this.drawer = false
    },
  },
  methods: {
      open: function () {
      this.isOpen = !this.isOpen;
      },
      logout: function () {
      // サーバからのリダイレクトがうまくいかない。簡易的にログアウト
      this.$store.commit('setAuthUser', null);
      this.$store.commit('setUserName', null);
      this.$store.commit('setUserImage', null);
      this.$router.push('/login');
      },
      // 画像
      openResult: function (animeId) {
        console.log("呼ばれた");
        this.$router.push({  name: 'result', query: {id: animeId}  });
      }
  },
}
</script>