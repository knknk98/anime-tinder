<template>
    <div>
        <TheResultTextBox/>
        <TheResultAnimeInfo/>
        <v-card>もう1回診断する</v-card>
    </div>
</template>

<script>
import TheResultTextBox from '~/components/TheResultTextBox.vue'
import TheResultAnimeInfo from '~/components/TheResultAnimeInfo.vue'
export default {
  // middleware: 'authenticated',
  components: {
      TheResultTextBox,
      TheResultAnimeInfo,
  }
}
</script>