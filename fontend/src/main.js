// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from "./store";
import axios from 'axios';
import vueAxios from 'vue-axios';
import $ from 'jquery';
import 'bootstrap';

Vue.use(vueAxios, axios);
Vue.config.productionTip = false;

/* eslint-disable no-new */

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min'

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
