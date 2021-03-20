<template>
  <v-btn
    class="mx-2"
    fab
    small
  >
    <v-icon id="superlike-gradient">
      mdi-heart
    </v-icon>
  </v-btn>
</template>
<script>
export default {
  data() {
  },
  methods: {
    superlike: function(){
      this.$router.push('/');
    }
  },
}
</script>
