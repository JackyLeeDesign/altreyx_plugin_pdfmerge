<template>
  <div class="container-fluid">
    <!-- PwC logo -->
    <div class="row">
      <div class="col">
        <div style="margin-top:20px;">
          <img src="./PwC.png" style="width: 100px;">
        </div>
      </div>
    </div>
    <div>{{showData}}</div>
    <!-- 主要內容 -->
    <div class="row">
      <div class="col">
        <!-- 第一步 -->
        <div class="card" style="margin-top:10px;">
          <div class="card-header d-flex justify-content-between align-items-center"><b>請連結欲合併的PDF檔資料：</b></div>
          <div class="card-body" style="overflow-x:auto;">
            <div class="mb-3">
              <b v-if="legder_status === true" style="color:green;"><BIconCheckLg style="vertical-align:text-top;" class="icon" /> 已連接完成</b>
              <b v-if="legder_status !== true" style="color:red;"><BIconExclamationTriangleFill style="vertical-align:text-top;" class="icon" /> {{legder_status}}</b>
            </div>
          </div>
        </div>

        <!-- 第二步 -->
        <div class="card" style="margin-top:10px;">
          <div class="card-header d-flex justify-content-between align-items-center"><b>Step3：請選擇排序順序</b></div>
          <div class="card-body" style="overflow-x:auto;">
            <draggable :list="fileList" :disabled="!enabledSortList" item-key="name" class="list-group"
              ghost-class="ghost" :move="checkMove" @start="dragging = true" @end="dragging = false">
              <template #item="{ element }">
                <div class="list-group-item" :class="{ 'not-draggable': !enabled }" :style="{'cursor': 'move'}">
                  {{ element.name }}
                </div>
              </template>
            </draggable>
            <!-- <div class="form-check mb-3">
              <input type="checkbox" class="form-check-input" v-model="pdf_isToDoAll" />
              <label for="exampleFormControlInput1" class="form-check-label"><b>
                  處理所有頁數
                </b></label>
            </div>
            <div class="mb-3" v-if="pdf_isToDoAll === false">
              <label for="exampleFormControlInput1" class="form-label"><b>
                  <BIconColumns style="vertical-align:text-top;" class="icon" /> 跨頁數請用","分隔，如:1,3,5。 某範圍頁數可用 "-"
                  表示，如:1-3。
                  亦可搭配使用，如:1-3,5,7
                </b></label>
              <input type="text" id="exampleFormControlInput1" class="form-control" placeholder="輸入頁數"
                v-model="pdf_page">
            </div> -->
          </div>
        </div>

        <!-- 第三步 -->
        <!-- <div class="card" style="margin-top:10px;">
          <div class="card-header d-flex justify-content-between align-items-center"><b>請連結欲合併的PDF檔資料：</b></div>
          <div class="card-body" style="overflow-x:auto;">
            <label for="exampleFormControlInput1" class="form-label"><b>
                <BIconFiles style="vertical-align:text-top;" class="icon" />本元件將指定PDF檔進行合併。
              </b></label>
              <ayx data-ui-props='{type:"FileBrowse", widgetId:"outputPath", browseType:"Folder"}'></ayx>
          </div>
        </div> -->
        

      </div>
    </div>
  </div>

  <footer class="footer mt-auto">
    <p class="text-muted" style="margin: 0px;text-align: center;">版本：0.0.5</p>
  </footer>

</template>
<script>
import draggable from "vuedraggable";
//replaceAll Polyfill


/**
 * String.prototype.replaceAll() polyfill
 * https://gomakethings.com/how-to-replace-a-section-of-a-string-with-another-one-with-vanilla-js/
 * @author Chris Ferdinandi
 * @license MIT
 */
if (!String.prototype.replaceAll) {
  String.prototype.replaceAll = function (str, newStr) {

    // If a regex pattern
    if (Object.prototype.toString.call(str).toLowerCase() === '[object regexp]') {
      return this.replace(str, newStr);
    }

    // If a string
    return this.replace(new RegExp(str, 'g'), newStr);

  };
}

