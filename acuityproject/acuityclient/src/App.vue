<template>
  <div id="main">
    <router-link to="/">go home</router-link>
    <router-link to="/about">go about</router-link>
    <router-link to="/log-in">Log in</router-link>
    <router-link to="/sign-up">Sign up</router-link>
    <router-view></router-view>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: "App",
  beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if(token){
      axios.defaults.headers.common['Authorization'] = "Token " + token
    }else{
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  components: {
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
