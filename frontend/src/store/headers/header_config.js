export let header_mapGetters, header_mapMutations;

import {mapGetters, mapMutations} from "vuex";

header_mapGetters = {
  ...mapGetters([
    'menu_open_state'
  ]),
};

header_mapMutations = {
  ...mapMutations([
    'setMenuOpen',
  ])
};