//Clean Punctuation
String.prototype.clsPunc = function () {
  return this.replace(/[\p{P}\p{S}\p{Z}]/gu, '').toLowerCase()
}


export default {
  name: 'files',
  data() {
    return {
      str_columns:[],
      val_columns:[],
      enabledSortList: true,
      fileList: [
        { name: "File1", path: "./test/File1", id: 0 },
        { name: "File2", path: "./test/File2", id: 1 },
        { name: "File3", path: "./test/File3", id: 2 }
      ],
      dragging: false,
      pdf_dir: "",
      showData:""
    }
  },
  components: {
    draggable
  },
  watch: {
  },
  mounted() {
    if (typeof window.Alteryx !== 'undefined') {
      //Load Alteryx Library
      document.write('<link rel="import" href="' + window.Alteryx.LibDir + '2/lib/includes.html">');
      let libpath = window.Alteryx.LibDir + "2/lib/build/designerDesktop.bundle.js"
      let script = document.createElement('script')
      script.setAttribute('src', libpath)
      //Script Onload Callback
      script.onload = function () {
        //Define DataItem
        window.Alteryx.Gui.BeforeLoad = function (manager, AlteryxDataItems) {
          var outputPath = new AlteryxDataItems.SimpleString('outputPath')
          manager.addDataItem(outputPath)
          // Bind to Checkbox widget
          manager.bindDataItemToWidget(outputPath, 'outputPath')
        }
        //Load Settings
        window.Alteryx.Gui.AfterLoad = function (manager) {
          // this.pdf_dir = manager.getDataItem("pdf_dir").getValue()

          //Load Income Field
          let str_type = ["String","WString","V_String","V_WString","Date","Time","DateTime"]
          let val_type = ["Byte","Int16","Int32","Int64","FixedDecimal","Float","Double"]
          let incomingFields = manager.getIncomingFields()
          // alert(incomingFields)
          window.console.log(incomingFields)
          this.showData = incomingFields;
          this.str_columns = incomingFields.filter(item => str_type.indexOf(item.strType) > -1).map(item => item.strName)
          this.val_columns = incomingFields.filter(item => val_type.indexOf(item.strType) > -1).map(item => item.strName)
        }.bind(this)
      }.bind(this)
      //Load Script
      document.head.appendChild(script)
    }
  },
  computed: {
    legder_status:function(){
      try{
        //是否連接資料
        if ((this.str_columns.length + this.val_columns.length) === 0){
          throw `未連接明細帳資料`
        }
        // //確定 str_columns 至少有 3 項
        // if (this.str_columns.length < 3){
        //   throw `僅有 ${this.str_columns.length} 個欄位屬於字串類型，您至少需要日期、傳票編號、科目代碼 3 個欄位。`
        // }
        // //一欄式 - 確定 val_columns 至少有 1 項
        // if (this.ledger_type === true){
        //   if (this.val_columns.length < 1){
        //     throw `僅有 ${this.val_columns.length} 個欄位屬於數值類型，一欄式明細帳您至少需要 1 個數值欄位。`
        //   }
        // }
        // //二欄式 - 確定 val_columns 至少有 1 項
        // else{
        //   if (this.val_columns.length < 2){
        //     throw `僅有 ${this.val_columns.length} 個欄位屬於數值類型，二欄式明細帳您至少需要借方與貸方兩個欄位。`
        //   }
        // }
        return true
      }catch(err){
        return err
      }
    },
  },
  methods: {
    checkMove: function (e) { window.console.log("Future index: " + e.draggedContext.futureIndex) }
  }
}
</script>

<style>
#app {
  font-family: "Helvetica Neue", Helvetica, Arial, "Microsoft JhengHei", "PingFang TC", "Heiti TC", sans-serif;
  display: flex;
  flex-direction: column;
  height: 100%;
}

html,
body {
  height: 100%;
}
</style>
