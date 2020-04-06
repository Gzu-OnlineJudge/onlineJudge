<template>
  <div class="tinymce-editor">
    <editor v-model = "myValue" :init="init" :disabled="disabled" @onClick="onClick"></editor>
  </div>
</template>
<script>
  // import axios from "axios";
  import tinymce from "tinymce/tinymce";
  import Editor from "@tinymce/tinymce-vue";
  import "tinymce/themes/silver";
  // 编辑器插件plugins
  // 更多插件参考：https://www.tiny.cloud/docs/plugins/
  import "tinymce/plugins/image"; // 插入上传图片插件
  // import 'tinymce/plugins/media'// 插入视频插件
  import "tinymce/plugins/table"; // 插入表格插件
  import "tinymce/plugins/lists"; // 列表插件
  import "tinymce/plugins/wordcount"; // 字数统计插件
  export default {
    name: 'TinymceEditor'
    ,
    components: {
      Editor
    },
    props: {
      value: {
        type: String,
        default: ""
      },
      // 基本路径，默认为空根目录，如果你的项目发布后的地址为目录形式，
      // 即abc.com/tinymce，baseUrl需要配置成tinymce，不然发布后资源会找不到
      baseUrl: {
        type: String,
        default: "/static"
      },
      disabled: {
        type: Boolean,
        default: false
      },
      plugins: {
        type: [String, Array],
        default: "lists image table wordcount"
      },
      // 在toolbar中添加工具栏相应按钮
      toolbar: {
        type: [String, Array],
        default:
          "undo redo |  formatselect | bold italic forecolor backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | lists image table | removeformat"
      }
    },
    data() {
      return {
        init: {
          language_url: `/static/tinymce/lang/zh_CN.js`, // 语言包路径
          language: "zh_CN",  //语言
          skin_url: `/static/tinymce/skins/ui/oxide`, //skin路径
          content_css: `/static/tinymce/skins/content/default/content.css`,
          height: 300,  //编辑器高度
          plugins: this.plugins,
          toolbar: this.toolbar,
          branding: false,  //是否禁用“Powered by TinyMCE”
          menubar: false, //顶部菜单栏显示
          // 此处为图片上传处理函数
          // 如需ajax上传可参考https://www.tiny.cloud/docs/configure/file-image-upload/#images_upload_handler
          // images_upload_handler: (blobInfo, success, failure) => {
          // let formdata = new FormData()
          // formdata.set('file', blobInfo.blob())
          // axios.post(url, formdata).then(res => {
          //   success(res.data.data)
          // }).catch(res => {
          //   failure('error')
          // })
          // },
        },
        myValue: this.value
      };
    },
    mounted() {
      tinymce.init({});
    },
    methods: {
      // 添加相关的事件，可用的事件参照文档=> https://github.com/tinymce/tinymce-vue => All available events
      // 需要什么事件可以自己增加
      onClick(e) {
        this.$emit("onClick", e, tinymce);
      },
      // 可以添加一些自己的自定义事件，如清空内容
      clear() {
        this.myValue = "";
      }
    },
    watch: {
      value(newValue) {
        this.myValue = newValue;
      },
      myValue(newValue) {
        this.$emit("input", newValue);
      }
    }
  };
</script>
