from ast import Delete
from ayx import Package
try:
    Package.installPackages(package=['pandas','PyPDF2==2.11.0'], install_type="install --user")
except:
    pass
# ----------------
from ayx import Alteryx
import pandas as pd
from PyPDF2 import PdfMerger,PdfReader
import os
merger = PdfMerger(strict=False)

# 建立pandas表格資料,最後輸出該表
resultTemplate = {
    "Status":[""],
    "Message":"",
    "Output Path":""
}
resultData = pd.DataFrame(resultTemplate)

try: 
    # 讀取前端所選PDF檔案路徑
    data = Alteryx.read("#1")
    file_list = data['file_list']
    # 讀取欲儲存的結果檔案資料夾
    output_dir = Alteryx.read("#2")
    output_dir = output_dir['output_dir'].iloc[0]
    output_path=""
    if(output_dir and os.path.isdir(output_dir)):
        # 結果檔名判斷，若已存在則補序號
        output_path = os.path.join(output_dir,"merge_result.pdf")
        file = os.path.splitext(output_path)[0]
        ext = os.path.splitext(output_path)[1]   
        i = 2
        while os.path.exists(output_path):
            output_path = f'{file}({i}){ext}'
            i += 1
    else:
        raise Exception("儲存目的資料夾路徑不存在，請確認後再重新執行 ! ")

# 主程式       
    for i in range(len(file_list)):
#       未輸入的欄位則跳過
        if(not file_list[i]):
            continue
        
#       檔案若存在則合併,反之則標示錯誤並顯示錯誤訊息
        isExist = os.path.exists(file_list[i])
        if(isExist == True):
            reader = PdfReader(open(file_list[i],"rb"))
            merger.append(reader)
        else:
            raise Exception("該檔案不存在! " + file_list[i])
            
    # Write to an output PDF document
    merger.write(open(output_path, 'wb'))
    resultData.at[0, "Status"] = "Success"
    resultData.at[0, "Message"] = "-"
    resultData.at[0, "Output Path"] = output_path
except Exception as e:
    resultData.at[0, "Status"] = "Failure"
    resultData.at[0, "Message"] = "Alteryx 解析 PDF 過程發生錯誤，請與 AI&T 同仁聯繫("+str(e)+")"
    resultData.at[0, "Output Path"] = "-"
    if(output_path and os.path.exists(output_path)):
        os.remove(output_path)
Alteryx.write(resultData,1)
# Copyright © 2001-2022 Python Software Foundation; All Rights Reserved.

