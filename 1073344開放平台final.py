

import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
from lxml import etree
from io import BytesIO
def main():
    r = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-063?Authorization=rdec-key-123-45678-011121314", verify=False)
    list_of_dicts = r.json()    
    for dist in list_of_dicts["records"]["locations"][0]["location"]:
        #print(i["locationsName"])
        
        time=[]
        rainChance=[]
        maxTemp=[]
        minTemp=[]
        weather=[]
        if(dist["locationName"]==combo.get() or combo.get()==""):
            for i in dist["weatherElement"][0]["time"]:
                if i["elementValue"][0]["value"]!=" ":
                    time.append(i["startTime"][6:16]+" ~ "+i["endTime"][6:16])
                    rainChance.append(i["elementValue"][0]["value"])

            for i in dist["weatherElement"][8]["time"]:
                if i["elementValue"][0]["value"]!=" ":
                    minTemp.append(i["elementValue"][0]["value"])

            for i in dist["weatherElement"][12]["time"]:
                if i["elementValue"][0]["value"]!=" ":
                    maxTemp.append(i["elementValue"][0]["value"])  

            for i in dist["weatherElement"][6]["time"]:
                if i["elementValue"][0]["value"]!=" ":
                    weather.append(i["elementValue"][0]["value"])
            mylist.insert(END,dist["locationName"])
            for i in range(len(rainChance)):
                line=time[i]+"   降雨機率:"+rainChance[i]+"% "+"   溫度："+minTemp[i]+" ~ "+maxTemp[i]+" °C   "+weather[i]
                mylist.insert(END,line)

def onOK():
    # 取得輸入文字
    mylist.delete(0,END)
    main()

window = tk.Tk()
window.title('台北市各區氣象預報')
window.geometry("600x250+250+150")

# 標示文字
label = tk.Label(window, text = '請選擇區域')
label.pack()

# 輸入欄位
combo = ttk.Combobox(window, 
                            values=["",
                                    "南港區", 
                                    "文山區",
                                    "萬華區",
                                    "大同區",
                                    "中正區",
                                    "中山區",
                                    "大安區",
                                    "信義區",
                                    "松山區",
                                    "北投區",
                                    "士林區",
                                    "內湖區",
                                   ])
combo.pack()

# 按鈕
button = tk.Button(window, text = "查詢", command = onOK)
button.pack()

scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(window, yscrollcommand = scrollbar.set, width = 500,height=10)

mylist.pack(fill = NONE)
scrollbar.config( command = mylist.yview )

window.mainloop()

