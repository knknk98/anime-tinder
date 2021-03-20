<template>
  <div id="container">
    <div id="login-gridA">
      <div class="block-box">
        <h1>タイトル</h1>
        <h2 class="catchcopy">オタクは急展開する。<br>アニメひとつで。</h2>
        <br><br>
        <LoginButton/>
      </div>
    </div>
    <div id="login-gridB" class="horizontal-gradient"></div>
    <div id="login-gridC" class="horizontal-gradient"></div>
  </div>
</template>
<script>
import LoginButton from '~/components/LoginButton.vue'
export default {
  // middleware: 'authenticated',
  components: {
    LoginButton
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