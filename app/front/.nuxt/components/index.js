export { default as LoginButton } from '../../components/LoginButton.vue'
export { default as TheResultBox } from '../../components/TheResultBox.vue'

export const LazyLoginButton = import('../../components/LoginButton.vue' /* webpackChunkName: "components/login-button" */).then(c => c.default || c)
export const LazyTheResultBox = import('../../components/TheResultBox.vue' /* webpackChunkName: "components/the-result-box" */).then(c => c.default || c)
