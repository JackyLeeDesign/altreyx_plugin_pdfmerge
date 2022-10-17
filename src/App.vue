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
    <!-- 主要內容 -->
    <div class="row">
      <div class="col">
        <!-- 第一步 -->
        <div class="card" style="margin-top:10px;">
          <div class="card-header d-flex justify-content-between align-items-center"><b>Step1：請先選擇結果檔案存放資料夾：</b></div>
          <div class="card-header d-flex justify-content-between align-items-center">(檔名自動儲存為 merge_result.pdf)</div>
          <div class="card-body" style="overflow-x:auto;">
            <ayx data-ui-props="{type:'FileBrowse', widgetId:'outputPath',browseType:'Folder'}"></ayx>
          </div>
        </div>

        <!-- 第二步 -->
        <div class="card" style="margin-top:10px;">
          <div class="card-header d-flex justify-content-between align-items-center"><b>Step2：請依照合併順序選擇欲合併之PDF檔案:</b>
          </div>
          <div class="card-header d-flex justify-content-between align-items-center">(一次最多合併8個檔案，若超過則重複執行該元件即可)</div>
          <div class="card-body" style="overflow-x:auto;">
            <ayx
              data-ui-props="{type:'FileBrowse', widgetId:'pdfFlie1', browseType:'File', fileTypeFilters: 'PDF Files (*.pdf)|*.pdf'}">
            </ayx><br>
            <ayx
              data-ui-props="{type:'FileBrowse', widgetId:'pdfFlie2', browseType:'File', fileTypeFilters: 'PDF Files (*.pdf)|*.pdf'}">
            </ayx><br>
            <ayx
              data-ui-props="{type:'FileBrowse', widgetId:'pdfFlie3', browseType:'File', fileTypeFilters: 'PDF Files (*.pdf)|*.pdf'}">
            </ayx><br>
            <ayx
              data-ui-props="{type:'FileBrowse', widgetId:'pdfFlie4', browseType:'File', fileTypeFilters: 'PDF Files (*.pdf)|*.pdf'}">
            </ayx><br>
            <ayx
              data-ui-props="{type:'FileBrowse', widgetId:'pdfFlie5', browseType:'File', fileTypeFilters: 'PDF Files (*.pdf)|*.pdf'}">
            </ayx><br>
            <ayx
              data-ui-props="{type:'FileBrowse', widgetId:'pdfFlie6', browseType:'File', fileTypeFilters: 'PDF Files (*.pdf)|*.pdf'}">
            </ayx><br>
            <ayx
              data-ui-props="{type:'FileBrowse', widgetId:'pdfFlie7', browseType:'File', fileTypeFilters: 'PDF Files (*.pdf)|*.pdf'}">
            </ayx><br>
            <ayx
              data-ui-props="{type:'FileBrowse', widgetId:'pdfFlie8', browseType:'File', fileTypeFilters: 'PDF Files (*.pdf)|*.pdf'}">
            </ayx>
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
    <p class="text-muted" style="margin: 0px;text-align: center;">版本：0.0.6</p>
  </footer>

</template>
<script>
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
    }
  },
  components: {
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
          manager.bindDataItemToWidget(outputPath, 'outputPath')

          var pdfFlie1 = new AlteryxDataItems.SimpleString('pdfFlie1')
          manager.addDataItem(pdfFlie1)
          manager.bindDataItemToWidget(pdfFlie1, 'pdfFlie1')

          var pdfFlie2 = new AlteryxDataItems.SimpleString('pdfFlie2')
          manager.addDataItem(pdfFlie2)
          manager.bindDataItemToWidget(pdfFlie2, 'pdfFlie2')

          var pdfFlie3 = new AlteryxDataItems.SimpleString('pdfFlie3')
          manager.addDataItem(pdfFlie3)
          manager.bindDataItemToWidget(pdfFlie3, 'pdfFlie3')

          var pdfFlie4 = new AlteryxDataItems.SimpleString('pdfFlie4')
          manager.addDataItem(pdfFlie4)
          manager.bindDataItemToWidget(pdfFlie4, 'pdfFlie4')

          var pdfFlie5 = new AlteryxDataItems.SimpleString('pdfFlie5')
          manager.addDataItem(pdfFlie5)
          manager.bindDataItemToWidget(pdfFlie5, 'pdfFlie5')

          var pdfFlie6 = new AlteryxDataItems.SimpleString('pdfFlie6')
          manager.addDataItem(pdfFlie6)
          manager.bindDataItemToWidget(pdfFlie6, 'pdfFlie6')

          var pdfFlie7 = new AlteryxDataItems.SimpleString('pdfFlie7')
          manager.addDataItem(pdfFlie7)
          manager.bindDataItemToWidget(pdfFlie7, 'pdfFlie7')

          var pdfFlie8 = new AlteryxDataItems.SimpleString('pdfFlie8')
          manager.addDataItem(pdfFlie8)
          manager.bindDataItemToWidget(pdfFlie8, 'pdfFlie8')

        }
      }.bind(this)
      //Load Script
      document.head.appendChild(script)
    }
  },
  computed: {
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
