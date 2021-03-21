export const state = () => ({
  authUser: null,
  userName: null,
  userImage: null,
  isBeginner: true,
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
  setStarted(state, isBeginner) {
    state.isBeginner = isBeginner;
  },
};