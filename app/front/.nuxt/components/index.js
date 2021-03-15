export { default as LoginButton } from '../../components/LoginButton.vue'

export const LazyLoginButton = import('../../components/LoginButton.vue' /* webpackChunkName: "components/login-button" */).then(c => c.default || c)
