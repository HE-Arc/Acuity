<template>
  <div class="home-page">
    <h1>Acuity</h1>
    <h3>Homepage</h3>
        
    <ul>
      <li v-for="user in users" :key="user">
        {{user.first_name}}
      </li>
    </ul>

  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      users: [],
    };
  },
  methods: {
    getInitialUsers() {
      axios.get('http://localhost:8000/api/users/?results=2').then((response) => {
        this.users = response.data;
      });
    },
  },
  beforeMount() {
    this.getInitialUsers();
  },
};
</script>
