export { default as LoginButton } from '../../components/LoginButton.vue'
export { default as TheResultAnimeInfo } from '../../components/TheResultAnimeInfo.vue'
export { default as TheResultTextBox } from '../../components/TheResultTextBox.vue'

export const LazyLoginButton = import('../../components/LoginButton.vue' /* webpackChunkName: "components/login-button" */).then(c => c.default || c)
export const LazyTheResultAnimeInfo = import('../../components/TheResultAnimeInfo.vue' /* webpackChunkName: "components/the-result-anime-info" */).then(c => c.default || c)
export const LazyTheResultTextBox = import('../../components/TheResultTextBox.vue' /* webpackChunkName: "components/the-result-text-box" */).then(c => c.default || c)
