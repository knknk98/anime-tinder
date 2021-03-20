<template>
  <div>
    <v-app-bar
      color="deep-purple accent-4"
      dense
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Page title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer
    app
    v-model="drawer"
    clipped
    class="accent-4"
    >
    <h3 id="recent-title">最近の診断結果</h3>
    </v-navigation-drawer>

  </div>
</template>


<script>
  export default {
    data: () => ({
      drawer: false,
      group: null,

    }),

    watch: {
      group () {
        this.drawer = false
      },
    },
  }
</script>