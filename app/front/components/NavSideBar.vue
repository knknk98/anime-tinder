<template>
  <!-- 色付きドロワー -->
  <v-navigation-drawer
    app
    v-model="drawer"
    clipped
    class="accent-4"
    permanent
  >
    <v-list-item dark class="horizontal-gradient" id="nav-icon">
      <v-list-item-content>
        <v-list-item-title>
          <img src="https://pbs.twimg.com/profile_images/1360240155081154563/O1hSiV0j_bigger.jpg" class="nav-icon-line" width="32">
          <h3 class="nav-icon-line">@iPhone_S_E_X</h3>
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>

    <!-- 履歴表示 -->
    <h3 id="recent-title">最近の診断結果</h3>
    <v-list>
      <v-list-item
        v-for="item in items"
        :key="item.title"
        :href="item.to"
      >
        <v-list-item-content>
          <v-card
            dark
            class="mx-auto"
            :img="item.imageUrl"
            height="250"
          >
            <v-card-title>
              <h3>
                {{ item.title }}
              </h3>
            </v-card-title>
          </v-card>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
  export default {
    data () {
      return {
        drawer: null,
        items: [
          { title: '五等分の花嫁', imageUrl: "https://animeanime.jp/imgs/p/jtKDOVlKAvjRrNw8SXAVejagI61Nrq_oqaqr/359929.jpg", to: "/result/gotoubun" },
          { title: '呪術廻戦', imageUrl: "https://pbs.twimg.com/media/Epkl6M8VoAAGZAP.jpg", to: "/result/jyujyutsu" },
          { title: 'リゼロ', imageUrl: "https://eiga.k-img.com/images/anime/news/112498/photo/a8c42bc0e5f54dc2/320.jpg?1607668254", to: "/result/rezero" },
          { title: 'はたらく細胞', imageUrl: "https://assets.numan.tokyo/media/articles/images/000/008/367/large/b5b3dba5-f3a8-41af-b775-0bf08c1b7346.jpg?1584837573", to: "/result/hataraku" },
          { title: 'ゆるキャン△', imageUrl: "https://dengekionline.com/images/U6Eo/iVNf/gAfD/JWlv/Vkjtk62p9OOmOlk5ovvHfnSD7BsrhFp0IYEPVWKXQjNE4bjLhjQ2ETa8nvAKQkPdow0ld9prCOr91ahW.jpg", to: "/result/yurukyan" },
        ],
      }
    },
  }
</script>