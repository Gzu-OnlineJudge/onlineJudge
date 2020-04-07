export let login_state_mapGetters, login_state_mapMutations, login_state_mapActions;

import {mapMutations, mapGetters, mapActions} from "vuex";

login_state_mapGetters = {
  ...mapGetters([
    'loginState',
    'user',
    'token',
  ])
};


login_state_mapMutations = {
  ...mapMutations([
    'setLoginState',
    'setUser',
    'setToken',
  ]),
};


login_state_mapActions = {
  ...mapActions([
    'logout'
  ])
}
