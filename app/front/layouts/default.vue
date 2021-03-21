<template>
  <v-app >
    <v-main>
        <div v-if="$route.name == 'index' || $route.name.includes('result')">
          <AppBar/>
        </div>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from '~/components/AppBar.vue'
export default {
  components: {
    AppBar,
  },
  mounted(){
  }
}
</script>
