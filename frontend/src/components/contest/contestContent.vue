<template>
  <div class="w-100">
    <div class="w-100">
      <div class="w-100 bg-white shadow-sm">
        <div class="mt-0 w-100 container px-0">
          <ul :class="{'show': MenuShow}" class="nav-contest nav flex-column flex-md-row align-items-center position-relative">
            <li class="slide position-absolute"></li>
            <li @click="tab=1,MenuShow=false" class="nav-item" :class="tab==1?'active':''">
              <a class="nav-link" >比赛说明</a>
            </li>
            <li @click="tab=2,MenuShow=false" class="nav-item" :class="tab==2?'active':''">
              <a class="nav-link" >题目</a>
            </li>
            <li @click="tab=3,MenuShow=false" class="nav-item" :class="tab==3?'active':''">
              <a class="nav-link" >排名</a>
            </li>
            <li @click="tab=4,MenuShow=false, getStatusList()" class="nav-item" :class="tab==4?'active':''">
              <a class="nav-link" >提交记录</a>
            </li>
            <li @click="MenuShow=!MenuShow" class="bg-white position-absolute nav-item d-md-none w-100">
              <svg class="ml-3 mr-2" viewBox="0 0 1024 1024" width="18" height="21">
                <path fill="#8a8a8a" d="M919.8 381.1L555.2 779.8a57.377 57.377 0 0 1-43.1 19.5c-16.5 0-32.2-7.1-43.1-19.5L104.4 381.1c-17.8-18.8-23.3-46.2-14.1-70.4s31.4-41.1 57.2-43.4h728.9c25.9 2.2 48.2 19 57.4 43.3 9.3 24.3 3.8 51.6-14 70.5z" />
              </svg>
              {{tabActive}}
            </li>
          </ul>
        </div>
      </div>
      <div class="content-contest">
        <div class="w-100 px-0">
          <div class="container px-0">
            <div class="w-100 bg-white py-3 my-3">
              <div class="mb-3 d-flex justify-content-between">
                <div class="col-3 d-none d-md-flex justify-content-center align-items-center">
                  <span class="font-weight-bolder mr-1">开始时间 :</span>
                  {{contest.startTime}}
                </div>
                <div class="col-12 d-flex col-md-3 justify-content-center flex-wrap">
                  <h4 class="mr-2">Round 1 :</h4>
                  <h4>第一次月赛</h4>
                </div>
                <div class="col-3 col-3 d-none d-md-flex justify-content-center align-items-center">
                  <span class="font-weight-bolder mr-1">结束时间 :</span>
                  2019-2-28 19:30
                </div>
              </div>
              <div class="progress mx-3">
                <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
              </div>
            </div>
          </div>
          <div v-if="isStart" class="w-100 pb-5">
            <li v-show="tab == 1" class="container px-0" style="display: block">
              <div class="bg-white">
                {{contest.info}}
              </div>
            </li>
            <li v-show="tab == 2" class="container px-0" style="display: block">
              <div class="border-radius shadow">
                <table class="mb-0 table bg-white problem-list">
                  <thead class="thead-light">
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">标题</th>
                    <th scope="col">通过数</th>
                    <th scope="col">尝试数</th>
                    <th scope="col">通过率</th>
                    <th scope="col">是否通过</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr v-for="(i, index) in problems" :key="i.problem_id">
                    <th scope="row">{{index|format}}</th>
                    <td>
                      <router-link :to="{name: 'contestProblem', params: {contest_id: contest.id, problem_id: i.proNo}}">
                        {{i.title}}
                      </router-link>
                    </td>
                    <td>{{i.ac_num}}</td>
                    <td>{{i.total_num}}</td>
                    <td>{{isNaN(i.ac_num / i.total_num) ? 0 : i.ac_num / i.total_num}}</td>
                    <td>{{i % 5 == 0?'通过':'未通过'}}</td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </li>
            <li v-show="tab == 3" class="container px-0" style="display: block">
              <div class="w-100 d-flex px-0">
                <div class="input-group mb-3 col-6 col-md-2 px-1 outline-none-search">
                  <div class="input-group-prepend">
                    <svg viewBox="0 0 1024 1024" class="m-auto" width="30" height="30">
                      <path fill="#dadce0" d="M238.762667 238.805333a277.333333 277.333333 0 0 1 432.170666 341.632l141.056 141.056a64 64 0 1 1-90.538666 90.496l-141.013334-141.056A277.333333 277.333333 0 0 1 238.762667 238.805333zM299.136 299.093333a192 192 0 1 0 271.530667 0 192 192 0 0 0-271.530667 0z" />
                    </svg>
                  </div>
                  <input type="text" placeholder="按用户名搜索" class="form-control">
                </div>
                <div class="input-group mb-3 col-6 col-md-2 px-1 outline-none-search">
                  <div class="input-group-prepend">
                    <svg viewBox="0 0 1024 1024" class="m-auto" width="30" height="30">
                      <path fill="#dadce0" d="M238.762667 238.805333a277.333333 277.333333 0 0 1 432.170666 341.632l141.056 141.056a64 64 0 1 1-90.538666 90.496l-141.013334-141.056A277.333333 277.333333 0 0 1 238.762667 238.805333zM299.136 299.093333a192 192 0 1 0 271.530667 0 192 192 0 0 0-271.530667 0z" />
                    </svg>
                  </div>
                  <input type="text" placeholder="按学校搜索" class="form-control">
                </div>
              </div>
              <div class="row flex-nowrap justify-content-between mx-0 rank-list border-radius shadow tab-contest">
                <div class="px-0">
                  <table class="table bg-white">
                    <thead class="thead-light">
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">用户</th>
                      <th scope="col">AC</th>
                      <th scope="col">昵称</th>
                      <th scope="col">罚时</th>
                      <th scope="col">学校</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="i in 10" :key="i">
                      <td scope="row" v-html="setRank(i)"></td>
                      <td><router-link to="#">Gzuwkj</router-link></td>
                      <td>10</td>
                      <td>文坤建</td>
                      <td>03:14:50</td>
                      <td>贵州职业技术学院</td>
                    </tr>
                    </tbody>
                  </table>
                </div>
                <div class="px-0" ref="tableScreen">
                  <table class="table mb-0">
                    <thead class="thead-light">
                    <tr>
                      <th scope="col" v-for="i in 15" :key="i">{{i|format}}</th>
                    </tr>
                    </thead>
                    <tbody @mousedown="dragScroll($event)" ref="tableMove">
                    <tr v-for="i in 10" :key="i">
                      <td v-for="j in 15" :key="j"></td>
                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </li>
            <li v-show="tab == 4" class="container px-0" style="display: block">
              <div class="w-100 d-flex flex-wrap px-0">
                <div class="input-group mb-3 col-6 col-md-2 px-1 outline-none-search">
                  <div class="input-group-prepend">
                    <svg viewBox="0 0 1024 1024" class="m-auto" width="30" height="30">
                      <path fill="#dadce0" d="M238.762667 238.805333a277.333333 277.333333 0 0 1 432.170666 341.632l141.056 141.056a64 64 0 1 1-90.538666 90.496l-141.013334-141.056A277.333333 277.333333 0 0 1 238.762667 238.805333zM299.136 299.093333a192 192 0 1 0 271.530667 0 192 192 0 0 0-271.530667 0z" />
                    </svg>
                  </div>
                  <input type="text" placeholder="按用户名搜索" class="form-control">
                </div>
                <div @click.stop="downSelect($event)" class="input-group mb-3 col-3 col-md-2 col-lg-1 px-1 outline-none-search down-select-search">
                  <input type="text" placeholder="题目" class="form-control" readonly>
                  <div class="input-group-prepend">
                    <svg viewBox="0 0 1024 1024" width="30" height="30">
                      <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
                    </svg>
                  </div>
                  <div class="position-absolute w-100 bg-white shadow-sm">
                    <ul class="d-flex flex-column align-items-center p-0 m-0">
                      <li>全部</li>
                      <li v-for="i in problems.length" :key="i">{{i - 1|format}}</li>
                    </ul>
                  </div>
                </div>
                <div @click.stop="downSelect($event)" class="input-group mb-3 col-3 col-md-2 col-lg-1 px-1 outline-none-search down-select-search">
                  <input type="text" placeholder="语言" class="form-control" readonly>
                  <div class="input-group-prepend">
                    <svg viewBox="0 0 1024 1024" width="30" height="30">
                      <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
                    </svg>
                  </div>
                  <div class="position-absolute w-100 bg-white shadow-sm">
                    <ul class="d-flex flex-column align-items-center p-0 m-0">
                      <li>全部</li>
                      <li>C</li>
                      <li>C++</li>
                      <li>Java</li>
                    </ul>
                  </div>
                </div>
                <div @click.stop="downSelect($event)" class="input-group mb-3 col-4 col-md-2 px-1 outline-none-search down-select-search">
                  <input style="max-width: 7.5rem" type="text" placeholder="运行结果" class="form-control" readonly>
                  <div class="input-group-prepend">
                    <svg viewBox="0 0 1024 1024" width="30" height="30">
                      <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
                    </svg>
                  </div>
                  <div class="position-absolute w-100 bg-white shadow-sm">
                    <ul class="d-flex flex-column align-items-center p-0 m-0">
                      <li>全部</li>
                      <li>答案正确</li>
                      <li>答案错误</li>
                      <li>内存超限</li>
                      <li>时间超限</li>
                      <li>运行错误</li>
                      <li>编译错误</li>
                      <li>格式错误</li>
                      <li>输出超限</li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="status-list border-radius shadow tab-contest">
                <table class="mb-0 table bg-white">
                  <thead class="thead-light">
                  <tr>
                    <th scope="col">运行ID</th>
                    <th scope="col">用户名</th>
                    <th scope="col">题目</th>
                    <th scope="col">运行结果</th>
                    <th scope="col">运行时间(ms)</th>
                    <th scope="col">内存(KB)</th>
                    <th scope="col">语言</th>
                    <th scope="col">提交时间</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr v-for="(i, index) in statusList" :key="index">
                    <td  scope="row">{{i.runID}}</td>
                    <td><router-link to="#">{{i.user.user_name}}</router-link></td>
                    <td><router-link to="#">{{i.problem_id}}</router-link></td>
                    <td>
                      <router-link :to="{name: 'contestProblemCode', params: {contest_id: 1, run_id: 1}}">
                        {{i.result}}
                      </router-link>
                    </td>
                    <td>{{i.memory}}</td>
                    <td>{{i.time}}</td>
                    <td>{{i.language}}</td>
                    <td>{{i.subTime}}</td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </li>
          </div>
          <div v-else class="w-100 px-0">
            <div class="container px-0 pt-2 pb-3 d-flex justify-content-center">
              <span>距离比赛开始还有:</span>
            </div>
            <div class="container px-0 timer-contest d-flex justify-content-center">
              <ul class="p-0 d-flex justify-content-between">
                <li class="bg-white d-flex flex-column"><div>{{clock.clockTime.days}}</div><small>天</small></li>
                <li class="bg-white d-flex flex-column"><div>{{clock.clockTime.hours|parseNum(2)}}</div><small>小时</small></li>
                <li class="bg-white d-flex flex-column"><div>{{clock.clockTime.minutes|parseNum(2)}}</div><small>分钟</small></li>
                <li class="bg-white d-flex flex-column"><div>{{clock.clockTime.seconds|parseNum(2)}}</div><small>秒</small></li>
              </ul>
            </div>
            <div class="container px-0 d-flex justify-content-center">
              <router-link to="#" class="btn btn-green">立即报名</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    name: "contestContent",
    data(){
      return {
        tab: 1,
        MenuShow: false,
        isStart: true,
        clock: {
          startTime: new Date(),
          nowTime: new Date(),
          clockTime: {},
          timer: null,
        },
        problems: [],
        statusList: [],
        contest: '',
      }
    },
    computed: {
      tabActive(){
        let dom = $(`.nav-contest li:eq(${this.tab}) a`);
        return dom.text() ? dom.text() : '比赛说明'
      },
    },
    mounted: function(){
      /*************比赛倒计时**********************/
      let fullSeconds = this.clock.startTime.getTime() - this.clock.nowTime.getTime();
      this.clock.clockTime.days = Math.floor(fullSeconds / (1000*24*3600));
      fullSeconds -= this.clock.clockTime.days * (1000*24*3600);
      this.clock.clockTime.hours = Math.floor(fullSeconds / (1000*3600));
      fullSeconds -= this.clock.clockTime.hours * (1000*3600);
      this.clock.clockTime.minutes = Math.floor(fullSeconds / (1000*60));
      fullSeconds -= this.clock.clockTime.minutes * (1000*60);
      this.clock.clockTime.seconds = Math.floor(fullSeconds / (1000));
      function start(_this, index) {
        /**
         * 递归实现倒计时
         */
        if(index === 4){
          if(_this.clock.clockTime.seconds - 1 < 0){
            if(!start(_this, index - 1)) return false;
            _this.clock.clockTime.seconds = 60;
          }
          _this.clock.clockTime.seconds--
        }
        else if(index === 3){
          if(_this.clock.clockTime.minutes - 1 < 0){
            if(!start(_this, index - 1)) return false;
            _this.clock.clockTime.minutes = 60;
          }
          _this.clock.clockTime.minutes--
        }
        else if(index === 2){
          if(_this.clock.clockTime.hours - 1 < 0){
            if(!start(_this, index - 1)) return false;
            _this.clock.clockTime.hours = 24;
          }
          _this.clock.clockTime.hours--
        }
        else if(index === 1){
          if(_this.clock.clockTime.days - 1 < 0){
            return false;
          }
          _this.clock.clockTime.hours--
        }
        return true;
      }
      this.clock.timer = this.isStart ? null : setInterval(()=>{
        /**
         * 启动定时器
         */
        if(!start(this, 4)) {
          clearInterval(this.clock.timer);
          this.isStart = true;
        }
        else{

        }
      }, 1000)

    },
    beforeRouteEnter(to, from, next){
      axios.get(`http://192.168.0.100:8000/api/contest/${to.params['contest_id']}/`).then(res=>{
        if(res.data.status === 200){
          next(vm=>{
            let data = res.data;
            console.log(data);
            vm.isStart = data.is_start;
            if(data.is_start){
              vm.contest = data.contest;
              vm.contest.startTime = new Date(vm.contest.startTime);
              console.log(vm.contest)
              vm.problems = data.problems;
              console.log(vm.problems)
            }
            else{
              vm.clock.startTime = new Date(data.startTime);
              vm.clock.nowTime = new Date();
            }
          })
        }
        next()
      });
    },
    beforeRouteLeave(to, from, next){
      if(this.clock.timer)
        clearInterval(this.clock.timer);
      next();
    },
    watch: {
      tab: (value)=>{
        let dom = $(`.nav-contest li:eq(${value})`);
        let pos = dom.position();
        $(".nav-contest li.slide").css({left: +pos.left, width: '5.95em' });
      }
    },
    filters: {
      format(value){
        return String.fromCharCode(65 + value);
      },
      parseNum(value, index){
        value = value.toString();
        index = (index - value.length) < 0 ? 0 :  (index - value.length);
        while (index--){
          value = '0' + value;
        }
        return value;
      }
    },
    methods: {
      dragScroll(event){
        let startX = event.pageX;
        let _this = this;
        $(this.$refs.tableMove).mousemove(function (e) {
          let x = e.pageX;
          let realX =  $(_this.$refs.tableScreen).scrollLeft() - (x - startX) / 8;
          $(_this.$refs.tableScreen).scrollLeft(realX);
        });
        $(document).mouseup(function (e) {
          $(_this.$refs.tableMove).off('mousemove');
        })
      },
      setRank(index){
        if(index == 1) return `<svg viewBox="0 0 1251 1024" width="24" height="24">
                                <path fill="#f39c12" d="M1000.448 815.217778l208.782222 16.042666-238.933333-240.981333a410.737778
                                 410.737778 0 0 0 44.202667-184.718222C1016.490667 182.727111 833.763556 0 610.929778 0 387.982222
                                 0 207.303111 182.727111 207.303111 405.617778c0 74.24 20.081778 144.497778 56.263111 204.8L44.714667
                                 831.203556l208.782222-14.051556L239.502222 1024l236.942222-236.942222a382.976 382.976 0 0 0 136.533334
                                 24.120889c56.206222 0 110.421333-12.060444 158.606222-32.142223L1014.442667 1024l-13.994667-208.782222z
                                 m-508.416-109.624889c-5.290667-1.763556-12.401778-5.347556-17.692444-7.111111-3.584-1.763556-5.347556-1.763556-8.874667-3.527111-5.347556-1.763556-10.638222-5.347556-14.222222-7.111111-3.527111-1.763556-7.054222-5.290667-12.401778-7.111112-3.527111-1.706667-7.111111-5.290667-10.638222-7.054222l-21.276445-15.985778c-1.763556-1.763556-3.584-3.527111-5.347555-3.527111a114.744889 114.744889 0 0 0-15.928889-14.222222c-3.584-1.706667-5.347556-5.290667-7.111111-8.874667a77.141333 77.141333
                                 0 0 1-10.638223-12.401777c-3.527111-3.527111-5.347556-7.111111-8.874666-10.638223s-5.347556-7.111111-8.874667-10.638222-5.290667-8.874667-8.874667-12.401778a319.715556 319.715556
                                 0 0 1-53.191111-175.616 322.844444 322.844444 0 0 1 322.844445-322.844444c177.322667 0 322.787556 145.464889
                                 322.787555 322.844444 0 54.954667-14.222222 108.202667-39.025777 152.519112h-1.706667c-3.584 7.111111-8.931556
                                 14.222222-12.515556 21.276444-1.706667 3.584-3.527111 7.111111-7.054222 8.874667-3.527111 5.347556-8.874667
                                 10.638222-12.401778 15.985777a13.824 13.824 0 0 1-7.111111 7.111112c-3.527111 5.290667-8.874667 8.874667-12.401778
                                 14.222222l-7.111111 7.054222c-3.527111 3.527111-8.874667 7.111111-12.401777 12.401778-3.527111 1.763556-5.347556 5.347556-8.874667
                                 7.111111-3.527111 3.527111-7.111111 5.290667-12.401778 8.874667a175.786667 175.786667 0 0 1-30.151111 19.512888s-1.820444 0-1.820444
                                 1.706667c-7.054222 3.584-12.401778 7.168-19.456 10.695111-3.584 1.763556-7.111111 3.527111-8.874667 5.347556l-5.347556 1.706666a323.128889
                                 323.128889 0 0 1-124.131555 24.860445 337.180444 337.180444 0 0 1-118.897778-23.04z m376.832 40.277333c2.844444 0 5.12-3.925333
                                 7.793778-5.176889 6.428444 0 9.102222-6.542222 14.222222-10.410666 1.365333-1.308444 2.673778-1.308444 2.673778-2.616889 5.12-3.868444
                                 10.353778-9.102222 15.587555-14.279111l3.868445-3.925334c5.176889-5.12 10.410667-10.353778 14.279111-16.839111 0-1.308444 1.308444-1.308444
                                 1.308444-2.616889l11.719111-15.587555c1.308444-1.308444 1.763556-3.128889 1.763556-3.128889l95.744 99.555555-94.037333-9.955555 9.045333
                                 93.639111-95.744-100.807111s9.102222-5.233778 11.776-7.850667z m-489.187556 1.194667c-3.072 0-5.518222-4.152889-8.248888-5.518222-6.826667
                                 0-9.671111-6.883556-15.189334-11.036445-1.365333-1.365333-2.787556-1.365333-2.787555-2.787555-5.518222-4.096-11.036444-9.671111-16.497778-15.132445l-4.209778-4.152889a95.004444 95.004444 0 0 1-15.132444-17.976889c0-1.365333-1.422222-1.365333-1.422223-2.730666l-12.401777-16.554667a8.362667 8.362667 0 0 1-1.877334-3.299555l-101.717333 105.699555 99.896889-10.524444-9.557333 99.441777 101.660444-107.064888s-9.728-5.575111-12.515556-8.362667z" />
                                <path fill="#f39c12" d="M560.583111 324.039111c-4.266667 1.137778-10.24 2.161778-14.449778 2.161778a36.181333 36.181333 0 0 1-35.953777-35.384889c0-16.611556 10.695111-30.549333 27.306666-35.384889l53.134222-15.587555c15.530667-4.266667 27.363556-6.940444 38.570667-6.940445h1.137778c22.528 0 40.618667 18.204444 40.618667 40.732445v302.478222a40.732444 40.732444 0 1 1-81.464889 0l0.056889-259.584-29.013334 7.509333z"/>
                               </svg>`;
        else return index;
      },
      downSelect(event){
        let target = event.srcElement || event.target;
        let node = $(event.currentTarget);
        if(target.nodeName == 'LI'){
          node.children('input').attr('value', $(target).text())
        }
        node.children('div:last-child').toggleClass('show');
      },
      getStatusList(){
        this.axios.get(`http://192.168.0.100:8000/api/contest/${this.contest_id}/status/`).then(res=>{
          console.log(res.data)
          if(res.data.status === 200){
            this.statusList = [];
            res.data.statusList.forEach(item=>{
              this.statusList.push({
                runID: item.runID,
                problem_id: item.probId,
                memory: item.memory,
                subTime: item.subTime,
                time: item.time,
                result: item.result,
                language: item.language,
                user: {
                  user_name: item.userName,
                  user_id: item.userId,
                }
              })
            })
          }
        });
      }
    }
  }
