export const state = () => ({
  authUser: null,
  userName: null,
  userImage: null,
});

export const mutations = {
  setAuthUser(state, authUser) {
    state.authUser = authUser;
  },
  setUserName(state, userName) {
    state.userName = userName;
  },
  setUserImage(state, userImage) {
    state.userImage = userImage;
  },
};