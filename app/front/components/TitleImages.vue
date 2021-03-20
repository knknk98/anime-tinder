<template>
  <v-carousel
    cycle
    height=800
    hide-delimiter-background
    hide-delimiters
    :show-arrows="false"
    interval=3000
  >
    <v-carousel-item
      v-for="(image_src,i) in image_srcs"
      :key="i"
      transition="fade-transition"
    >
    <v-img :src="image_src"></v-img>

    </v-carousel-item>
  </v-carousel>
</template>

<script>
  export default {
    data () {
      return {
        image_srcs: [
            require("@/assets/image/title1.png"),
            require("@/assets/image/title2.png"),
            require("@/assets/image/title3.png"),
        ]
      }
    },
  }
</script>