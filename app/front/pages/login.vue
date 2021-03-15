<template>
  <div id="container">
    <div id="login-gridA">
      <div class="block-box">
        <h1>ここにタイトルを入れる。</h1>
        <h2 class="catchcopy">オタクは急展開する。アニメひとつで。</h2>
        <br><br>
        <LoginButton/>
      </div>
    </div>
    <div id="login-gridB" class="horizontal-gradient">
      B
    </div>
    <div id="login-gridC" class="horizontal-gradient">
      C
    </div>
  </div>
</template>
<script>
import LoginButton from '~/components/LoginButton.vue'
export default {
  // middleware: 'authenticated',
  components: {
    LoginButton
  }
}
</script>