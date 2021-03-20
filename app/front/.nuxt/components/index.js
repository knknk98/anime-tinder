export { default as CaptionBox } from '../../components/CaptionBox.vue'
export { default as Loading } from '../../components/Loading.vue'
export { default as LoginButton } from '../../components/LoginButton.vue'
export { default as NavSideBar } from '../../components/NavSideBar.vue'
export { default as SNSShareButton } from '../../components/SNSShareButton.vue'
export { default as TheResultAnimeInfo } from '../../components/TheResultAnimeInfo.vue'
export { default as TheResultTextBox } from '../../components/TheResultTextBox.vue'

export const LazyCaptionBox = import('../../components/CaptionBox.vue' /* webpackChunkName: "components/caption-box" */).then(c => c.default || c)
export const LazyLoading = import('../../components/Loading.vue' /* webpackChunkName: "components/loading" */).then(c => c.default || c)
export const LazyLoginButton = import('../../components/LoginButton.vue' /* webpackChunkName: "components/login-button" */).then(c => c.default || c)
export const LazyNavSideBar = import('../../components/NavSideBar.vue' /* webpackChunkName: "components/nav-side-bar" */).then(c => c.default || c)
export const LazySNSShareButton = import('../../components/SNSShareButton.vue' /* webpackChunkName: "components/s-n-s-share-button" */).then(c => c.default || c)
export const LazyTheResultAnimeInfo = import('../../components/TheResultAnimeInfo.vue' /* webpackChunkName: "components/the-result-anime-info" */).then(c => c.default || c)
export const LazyTheResultTextBox = import('../../components/TheResultTextBox.vue' /* webpackChunkName: "components/the-result-text-box" */).then(c => c.default || c)
