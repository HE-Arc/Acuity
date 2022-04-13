import axios from 'axios'
import { createApp } from 'vue/dist/vue.esm-bundler'
import App from './App.vue'
import router from './router/index.js'
import store from './store/index.js'
import './assets/style.css';
import Qui from '@qvant/qui-max';
import '@qvant/qui-max/styles';
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

createApp(App).use(VueSweetalert2).use(Qui).use(store).use(router, axios).mount('#app')