export { default as NavBar } from '../../components/NavBar.vue'

export const LazyNavBar = import('../../components/NavBar.vue' /* webpackChunkName: "components/nav-bar" */).then(c => c.default || c)
