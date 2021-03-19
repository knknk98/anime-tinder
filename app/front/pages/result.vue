<template>
    <div class="home-background pa-5">
        <TheResultTextBox/>
        <TheResultAnimeInfo/>
        <v-btn class="ma-3">もう1回診断する</v-btn>
        <CaptionBox title="結果をツイートする" />
        <TweetButton/>
        <CaptionBox title="みんなの診断結果" />
    </div>
</template>

<script>
import TheResultTextBox from '~/components/TheResultTextBox.vue'
import TheResultAnimeInfo from '~/components/TheResultAnimeInfo.vue'
import CaptionBox from '~/components/CaptionBox.vue'
import TweetButton from '~/components/TweetButton.vue'

export default {
  // middleware: 'authenticated',
  components: {
      TheResultTextBox,
      TheResultAnimeInfo,
      CaptionBox,
      TweetButton,
  }
}
</script>