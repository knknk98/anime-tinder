<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols=12 md=3>
          <v-img
            :src="'data:image/jpg;base64,'+anime.image"
            aspect-ratio=0.75
            max-height=400
            max-width=300
          >
          </v-img>
        </v-col>
        <v-col cols=12 md=9>
          <v-expansion-panels flat class="mb-3">
            <v-expansion-panel>
              <v-expansion-panel-header><strong>概要</strong></v-expansion-panel-header>
              <v-expansion-panel-content>
                  <p>{{anime.description}}</p>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
          <br/>
          <v-expansion-panels flat class="mb-3">
            <v-expansion-panel>
              <v-expansion-panel-header><strong>キャスト/スタッフ</strong></v-expansion-panel-header>
              <v-expansion-panel-content>
                <p>[制作会社]{{anime.company}}</p>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
          <!--ハッシュタグ・動画リンク-->
          <div>
            <v-row>
              <v-col cols=12 md=8>
                <h4>{{anime.genre}}</h4>
                <v-btn :href="'https://anime.dmkt-sp.jp/animestore/sch_pc?searchKey='+anime.title+'=svod_tvod'" target="_blank" rel="noopener noreferrer" style="text-transform: none" color="#EB5528" dark x-small>
                  <strong>dアニメストア</strong></v-btn>
                <v-btn :href="'https://www.amazon.co.jp/s?k='+anime.title+'&i=instant-video'" target="_blank" rel="noopener noreferrer" style="text-transform: none" color="#01A7E1" dark x-small>
                  Amazon Prime Video
                </v-btn>
              </v-col>
              <v-col cols=12 md=4>
                <v-btn @click="restart" block color="white" class="mt-2"><strong>もう1度探す</strong></v-btn>
              </v-col>
            </v-row>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
export default {
  props:{
    anime: Object,
  },
  methods: {
    restart: function () {
      this.$router.push('/');
    },
  }
};
</script>
