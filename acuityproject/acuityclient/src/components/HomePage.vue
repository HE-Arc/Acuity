<template>
  <div class="home-page">
    <main-header></main-header>
    <div class="column">
      <div v-if="is_dsc" class="item h20 direction-column">
        <h3>Here are the <label class="accent-text">worst</label> citizens</h3>
        <p>
          Check the
          <a @click="is_dsc = false; this.getBestUsers();">
            bests
          </a>
        </p>
      </div>
      <div v-if="!is_dsc" class="item h20 direction-column">
        <h3>Here are the <label class="accent-text">bests</label> citizens</h3>
        <p>
          Check the
          <a @click="is_dsc = true; this.getWorstUsers();">
            worsts
            </a>
        </p>
      </div>
      <div class="item h60">
        <div class="users-list h100">
          <button
            v-for="user in users" :key="user" @click="toUserPage(user.id)" class="user-button w100 h10">
            <div class="column-list user-name">
              {{ user.first_name }} {{ user.last_name }}
            </div>
            <div class="column-list score-mean">
              {{ user.score_mean.toFixed(1) }}
            </div>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import MainHeader from "./MainHeader.vue";

export default {
  components: { MainHeader },
  data() {
    return {
      users: [],
      is_dsc: false,
    };
  },
  methods: {
    toUserPage(userId) {
      const connected = localStorage.getItem("token");
      if (connected === null) 
        this.$router.push("/log-in");
      else 
        this.$router.push("/users/" + userId);
    },

    getBestUsers() {
      axios
        .get(this.$router.routeApi("/users/best_users/"))
        .then((response) => {
          this.users = response.data;
        });
    },
    getWorstUsers() {
      axios
        .get(this.$router.routeApi("/users/worst_users/"))
        .then((response) => {
          this.users = response.data;
        });
    },
  },
  beforeMount() {
    this.getBestUsers();
  },
};
</script>
