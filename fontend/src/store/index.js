import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import {header_getters, header_mutations, headers_state} from "./headers/index";

const store = new Vuex.Store({
  state: {
    ...headers_state,
    user: {
      username: undefined,
      user_id: undefined
    },
    is_login: false,
    token: undefined,
  },
  getters: {
    ...header_getters,
    loginState: state => state.is_login,
    user: state => state.user,
    token: state => state.token,
  },
  mutations: {
    ...header_mutations,
    setLoginState: (state, value) => state.is_login = value,
    setUser: (state, value) => state.user = value,
    setToken: (state, value) => state.token = value,
  },
  actions: {
    logout:(context)=>{
      sessionStorage.removeItem('token');
      localStorage.removeItem('token');
      context.commit('setLoginState', false);
      context.commit('setToken', '');
      context.commit('setUser', {username: 'anyone', user_id: -1});
    }
  }
});

export default store;
