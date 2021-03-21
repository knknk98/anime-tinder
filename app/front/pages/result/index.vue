<template>
  <div>
    <Loading v-show="loading"></Loading>
    <div class="home-background mt-5" v-show="!loading">
      <TheResultTextBox :title="animeInfo.title"/>
      <TheResultAnimeInfo :anime="animeInfo"/>
      <CaptionBox title="結果をシェアする" />
      <SNSShareButton :title="animeInfo.title"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Loading from '@/components/Loading';
import TheResultTextBox from '~/components/TheResultTextBox.vue'
import TheResultAnimeInfo from '~/components/TheResultAnimeInfo.vue'
import SNSShareButton from '~/components/SNSShareButton.vue'

export default {
  middleware: 'authenticated',
  components: {
    Loading,
    TheResultTextBox,
    TheResultAnimeInfo,
    SNSShareButton,
  },
  data() {
    return {
      name: 'result',
      loading: true,
      animeInfo: {},
    }
  },
  async mounted() {
    var animeId = this.$route.query.id;
    await axios.post(this.$config.serverURL+'/app/fetch', {
      animeId: animeId,
      sessionID: this.$store.state.authUser,
    }).then(res => {
      this.animeInfo = res.data.animes[0];
      this.loading = false;
    }).catch(err => {
    });
  },
}
</script>