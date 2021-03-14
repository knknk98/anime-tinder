// ログイン前のユーザーは/loginにリダイレクト
export default function ({ route, store, redirect }) {
  if(route.name !== 'login' && !store.state.authUser) { // ログイン済みでない、かつ/login以外にアクセス
    redirect({ name: 'login' });
  }
}