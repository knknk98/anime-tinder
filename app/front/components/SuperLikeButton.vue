<template>
  <v-btn
    class="mx-2"
    fab
    small
    @click="superlike"
  >
    <v-icon id="superlike-gradient">
      mdi-heart
    </v-icon>
  </v-btn>
</template>
<script>
export default {
  methods: {
    superlike: function(){
      this.$emit('superlike');
    }
  },
}
</script>
