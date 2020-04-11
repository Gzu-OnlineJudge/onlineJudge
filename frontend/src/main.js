// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from "./store";
import axios from 'axios';
import vueAxios from 'vue-axios';
import 'bootstrap';


axios.defaults.baseURL='http://192.168.0.101:8000/api/';
axios.defaults.headers.common['Authorization'] = 'JWT ' + (sessionStorage.token || localStorage.token);


Vue.use(vueAxios, axios);
Vue.config.productionTip = false;

/* eslint-disable no-new */

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min'
import Router from "vue-router";

router.beforeEach((to, from, next) => {
  let params = to.params;
  for(let key in params){
    to.meta.path = to.meta.path.replace(':'+key, params[key]);
  }
  next();
});

Date.prototype.format = function (fmt) {
  /**
   * (new Date()).pattern("yyyy-MM-dd hh:mm:ss.S") ==> 2006-07-02 08:09:04.423
   * (new Date()).pattern("yyyy-MM-dd E HH:mm:ss") ==> 2009-03-10 二 20:09:04
   * (new Date()).pattern("yyyy-MM-dd EE hh:mm:ss") ==> 2009-03-10 周二 08:09:04
   * (new Date()).pattern("yyyy-MM-dd EEE hh:mm:ss") ==> 2009-03-10 星期二 08:09:04
   * (new Date()).pattern("yyyy-M-d h:m:s.S") ==> 2006-7-2 8:9:4.18
   **/
  let value = this;
  value = value || new Date();
  var o = {
    "M+" : value.getMonth()+1, //月份
    "d+" : value.getDate(), //日
    "h+" : value.getHours()%12 == 0 ? 12 : value.getHours()%12, //小时
    "H+" : value.getHours(), //小时
    "m+" : value.getMinutes(), //分
    "s+" : value.getSeconds(), //秒
    "q+" : Math.floor((value.getMonth()+3)/3), //季度
    "S" : value.getMilliseconds() //毫秒
  };
  var week = {
    "0" : "/u65e5",
    "1" : "/u4e00",
    "2" : "/u4e8c",
    "3" : "/u4e09",
    "4" : "/u56db",
    "5" : "/u4e94",
    "6" : "/u516d"
  };
  if(/(y+)/.test(fmt)){
    fmt=fmt.replace(RegExp.$1, (value.getFullYear()+"").substr(4 - RegExp.$1.length));
  }
  if(/(E+)/.test(fmt)){
    fmt=fmt.replace(RegExp.$1, ((RegExp.$1.length>1) ? (RegExp.$1.length>2 ? "/u661f/u671f" : "/u5468") : "")+week[value.getDay()+""]);
  }
  for(var k in o){
    if(new RegExp("("+ k +")").test(fmt)){
      fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
    }
  }
  return fmt;
}

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
