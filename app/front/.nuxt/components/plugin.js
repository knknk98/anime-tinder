import Vue from 'vue'

const components = {
  LoginButton: () => import('../../components/LoginButton.vue' /* webpackChunkName: "components/login-button" */).then(c => c.default || c),
  TheResultBox: () => import('../../components/TheResultBox.vue' /* webpackChunkName: "components/the-result-box" */).then(c => c.default || c)
}

for (const name in components) {
  Vue.component(name, components[name])
  Vue.component('Lazy' + name, components[name])
}
