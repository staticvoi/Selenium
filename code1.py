import glob
import pandas as pd
import extract_msg
import os

 

targetPattern = r"C:\Users\HP\Desktop\Selenium using python\Automation\*.xlsx"
a = glob.glob(targetPattern)
print(a)

 

for i in a:
    print(i)
    
    df = pd.read_excel(i)
    print(df)

 

    email_text = df['email text'].to_list()
    print(email_text)

 

    a = email_text[0]
    print(a)
    path = r"C:\Users\HP\Desktop\Selenium using python\Automation"
    b = os.path.join(path + "/" + a)
    msg = extract_msg.Message(b)
    msg_message = msg.body
    print(msg_message)

 

    body = msg_message.split(" ")
    print(body)
    

    index_approved = body.index('approved')
    print(index_approved)

    try: 
        index_not = index_approved-1
    except ValueError:
        if index_not == 'not':
            print('not approved email')
        else:
            print("approved is present call pranit wala function")    
        # if 'approved' in body:
        # print("approved is present call pranit wala function")

    