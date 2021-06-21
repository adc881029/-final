# 1073344開放平台設計期末專題

## bulid process
我的程式是在anaconda環境下，以python 3.8版本開發的，並且使用了tkinter、requests、lxml和io函式庫，你可能會需要先安裝這些函式庫
```
pip install tk
```
## Introduction
我的程式從中央氣象局抓下台北市各區的氣象預報，並做呈現

## methods
我的程式的pseudocode
```
在圖形化介面添加下拉式選單、按鈕及輸出欄
if 如果按鈕被按下：
    執行main
    
def main()
    取得氣象預報資料
    if 資料的區域==下拉式選單中被選中的區域:
        把該區資料輸出到輸出欄
```
## Results
這是選擇區域的下拉式選單(如果選擇空白則全部區域都顯示)
![results pic](https://github.com/adc881029/pic/blob/main/chose%20menu.png)

這是選擇大同區並按搜尋的結果
![results pic](https://github.com/adc881029/pic/blob/main/大同.png)

這是選擇內湖區並按搜尋的結果
![results pic](https://github.com/adc881029/pic/blob/main/內湖.png)

## References
我的程式使用了以下API：

中央氣象局氣象預報：
    
    https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-063?Authorization=rdec-key-123-45678-011121314
