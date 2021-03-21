<template>
  <div id="container">
    <div id="login-gridA">
      <div class="block-box">
          <div class="pa-md-10">
          <strong class="text-h1">Toonder</strong>
          <h2 class="catchcopy">オタクは急展開する。<br>アニメひとつで。</h2>
          <br/>
          <LoginButton/>
          </div>
        </div>
      </div>
      <div id="login-gridB"><TitleImages/></div>
    </div>
</template>

<script>
import LoginButton from '~/components/LoginButton.vue'
import TitleImages from '~/components/TitleImages.vue'
export default {
  components: {
    LoginButton,
    TitleImages,
  },
  data() {
    return {
      name: 'login',
      image_srcs: [
          require("@/assets/image/logo.PNG"),
      ]
    }
  },
  head() {
    return {
      title: 'ログイン・',
    }
  },
}
</script>