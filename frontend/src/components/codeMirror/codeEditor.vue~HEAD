<template>
  <codemirror v-model="item" :options="cmOption" class="code-mirror" @ready="onCmReady" ref="myCmGenerate"></codemirror>
</template>


<script>
  import { codemirror } from 'vue-codemirror'
  // 我这里引入的是JS语言文件
  import 'codemirror/mode/javascript/javascript.js'
  import './setting.js'
  import Vue from "vue";
  import 'codemirror/theme/idea.css'
  import 'codemirror/theme/darcula.css'
  Vue.use(codemirror)
  export default {
    name: 'codeEditor',
    props: ['height', 'width', 'code'],
    data () {
      return {
        item: this.code,
        cmOption: {
          tabSize: 2, // tab
          lineNumbers: true, // 显示行号
          styleSelectedText: true,
          scrollbarStyle: null,
          line: true,
          foldGutter: true, // 块槽
          gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter'],
          highlightSelectionMatches: { showToken: /\w/, annotateScrollbar: true }, // 可以启用该选项来突出显示当前选中的内容的所有实例
          mode: { // 模式, 可查看 codemirror/mode 中的所有模式
            name: 'javascript',
            json: true
          },
          // hint.js options
          // 快捷键 可提供三种模式 sublime、emacs、vim
          keyMap: 'sublime',
          matchBrackets: true,
          showCursorWhenSelecting: true,
          theme: 'darcula', // 主题
          extraKeys: { 'Ctrl': 'autocomplete' }, // 可以用于为编辑器指定额外的键绑定，以及keyMap定义的键绑定
          cursorHeight: 1,
          autoCloseBrackets: true,
        }
      }
    },
    components: {
      codemirror
    },
    watch: {
      item(value){
        // console.log(value)
      },
    },
    methods: {
      onCmReady() {
        this.$refs.myCmGenerate.codemirror.setSize(this.width, this.height);
      },
    }
  }
</script>
<style>
  .cm-s-darcula .CodeMirror-gutters{
    background: #2d3436;
    border-right: none;
  }
  .cm-s-darcula.CodeMirror {
    background: #2d3436;
    color: #A9B7C6;
  }
</style>