</script>

<style scoped>
  .nav-contest{
    height: 60px;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
  }
  .nav-contest.show{
    height: calc(60px + 1.8em*3 + 17px*3 + 5px);
  }
  .nav-contest li.active{
    display: none;
  }
  .nav-contest li{
    line-height: 1.8em;
    font-size: 17px;
    text-align: center;
    width: 100%;
  }
  .nav-contest li a{
    color: #273849;
  }
  .nav-contest.show li:last-child{
    border-top: 1px solid #dadce0;
  }
  .nav-contest li:last-child{
    bottom: 0;
    height: 60px;
    display: flex;
    font-size: 18px;
    align-items: center;
    cursor: pointer;
    color: #273849;
  }
  .nav-contest.show li:last-child svg{
    transform: rotate(180deg);
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
  }
  .content-contest{
    min-height: calc(100vh - 60px - 55px - (60px + 1.8em*3 + 17px*3 + 5px));
    max-height: calc(100vh - 60px - 55px - 60px);
    overflow-y: auto;
  }
  .progress{
    height: .85em;
  }
  .border-radius{
    border-radius: 5px 5px 5px 5px;
  }
  .tab-contest{
    overflow-x: auto;
  }
  .outline-none-search input{
    border: 1px solid #dadce0;
    background-color: white;
    border-radius: 13px!important;
    padding-left: 2.35em;
    box-sizing: border-box;
    height: 2rem;
    font-size: 14px;
  }
  .outline-none-search input:focus{
    box-shadow: none;
    border: 1px solid #17bf63;
  }
  .outline-none-search.input-group{
    position: relative;
  }
  .outline-none-search .input-group-prepend{
    position: absolute;
    background: transparent;
    z-index: 1050;
    width: 23px;
    top: 1px;
    left: .6em;
  }
  .down-select-search input{
    cursor: pointer;
  }
  .down-select-search div:last-child{
    display: none;
    top: 2rem;
    border-radius: 5px;
    border: 1px solid #dadce0;
    max-height: 225px;
    overflow-y: auto;
  }
  .down-select-search div:last-child.show{
    display: block;
  }
  .down-select-search div:last-child ul li{
    list-style: none;
    cursor: pointer;
    line-height: 2.25em;
    width: 100%;
    text-align: center;
    border-bottom: 1px solid #dadce0;
  }
  .down-select-search div:last-child ul li:hover{
    color:#17bf63;
    background-color: rgba(79, 192, 141, 0.2);
  }
  table *{
    text-align: center;
    user-select: none;
    padding: 0;
    font-size: 14px;
  }
  table thead th{
    padding: .65em .25em;
    box-sizing: border-box;
    font-weight: 500;
    font-size: 16px;
    background-color: #eee;
    border-top: 1px solid #95a5a6;
  }
  table tbody th, table tbody td{
    border-bottom-style: dashed;
    border-top-style: dashed;
    border-top-color: #95a5a6;
    border-bottom-color: #95a5a6;
    border-top-width: 1px;
    border-bottom-width: 1px;
  }
  /************************题目列表****************************/
  .table.problem-list thead *{
    white-space:nowrap;
  }
  .table.problem-list thead tr th:nth-child(1), .table.problem-list tbody tr td:nth-child(1) {
    min-width: 1.2em;
    max-width: 1.2em;
  }
  .table.problem-list thead tr th:nth-child(2), .table.problem-list tbody tr td:nth-child(2) {
    min-width: 12em;
  }
  .table.problem-list thead tr th:nth-child(3), .table.problem-list tbody tr td:nth-child(3) {
    min-width: 2.75em;
    max-width: 3em;
  }
  .table.problem-list thead tr th:nth-child(4), .table.problem-list tbody tr td:nth-child(4) {
    min-width: 2.75em;
    max-width: 3em;
  }
  .table.problem-list thead tr th:nth-child(5), .table.problem-list tbody tr td:nth-child(5) {
    min-width: 2.75em;
    max-width: 3em;
  }
  .table.problem-list thead tr th:nth-child(6), .table.problem-list tbody tr td:nth-child(6) {
    min-width: 3.75em;
    max-width: 4em;
  }
  .table.problem-list tbody *{
    padding: .5rem 0rem;
  }
  .table.problem-list tbody a{
    color: rgb(37, 187, 155);
  }
  .table.problem-list tbody tr.success{
    background-color: rgba(79, 192, 141, 0.2);
    color: #17bf63;
  }
  .table.problem-list tbody tr.success a{
    color: #17bf63;
  }
  .table.problem-list tbody tr.danger{
    background-color: rgba(192, 57, 43, 0.1);
    color: #c0392b;
  }
  .table.problem-list tbody tr.danger a{
    color: #c0392b;
  }
  /*****************比赛排名******************************/
  .rank-list table tbody *{
    vertical-align: middle;
    height: 5em;
    word-break: break-all;
    font-family: Arial,sans-serif;
    font-size: 13.5px;
  }
  .rank-list div:first-child{
    flex: 1;
    border-right: 1px solid #bdc3c7;
  }
  .rank-list div:first-child table thead th:nth-child(1), .rank-list div:first-child table tbody tr td:nth-child(1) {
    min-width: 1.5em;
    max-width: 1.75em;
    padding-left: .5em;
  }
  .rank-list div:first-child table tbody tr td:nth-child(1){
    padding-left: .25em;
  }
  .rank-list div:first-child table thead th:nth-child(2), .rank-list div:first-child table tbody tr td:nth-child(2) {
    min-width: 4em;
    max-width: 4.5em;
  }
  .rank-list div:first-child table tbody tr td:nth-child(2) a{
    color: rgb(37, 187, 155);
  }
  .rank-list div:first-child table tbody tr td:nth-child(2){
    padding-left: .75em;
    padding-right: .75em;
  }
  .rank-list div:first-child table thead th:nth-child(3), .rank-list div:first-child table tbody tr td:nth-child(3) {
    min-width: 2.25em;
    max-width: 2.75em;
  }
  .rank-list div:first-child table thead th:nth-child(4), .rank-list div:first-child table tbody tr td:nth-child(4) {
    min-width: 4.5em;
    max-width: 5em;
  }
  .rank-list div:first-child table tbody tr td:nth-child(4) {
    padding-left: .75em;
    padding-right: .75em;
  }
  .rank-list div:first-child table thead th:nth-child(5), .rank-list div:first-child table tbody tr td:nth-child(5) {
    min-width: 3.5em;
    max-width: 4em;
  }
  .rank-list div:first-child table thead th:nth-child(5), .rank-list div:first-child table tbody tr td:nth-child(6) {
    min-width: 5.5em;
  }
  .rank-list div:first-child table tbody tr td:nth-child(6) {
    padding-left: .35em;
    padding-right: .35em;
  }
  .rank-list div table tbody tr th,.rank-list div table tbody tr td{
    background-color: rgb(252, 252, 252);
  }
  .rank-list div:last-child{
    min-width: 6.5em;
    max-width: calc(6em * 7 + 1em);
    overflow-x: auto;
  }
  .rank-list div:last-child table thead th{
    width: 6em;
    min-width: 6em;
  }
  .rank-list div:last-child table tbody{
    cursor: grab;
  }
  .rank-list div:last-child table tbody tr td.success{
    background-color: rgba(79, 192, 141, 0.2);
  }
  .rank-list div:last-child table tbody tr td.danger{
    background-color: rgba(192, 57, 43, 0.1);
  }
  /*****************************提交记录***********************************/
  .status-list tbody td{
    min-width: 2em;
    max-width: 2.5em;
    vertical-align: middle;
    height: 3.25em;
    word-break: break-all;
    font-family: Arial;
  }
  .status-list tbody a{
    color: rgb(37, 187, 155);
  }
  .status-list tbody a.success{
    background-color: #17bf63;
    color: #f5f6fa;
    padding: .3em .5em;
    border-radius: 3px;
    text-decoration: none;
  }
  .status-list tbody a.danger{
    background-color: #ed3f14;
    color: #f5f6fa;
    padding: .3em .5em;
    border-radius: 3px;
    text-decoration: none;
  }
  .status-list thead th{
    min-width: 3em;
    max-width: 4em;
    vertical-align: middle;
  }
  .status-list tbody td:nth-child(1), .status-list thead th:nth-child(1){
    min-width: 4em;
    max-width: 4.5em;
  }
  .status-list tbody td:nth-child(2), .status-list thead th:nth-child(2){
    min-width: 4em;
    max-width: 4.5em;
  }
  .status-list tbody td:nth-child(4), .status-list thead th:nth-child(4){
    min-width: 5em;
    max-width: 5.5em;
  }
  .status-list tbody td:nth-child(5), .status-list thead th:nth-child(5){
    min-width: 4.5em;
    max-width: 5em;
  }
  .status-list tbody td:nth-child(8), .status-list thead th:nth-child(8){
    min-width: 4.5em;
    max-width: 5em;
  }
  .status-list tbody td:nth-child(8){
    padding: 0 .25em;
  }
  /*****************************倒计时*****************************************/
  @font-face {
    font-family: 'Pathway Gothic One';
    font-style: normal;
    font-weight: 400;
    src: local('Pathway Gothic One Regular'), local('PathwayGothicOne-Regular'), url(/static/fonts/MwQrbgD32-KAvjkYGNUUxAtW7pEBwx-tRVZfX80.woff2) format('woff2');
    unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }
  /* latin */
  @font-face {
    font-family: 'Pathway Gothic One';
    font-style: normal;
    font-weight: 400;
    src: local('Pathway Gothic One Regular'), local('PathwayGothicOne-Regular'), url(/static/fonts/MwQrbgD32-KAvjkYGNUUxAtW7pEBwx-tS1Zf.woff2) format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }
  .timer-contest ul{
    max-width: calc(5.95rem*4 + .99rem);
    width: calc(5.95rem*4 + .99rem);
    min-width: calc(5.95rem*4);
  }
  .timer-contest ul li{
    list-style: none;
    color: #17bf63;
    width: 5.95rem;
    height:7.95rem;
    border-radius: 7px;
    overflow: hidden;
    box-sizing: border-box;
    border: 1px solid #dadce0;
    font-family: Pathway Gothic One;
  }
  .timer-contest ul li div{
    width: 100%;
    height: 5.5rem;
    font-size: 3.85rem;
    font-weight: 400;
    text-align: center;
  }
  .timer-contest ul li small{
    font-size: 1.25rem;
    height: calc(7.95rem - 5.5rem + .1rem);
    text-align: center;
    color: white;
    background: rgba(79, 192, 141, 0.55);
  }
  .btn.btn-green{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 2.25rem;
    max-width: calc(5.95rem*4 + .99rem);
    width: calc(5.95rem*4 + .99rem);
    min-width: calc(5.95rem*4);
    background: #17bf63;
    color: white;
  }
  .btn.btn-green.active{
    background:#b2bec3;
  }
  @media (min-width: 768px) {
    .nav-contest, .nav-contest.show{
      height: 80px;
    }
    .nav-contest li{
      margin-right: 7px;
      width: 5.95em;
    }
    .nav-contest li.slide{
      display: block;
      height: calc(1.7em + 1.025em);
      border-bottom: 4px solid #17bf63;
      border-radius: 2px;
      transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
      left: 0;
    }
    .nav-contest li.active{
      display: inline-block;
    }
    .nav-contest li.active a{
      color: #17bf63;
    }
    .tab-contest{
      max-width: calc(100vw - 60px);
    }
  }
</style>
