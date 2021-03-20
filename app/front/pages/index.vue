<template>
  <div class="box home-background">
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
      <NopeButton/>
      <SuperLikeButton/>
      <LikeButton/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NopeButton from '@/components/NopeButton';
import SuperLikeButton from '@/components/SuperLikeButton';
import LikeButton from '@/components/LikeButton';

export default {
  middleware: 'authenticated',
  components: {
    NopeButton,
    SuperLikeButton,
    LikeButton,
  },
  data() {
    return {
      name: 'index',
    }
  },
  head() {
    return {
      title: '',
    }
  },
};
</script>
