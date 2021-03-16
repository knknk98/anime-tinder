<template>
  <v-app>
    <NavSideBar/>
    <v-main>
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
  }
}
</script>
