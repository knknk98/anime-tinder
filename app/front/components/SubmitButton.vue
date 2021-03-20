<template>
  <v-btn
    class="mx-2"
    fab
    small
    @click="submit"
  >
    <v-icon id="submit-gradient">
      mdi-arrow-right-thick
    </v-icon>
  </v-btn>
</template>
<script>
export default {
  methods: {
    submit: function(){
      this.$emit('submit');
    },
  },
}
</script>
