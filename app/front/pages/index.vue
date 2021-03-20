<template>
  <div>
    <Loading v-show="loading"></Loading>
    <div class="box home-background" v-show="!loading">
      <v-row justify="center" align="center">
        <v-col cols="12" sm="8" md="6">
          <v-card>
            <v-card-title class="header-title">
            </v-card-title>
            <v-card-text>
            </v-card-text>
            <v-card-actions>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
      <div id="buttons">
        <NopeButton @nope="nope"></NopeButton>
        <SuperLikeButton @superlike="superlike"></SuperLikeButton>
        <LikeButton @like="like"></LikeButton>
        <SubmitButton @submit="submit"></SubmitButton>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Loading from '@/components/Loading';
import NopeButton from '@/components/NopeButton';
import SuperLikeButton from '@/components/SuperLikeButton';
import LikeButton from '@/components/LikeButton';
import SubmitButton from '@/components/SubmitButton';

export default {
  middleware: 'authenticated',
  components: {
    Loading,
    NopeButton,
    SuperLikeButton,
    LikeButton,
    SubmitButton
  },
  data() {
    return {
      name: 'index',
      animedata: [],
      loading: false,
    }
  },
  head() {
    return {
      title: '',
    }
  },
  methods: {
    nope: function(){
      this.$router.push("/");
    },
    superlike: function(){
      this.$router.push("/");
    },
    like: function(){
      this.$router.push("/");
    },
    submit: function(){
      this.$router.replace({ name: 'result' });
    },
  },
};
</script>
