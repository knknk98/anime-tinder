<template>
  <v-row justify="center" align="center">
    Redirecting Home...
  </v-row>
</template>

<script>
import axios from 'axios';

export default {
  async mounted() {
    await axios.get('http://127.0.0.1:5000/user/callback', {
      params: this.$route.query,
    }).then(res => {
      // set session
      this.$store.commit('setAuthUser', res.data.sessionId);
      this.$store.commit('setUserName', res.data.username);
      this.$store.commit('setUserImage', res.data.profile_image_url);

      this.$router.push('/');
    }).catch(err => {
    });
  },
};
</script>
