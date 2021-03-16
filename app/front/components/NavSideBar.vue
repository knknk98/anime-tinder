<template>
  <div>
    <!-- 色付きドロワー -->
    <v-navigation-drawer
      app
      v-model="drawer"
      clipped
      class="accent-4 horizontal-gradient"
      dark
    >
      <h3>最近の診断結果</h3>
      <!-- 履歴表示 -->
      <v-list>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :href="item.to"
          link
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>


<script>
  export default {
    data () {
      return {
        drawer: null,
        items: [
          { title: '五等分の花嫁', to: "/result/gotoubun" },
          { title: '呪術廻戦', to: "/result/jyujyutsu" },
          { title: 'リゼロ', to: "/result/rezero" },
        ],
        csrf_token: document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
      }
    },
  }
</script>