<template>
    <div>
        <TheResultTextBox/>
        <TheResultAnimeInfo/>
        <v-btn>もう1回診断する</v-btn>
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