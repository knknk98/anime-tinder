<template>
  <v-tooltip top>
    <template v-slot:activator="{ on, attrs }">
    <v-btn
      class="mx-2"
      fab
      small
      @click="like"
      v-bind="attrs" v-on="on"
    >
      <v-icon id="like-gradient">
        mdi-circle-outline
      </v-icon>
    </v-btn>
    </template>
    <span>すき</span>
  </v-tooltip>
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
