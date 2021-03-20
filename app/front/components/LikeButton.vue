<template>
  <v-btn
    class="mx-2"
    fab
    small
    @click="like"
  >
    <v-icon id="like-gradient">
      mdi-circle-outline
    </v-icon>
  </v-btn>
</template>
<script>
export default {
  data() {
  },
  methods: {
    like: function(){
      this.$router.push('/result');
    },
  },
}
</script>
