<template>
  <div class="home-page">
    <h1>Acuity</h1>
    <h3>Homepage</h3>
        
      <div class="users-list row">
          <button v-for="user in users" :key="user" class="user-button w100">
            <div class="column-list user-name">
                {{ user.first_name }}
            </div>
            <div class="column-list score-mean">
                {{ user.score_mean.toFixed(1) }}
            </div>
          </button>
      </div>
    <div class="row">
      <q-button class="colmun" :theme="[is_dsc ? '' : 'secondary']" @click="is_dsc=true; this.getBestUsers()">
        Bests
      </q-button>
      <q-button class="column" :theme="[is_dsc ? 'secondary' : '']" @click="is_dsc=false; this.getWorstUsers()">
        Worsts
      </q-button>
    </div>
    <div>
      <q-button>
        Scan
      </q-button>

    </div>

  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      users: [],
      is_dsc: true,
    };
  },
  methods: {
    getBestUsers() {
      axios.get('http://localhost:8000/api/users/best_users/').then((response) => {
        this.users = response.data;
      });
    },
    getWorstUsers() {
      axios.get('http://localhost:8000/api/users/worst_users/').then((response) => {
        this.users = response.data;
      });
    },
  },
  beforeMount() {
    this.getBestUsers();
  }
};
</script>
