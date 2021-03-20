export const state = () => ({
  authUser: null,
  userName: null,
  userImage: null,
  accessed: true,
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
  setAccessed(state, accessed) {
    state.accessed = accessed;
  },
};