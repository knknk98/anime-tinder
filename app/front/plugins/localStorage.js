import createPersistedState from 'vuex-persistedstate'
 
export default ({ store }) => {
    window.onNuxtReady(() => {
        createPersistedState({
            key: 'animeRecommend'
        })(store)
    })
}