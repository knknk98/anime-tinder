<template>
  <div>

    <v-btn @click="share('twitter')">Twitterでシェア</v-btn>
    <v-btn @click="share('facebook')">Facebookでシェア</v-btn>
    <v-btn @click="share('line')">Lineでシェア</v-btn>
    <v-btn @click="share('hatena')">はてなでシェア</v-btn>

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
        clearable
      ></v-textarea>
    </v-container>
  </div>
</template>


<script>
  export default {
    data: () => ({
      rules: [v => !!v || '',
              v => (!!v && v.length <= 140) || `Max 140 characters`],
      text: "ここにツイート文を表示",
      hashtag: "aaa,bbb",
      value: "ここにツイート文を表示 #aaa #bbb",
    }),
    methods: {
      share(sns) {
        const shareUrl = "https://example.com"
        let href = ""
        switch( sns ) {
          case 'twitter':
              href = `https://twitter.com/intent/tweet?url=${shareUrl}&hashtags=`+this.hashtag+`&text=`+this.text
              break
          case 'facebook':
              href = `https://www.facebook.com/sharer/sharer.php?u=${shareUrl}`
              break
          case 'line':
              href = `https://line.me/R/msg/text/?`+this.text
              break
          case 'hatena':
              href = `http://b.hatena.ne.jp/add?&url=${shareUrl}`
              break
        }
        if(sns=="line"){
          window.open(href, '_blank')
        }else{
          window.open(href, '_blank',"rel=nofollow noopener noreferrer")
        }
      }
    }
  }
</script>


