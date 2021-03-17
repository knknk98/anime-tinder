<template>
  <v-app >
    <v-main>
        <div v-if="$store.state.authUser">
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
  }
}
</script>
