import Vue from 'vue'
import Router from 'vue-router'
import contest from "../components/contest/contest";
import contestContent from "../components/contest/contestContent";
import login_register from "../components/login_register/login_register";
import register from '../components/login_register/register'
import contestProblem from "../components/contest/contestProblem";
import userInfo from "../components/uer/userInfo";
import problem from "../components/problem/problem";
import status from "../components/submit_status/status";
import contestProblemCode from "../components/contest/contestProblemCode";



Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    /*******************比赛模块路由****************/
    {
      path: '/',
      redirect: '/contest/'
    },
    {
      /**
       * 比赛列表
       */
      path: '/contest/',
      name: 'contest',
      component: contest,
      meta: {
        name: '比赛列表',
        path: '/contest/',
        index: 1,
        parent: undefined,
        nameHandler: undefined,
      },
    },
    {
      /**
       * 比赛内容
       */
      path: '/contest/:contest_id/',
      name: 'contestContent',
      component: contestContent,
      params: {contest_id: 1},
      meta: {
        name: 'Round ',
        path: '/contest/:contest_id/',
        index: 2,
        parent: {path: '/contest/', name: 'contest'},
        nameHandler:(name, params)=>{
          return name + params['contest_id'];
        }
      },
    },
    {
      /**
       * 比赛题目
       */
      path: '/contest/:contest_id/problem/:problem_id/',
      name: 'contestProblem',
      component: contestProblem,
      meta: {
        name: '',
        path: '/contest/:contest_id/problem/:problem_id/',
        index: 3,
        parent: {path: '/contest/:contest_id/', name: 'contestContent'},
        nameHandle: undefined,
      },
    },
    {
      path: '/contest/:contest_id/status/:run_id/code/',
      name: 'contestProblemCode',
      component: contestProblemCode,
      meta: {
        name: '',
        path: '/contest/:contest_id/status/:run_id/code/',
        index: 3,
        parent: {path: '/contest/:contest_id/', name: 'contestContent'},
        nameHandler: (name, params)=>{
          return name + params['run_id'];
        },
      },
    },
    /*******************用户操作路由***********************/
    {
      path: '/login/',
      name: 'login',
      component: login_register,
      meta: {
        name: '登陆',
        path: '/login/',
        index: 1,
        parent: undefined,
        nameHandle: undefined,
      }
    },
    {
      path: '/register/',
      name: 'register',
      component: register,
      meta: {
        name: '注册',
        path: '/register/',
        index: 1,
        parent: undefined,
        nameHandle: undefined,
      }
    },
    {
      path: '/user/:user_id/',
      name: 'userInfo',
      component: userInfo,
      meta: {
        name: '个人中心',
        path: '/user/:user_id/',
        index: 1,
        parent: undefined,
        nameHandle: undefined,
      }
    },
    /*******************题库模块*******************************/
    {
      /**
       * 题目列表
       */
      path: '/problem/',
      name: 'problem',
      component: problem,
      meta: {
        name: '题库',
        path: '/problem/',
        index: 1, /* 一级目录 */
        parent: undefined,
        nameHandler: undefined,
      },
    },
    /*********************提交记录********************************/
    {
      /**
       * 提交记录
       */
      path: '/status/',
      name: 'status',
      component: status,
      meta: {
        name: '提交记录',
        path: '/status/',
        index: 1, /* 一级目录 */
        parent: undefined,
        nameHandler: undefined,
      },
    },
  ],
})
