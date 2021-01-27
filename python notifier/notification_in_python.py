import numpy as np
import pandas as pd
import os
import datetime
from plyer import notification

print(os.getcwd())

excelData = pd.read_excel('notification.xls')
main_data = pd.DataFrame(excelData).to_numpy()
for i in main_data:
    # print(i[3])
    if(datetime.datetime.now().hour == i[3].hour and datetime.datetime.now().minute == i[3].minute and datetime.datetime.now().second == i[3].second):
        notification.notify(title=i[1], message=i[2], timeout=10)
    else:
        print("--------------------------------------------------------------------------")
        print(datetime.datetime.now().hour)
        print(datetime.datetime.now().minute)
        print("--------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------")
        print(i[3].hour)
        print(i[3].minute)
        print("--------------------------------------------------------------------------")
