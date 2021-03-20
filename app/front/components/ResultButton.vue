<template>
  <v-tooltip top>
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        class="mx-2 button-orange"
        fab
        small
        color="red"
        @click="result"
        v-bind="attrs" v-on="on"
      >
        <v-icon id="submit-gradient">
          mdi-arrow-right-thick
        </v-icon>
      </v-btn>
    </template>
    <span>診断結果を見る</span>
  </v-tooltip>
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
