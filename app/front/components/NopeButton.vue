<template>
  <v-tooltip top>
    <template v-slot:activator="{ on, attrs }">
    <v-btn
      class="mx-2"
      fab
      small
      @click="nope"
      v-bind="attrs" v-on="on"
    >
      <v-icon id="nope-gradient">
        mdi-close
      </v-icon>
    </v-btn>
    </template>
    <span>きらい</span>
  </v-tooltip>
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
