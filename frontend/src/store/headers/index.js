export let header_getters, header_mutations, headers_state;


header_getters = {
  menu_open_state: state=> state.menuOpen
};

header_mutations = {
  setMenuOpen: (state, value)=>state.menuOpen = value,
};

headers_state = {
  menuOpen: false,
};
