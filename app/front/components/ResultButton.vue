<template>
  <v-btn
    class="mx-2"
    fab
    small
    @click="result"
  >
    <v-icon id="submit-gradient">
      mdi-arrow-right-thick
    </v-icon>
  </v-btn>
</template>
<script>
export default {
  methods: {
    result: function(){
      this.$emit('result');
    },
  },
}
</script>
