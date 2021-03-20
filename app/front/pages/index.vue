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
  </div>
</template>

<script>
import axios from 'axios';

export default {
  middleware: 'authenticated',
  head() {
    return {
      title: '',
    }
  },
};
</script>
