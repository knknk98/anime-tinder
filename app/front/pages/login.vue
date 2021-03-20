<template>
  <div id="container">
    <div id="login-gridA">
      <div class="block-box">
          <div class="pa-md-10">
          <h1>タイトル</h1>
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
  // middleware: 'authenticated',
  components: {
<<<<<<< HEAD
    LoginButton,
    TitleImages,
=======
    LoginButton
>>>>>>> 6ebd33045fd00a86fae0bb9ad89c75d4275b8b9b
  },
  data() {
    return {
      name: 'login',
    }
  },
  head() {
    return {
      title: 'ログイン・',
    }
  },
}
</script>