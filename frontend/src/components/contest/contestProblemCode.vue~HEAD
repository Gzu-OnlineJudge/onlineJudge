<template>
  <div class="w-100">
    <div class="w-100 py-3">
      <div class="container px-0 bg-white">
        <div class="col-12 px-0">
          <div class="alert alert-info d-flex flex-column" id="alert">
            <h5 class="my-2"><router-link class="text-success" to="#">A - A+B problem</router-link></h5>
            <div class="text-muted d-flex my-2 flex-column flex-md-row">
              <div class="mr-2 mb-1 mb-md-0">
                <span><b class="mr-1">提交时间 :</b> 2020-03-27 21:31:05</span>
              </div>
              <div class="mr-2 mb-1 mb-md-0">
                <span><b class="mr-1">语言 :</b> C++</span>
              </div>
              <div class="mr-2 mb-1 mb-md-0">
                <span><b class="mr-1">运行时间 :</b> 1950ms</span>
              </div>
              <div class="mr-2 mb-1 mb-md-0">
                <span><b class="mr-1">内存 :</b> 34028K</span>
              </div>
            </div>
            <div class="text-muted">
              <span class="d-flex align-items-center"><b>运行状态 :</b> <div class="success ml-2">答案正确</div></span>
            </div>
          </div>
        </div>
        <div class="col-12 px-4 pb-4">
          <h5><router-link class="text-success" to="#">Gzuwkj</router-link> 的代码</h5>
          <div v-html="code"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import thljs from 'highlight.js'
  import 'highlightjs-line-numbers.js/src/highlightjs-line-numbers'
  import 'highlight.js/styles/github.css'
  export default {
    name: "contestProblemCode",
    data(){
      return {
        code: "<pre><code>#include\"stdio.h\"\nint main(){\n" +
          "return 0;\n" +
          "}</code></pre>"
      }
    },
    mounted() {
      thljs.highlightBlock($('pre code')[0]);
      $(function () {
        hljs.initLineNumbersOnLoad();
        hljs.lineNumbersBlock($('pre code')[0])
      });
    }
  }
</script>

<style>
  td.hljs-ln-numbers {
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    text-align: center;
    border-right: 1px solid #CCC;
    vertical-align: top;
    width: 2rem;
    padding: 0 .5rem;
    color: gray;
    font-weight: 600;
  }
  td.hljs-ln-code{
    padding-left: .5rem;
  }
  table.hljs-ln{
    width: 100%;
  }
  .hljs tbody tr:nth-child(even){
    background: white;
  }
  .hljs tbody tr:nth-child(even) td:first-child{
    background: #f8f8f8;
  }
  #alert h5{
    font-size: 17px;
  }
  #alert .text-muted{
    font-size: 14px;
  }
  #alert .success{
    background-color: #17bf63;
    color: #f5f6fa;
    font-size: 13px;
    padding: .3em .5em;
    border-radius: 3px;
    text-decoration: none;
  }
  #alert .danger{
    background-color: #ed3f14;
    font-size: 13px;
    color: #f5f6fa;
    padding: .3em .5em;
    border-radius: 3px;
    text-decoration: none;
  }

</style>

