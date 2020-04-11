<template>
  <div class="tinymce-editor">
    <editor v-model = "myValue" :init="init" :disabled="disabled" @onClick="onClick"></editor>
  </div>
</template>
<script>
  // import axios from "axios";
  import Editor from "@tinymce/tinymce-vue";
  import './config'
  // 编辑器插件plugins
  // 更多插件参考：https://www.tiny.cloud/docs/plugins/


  export default {
    name: 'TinymceEditor',
    components: {
      Editor
    },
    props: {
      disabled: {
        type: Boolean,
        default: false
      },
      value: {
        type: String,
        default: '',
      },
      vclass: {
        type: String,
        default: '',
      }
    },
    data() {
      return {
        init: {
          language_url: `/static/tinymce/lang/zh_CN.js`, // 语言包路径
          language: "zh_CN",  //语言
          skin_url: `/static/tinymce/skins/ui/oxide`, //skin路径
          content_css: `/static/tinymce/skins/content/custom/content.css`,
          plugins: "lists image table code codesample template media link hr " +
            "visualblocks visualchars image paste autoresize" ,
          toolbar: this.disabled ? false : "undo redo |  formatselect | bold italic forecolor backcolor | alignleft " +
            "aligncenter alignright alignjustify | lists image table | removeformat | code | codesample",
          branding: false,
          menubar:this.disabled ? false : 'file edit insert view format table tools',
          menu:this.disabled ? false : {
            file: {title: 'File', items: 'newdocument save'},
            edit: {title: 'Edit', items: 'undo redo | cut copy paste pastetext | selectall'},
            insert: {title: 'Insert', items: 'link media image | template hr'},
            view: {title: 'View', items: 'visualblocks visualchars'},
            format: {title: 'Format', items: 'bold italic underline strikethrough superscript subscript | formats | removeformat'},
            table: {title: 'Table', items: 'inserttable tableprops deletetable | cell row column'},
            tools: {title: 'Tools', items: 'code '}
          },
          autoresize_bottom_margin: 0,
          autoresize_overflow_padding: 5,
          statusbar: !this.disabled,
          max_height: 350,
          body_class: this.vclass,
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
