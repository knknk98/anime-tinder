<template>
  <v-app >
    <v-main>
        <div v-if="$route.name === ('index' || 'result')">
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
    console.log(this.$store.state.authUser);
    console.log(this.$route.name);
  }
}
</script>
