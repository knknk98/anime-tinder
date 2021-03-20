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
      v-for="(slide, i) in slides"
      :key="i"
      transition="fade-transition"
    >
      <v-sheet
        :color="colors[i]"
        height="100%"
        width = "100%"
        tile
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="display-3">
            {{ slide }} Slide
          </div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
  export default {
    data () {
      return {
        colors: [
          'indigo',
          'warning',
          'pink darken-2',
          'red lighten-1',
          'deep-purple accent-4',
        ],
        slides: [
          'First',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
        ],
      }
    },
  }
</script>