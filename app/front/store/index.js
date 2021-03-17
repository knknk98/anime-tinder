export const state = () => ({
  authUser: null,
});

export const mutations = {
  setUser(state, authUser) {
    state.authUser = authUser;
  },
};

// export const actions = {
//   SPAモードでは非対応
//   nuxtServerInit({ commit }, { req }) {
//     if (req.session && req.session.user) {
//       commit("setUser", req.session.user);
//     }
//   }
// };