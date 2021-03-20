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
  methods: {
    like: function(){
      this.$emit('like');
    },
  },
}
</script>
