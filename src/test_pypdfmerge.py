# # -*- coding:utf-8*-
# # 利用PyPDF2模組合併同一資料夾下的所有PDF檔案
# # 只需修改存放PDF檔案的資料夾變數：file_dir 和 輸出檔名變數: outfile

# import os
# from PyPDF2 import PdfFileReader, PdfFileWriter
# import time
# # import sys

# # if not sys.warnoptions:
# #     import warnings
# #     warnings.simplefilter("ignore")

# # 使用os模組的walk函式，搜尋出指定目錄下的全部PDF檔案
# # 獲取同一目錄下的所有PDF檔案的絕對路徑
# def getFileName(filedir):

#     file_list = [os.path.join(root, filespath) \
#                 for root, dirs, files in os.walk(filedir) \
#                 for filespath in files \
#                 if str(filespath).endswith('pdf')
#                 ]
#     return file_list if file_list else []

# # 合併同一目錄下的所有PDF檔案
# def MergePDF(filepath, outfile):

#     output = PdfFileWriter()
#     outputPages = 0
#     pdf_fileName = getFileName(filepath)

#     if pdf_fileName:
#         for pdf_file in pdf_fileName:
#             print("路徑：%s"%pdf_file)

#             # 讀取源PDF檔案
#             input = PdfFileReader(open(pdf_file, "rb"),strict=False)

#             #獲得源PDF檔案中頁面總數
#             pageCount = input.getNumPages()
#             outputPages += pageCount
#             print("頁數：%d"%pageCount)

#             # 分別將page新增到輸出output中
#             for iPage in range(pageCount):
#                 output.addPage(input.getPage(iPage))

#         print("合併後的總頁數:%d."%outputPages)
#         # 寫入到目標PDF檔案
#         outputStream = open(os.path.join(filepath, outfile), "wb")
#         output.write(outputStream)
#         outputStream.close()
#         print("PDF檔案合併完成！")

#     else:
#         print("沒有可以合併的PDF檔案！")

# # 主函式
# def main():
#     time1 = time.time()
#     file_dir = r"e:\test"   #待合併pdf路徑
#     outfile = "merge.pdf"   #合併好的pdf檔名
#     MergePDF(file_dir, outfile)
#     time2 = time.time()
#     print('總共耗時：%s s.' %(time2 - time1))

# main()

# from PyPDF2 import PdfMerger
# import os


# # 獲取所有pdf檔案完整路徑
# def getAllpdfFiles(filedir):
#     file_list = [os.path.join(root, filespath) \
#                 for root, dirs, files in os.walk(filedir) \
#                 for filespath in files \
#                 if str(filespath).endswith('pdf')
#                 ]
#     return file_list if file_list else []

# filedir = r'C:\Users\JYKL\Desktop\pdsmergeTest'
# merger = PdfMerger()

# pdf_file_list = getAllpdfFiles(filedir)
# for pdf_file in pdf_file_list:
#     merger.append(open(pdf_file,"rb"))

# # add the first 3 pages of input1 document to output
# # merger.append(fileobj=input1, pages=(0, 3))

# # insert the first page of input2 into the output beginning after the second page
# # merger.merge(position=2, fileobj=input2, pages=(0, 1))

# # append entire input3 document to the end of the output document
# # merger.append(input3)

# # Write to an output PDF document
# output = open(os.path.join(filedir,"merge_result.pdf"), "wb")
# merger.write(output)

# # Close File Descriptors
# merger.close()
# output.close()


# ----------------------------------------------------------------------------------------------

# 2020 Alteryx 第一版
# =============================================
# # List all non-standard packages to be imported by your 
# # script here (only missing packages will be installed)
# from ayx import Package
# Package.installPackages(package=['pandas','PyPDF2'], install_type="install --user")
# =============================================
# from ayx import Alteryx
# import pandas as pd
# from PyPDF2 import PdfMerger
# import os
# pdf_dir = Alteryx.read("#1")

# try:
#     filedir = pdf_dir['input_dir'].iloc[0]

#     # 獲取所有pdf檔案完整路徑
#     def getAllpdfFiles(filedir):
#         file_list = [os.path.join(root, filespath) \
#                     for root, dirs, files in os.walk(filedir) \
#                     for filespath in files \
#                     if str(filespath).endswith('pdf')
#                     ]
#         return file_list if file_list else []

#     merger = PdfMerger()

#     pdf_file_list = getAllpdfFiles(filedir)
#     for pdf_file in pdf_file_list:
#         merger.append(open(pdf_file,"rb"))

#     # Write to an output PDF document
#     output = open(os.path.join(filedir,"merge_result.pdf"),"wb")
#     merger.write(output)
#     result = os.path.join(filedir,"merge_result.pdf")
#     pdf_dir["status"] = "Success：" + result
#     print("Success")
# except Exception as e:
#     pdf_dir["status"] = "Failure：" + str(e)
#     print("Failure：" + str(e))
# Alteryx.write(pdf_dir,1)

# 2020 Alteryx 第二版
# ----------------------------------------------------------------------------------------------
#################################
# List all non-standard packages to be imported by your 
# script here (only missing packages will be installed)
from ast import Delete
from ayx import Package

Package.installPackages(package=['pandas','PyPDF2'], install_type="install --user")


#################################
# 載入模組
from ayx import Alteryx
import pandas as pd
from PyPDF2 import PdfMerger,PdfReader
import os
merger = PdfMerger(strict=False)

# 建立pandas表格資料,最後輸出該表
resultTemplate = {
    "Status":[""]
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
    resultData.at[0, "Message"] = ""
    resultData.at[0, "Output Path"] = output_path
except Exception as e:
    resultData.at[0, "Status"] = "Failure"
    resultData.at[0, "Message"] = "Alteryx解析PDF過程發生錯誤，請與AI&T 同仁聯繫("+str(e)+")"
    resultData.at[0, "Output Path"] = ""
    if(output_path and os.path.exists(output_path)):
        os.remove(output_path)
Alteryx.write(resultData,1)



#################################



#################################