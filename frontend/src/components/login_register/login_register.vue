<template>
  <div class="w-100">
    <div class="text-center container">
      <form class="form-signin" method="post" @click.prevent>
        <h1 class="h3 mb-3 font-weight-normal">请登录</h1>
        <label for="inputId" class="sr-only">用户名</label>
        <input type="text" id="inputId" v-model="username" class="form-control" placeholder="用户名" name="username" required autofocus autocomplete>
        <label for="inputPassword" class="sr-only">密码</label>
        <input type="password" id="inputPassword" v-model="password" class="form-control" placeholder="密码" name="password" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit" @click="login">登录</button>
        <p class="mt-5 mb-3 text-muted">&copy; 2017-2019</p>
      </form>
      <router-link :to="{name: 'register'}">注册</router-link>
    </div>
  </div>
</template>

<script>
  import {login_state_mapGetters, login_state_mapMutations} from "../../store/login_state";

  export default {
    name: "login_register",
    data(){
      return {
        username: '',
        password: '',
      }
    },
    created() {
    },
    computed: {
      ...login_state_mapGetters,
    },
    methods: {
      ...login_state_mapMutations,
      login(){
        let param = new URLSearchParams();
        param.append('username', this.username);
        param.append('password', this.password);
        this.axios.post(
          this.$route.meta.path,
          param
        ).then(res=>{
          if(res.data.status === 200){
            sessionStorage.token = res.data.token;
            localStorage.token = res.data.token;
            this.setToken(res.data.token);
            this.setLoginState(true);
            this.setUser(res.data.user);
            setTimeout(()=>this.$router.replace({name: 'contest'}), 1000);
          }
          else
            alert(res.data.msg);
        })

      },
    }
  }
</script>

<style scoped>
  .form-signin {width: 100%;max-width: 330px;padding: 15px;margin: auto;margin-top: 5em;}
  .form-signin .checkbox {font-weight: 400;}
  .form-signin .form-control {position: relative;box-sizing: border-box;height: auto;padding: 10px;font-size: 16px;}
  .form-signin .form-control:focus {z-index: 2;}
  .form-signin h1 {margin-bottom: 1.5em!important;}
  .form-signin input[type="text"] {margin-bottom: 10px;border-bottom-right-radius: 0;border-bottom-left-radius: 0;}
  .form-signin input[type="password"] {margin-bottom: 10px;border-top-left-radius: 0;border-top-right-radius: 0;}
</style>
