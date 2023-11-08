import pandas as pd
import os
import glob
#import xlrd
#xls = xlrd.open_workbook(r'<path_to_your_excel_file>', on_demand=True)


df = pd.read_excel (r'C:\Users\HP\Desktop\Selenium using python\Automation\data.xlsx')
# print (df)

text = df['email text'].to_string()
# print(text)
# print(type(text))

arr = os.listdir('Automation')
# print(arr)
for file in arr:
        if file.endswith('.txt'):
            # print(file)
            # print(type(file))
            if text == file:
                print("True")


# https://www.google.com/search?q=how+to+compare+a+cell+value+with+a+string+in+excel+in+python&rlz=1C1CHZL_enIN760IN760&oq=how+to+compare+a+cell+value+with+a+string+in+excel+in+&aqs=chrome.3.69i57j33i160l3.21751j0j7&sourceid=chrome&ie=UTF-8
# All files ending with .txt
# print(glob.glob(r"C:\Users\HP\Desktop\Selenium using python\Automation\*.txt")) 
