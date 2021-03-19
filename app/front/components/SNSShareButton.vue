<template>
  <div>
    <a href="https://twitter.com/share?ref_src=twsrc%5Etfw"
      class="twitter-share-button"
      data-size="large"
      data-text="ツイート文を表示する"
      data-url="https://TEST.com"
      data-hashtags="aaaaaa,bbb,ccc"
      data-lang="ja"
      data-show-count="false">
    </a>
    <script src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <v-container fluid>
      <v-textarea
        name="input-7-1"
        filled
        label="コピペ用"
        auto-grow
        :rules="rules"
        :value="value"
        counter
        background-color="white"
        append-icon="mdi-content-copy"
        @click:append="writeToClipboard"
        clearable
      ></v-textarea>
    </v-container>
  </div>
</template>


<script>
  export default {
    data: () => ({
      rules: [v => v.length <= 140 || 'Max 140 characters'],
      value: "ここにツイート文を表示",
    }),
    method: {
      writeToClipboard() {
      },
    },
  }
</script>


