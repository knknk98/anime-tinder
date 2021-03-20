<template>
    <v-btn dark x-large class="horizontal-gradient" rounded @click="login">
        Twitter Login
    </v-btn>
</template>
<script>
export default {
  methods: {
    login: function () {
      window.location.href = this.$config.serverURL+"/user/login";
    },
  },
}
</script>