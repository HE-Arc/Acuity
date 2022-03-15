import axios from 'axios'
import { createApp } from 'vue/dist/vue.esm-bundler'
import App from './App.vue'
import router from './router/index.js'
import store from './store/index.js'
import './assets/style.css';
import Qui from '@qvant/qui-max';
import '@qvant/qui-max/styles';

axios.defaults.baseURL = 'http://localhost:8000/'

createApp(App).use(Qui).use(store).use(router, axios).mount('#app')
