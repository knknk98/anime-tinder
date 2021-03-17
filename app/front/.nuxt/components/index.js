export { default as LoginButton } from '../../components/LoginButton.vue'
export { default as NavSideBar } from '../../components/NavSideBar.vue'

export const LazyLoginButton = import('../../components/LoginButton.vue' /* webpackChunkName: "components/login-button" */).then(c => c.default || c)
export const LazyNavSideBar = import('../../components/NavSideBar.vue' /* webpackChunkName: "components/nav-side-bar" */).then(c => c.default || c)
