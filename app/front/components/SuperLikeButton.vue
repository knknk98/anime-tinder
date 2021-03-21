<template>
  <v-tooltip top>
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        class="mx-2"
        fab
        small
        @click="superlike"
        v-bind="attrs" v-on="on"
      >
        <v-icon id="superlike-gradient">
          mdi-heart
        </v-icon>
      </v-btn>
    </template>
    <span>だいすき</span>
  </v-tooltip>
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
