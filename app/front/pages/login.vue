<template>
  <div id="container">
    <div id="login-gridA" class="box">
      <h1>ここにタイトルを入れる。</h1>
      <h2>オタクは急展開する。アニメひとつで。</h2>
      <LoginButton/>
    </div>
    <div id="login-gridB" class="horizontal-gradient box">B</div>
    <div id="login-gridC" class="horizontal-gradient box">C</div>
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