<template>
  <v-app >
    <v-main>
        <div v-if="$route.name == 'index' || $route.name.includes('result')">
          <NavSideBar/>
        </div>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import NavSideBar from '~/components/NavSideBar.vue'
export default {
  components: {
    NavSideBar,
  },
  mounted(){
  }
}
</script>
