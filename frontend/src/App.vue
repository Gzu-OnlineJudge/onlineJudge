<template>
  <div>
    <v-header></v-header>
    <main class="position-relative">
      <v-sidebar></v-sidebar>
      <div class="main-content">
        <v-breadcrumb></v-breadcrumb>
        <router-view/>
      </div>
    </main>
  </div>
</template>

<script>
  import sidebar from "./components/sidebar";
  import headers from "./components/headers";
  import breadcrumb from "./components/breadcrumb";
  export default {
    name: 'App',
    components: {
      'v-sidebar': sidebar,
      'v-header': headers,
      'v-breadcrumb': breadcrumb
    }
  }
</script>


