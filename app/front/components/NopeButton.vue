<template>
  <v-btn
    class="mx-2"
    fab
    small
    @click="nope"
  >
    <v-icon id="nope-gradient">
      mdi-close
    </v-icon>
  </v-btn>
</template>
<script>
export default {
  methods: {
    nope: function(){
      this.$emit('nope');
    }
  },
}
</script>
