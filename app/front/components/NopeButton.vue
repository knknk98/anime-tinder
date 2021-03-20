<template>
  <v-btn
    class="mx-2"
    fab
    small
  >
    <v-icon id="nope-gradient">
      mdi-close
    </v-icon>
  </v-btn>
</template>
<script>
export default {
  data() {
  },
  methods: {
    nope: function(){
      this.$router.push('/');
    }
  },
}
</script>
