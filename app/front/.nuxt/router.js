import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _5fa2fc1a = () => interopDefault(import('../pages/callback.vue' /* webpackChunkName: "pages/callback" */))
const _631fc3ab = () => interopDefault(import('../pages/login.vue' /* webpackChunkName: "pages/login" */))
const _17718d8e = () => interopDefault(import('../pages/result/index.vue' /* webpackChunkName: "pages/result/index" */))
const _41819b76 = () => interopDefault(import('../pages/result/_id.vue' /* webpackChunkName: "pages/result/_id" */))
const _cd0fbed8 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/callback",
    component: _5fa2fc1a,
    name: "callback"
  }, {
    path: "/login",
    component: _631fc3ab,
    name: "login"
  }, {
    path: "/result",
    component: _17718d8e,
    name: "result"
  }, {
    path: "/result/:id",
    component: _41819b76,
    name: "result-id"
  }, {
    path: "/",
    component: _cd0fbed8,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config.app && config.app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
