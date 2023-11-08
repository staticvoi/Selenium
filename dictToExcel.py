import csv

dict1 = {
    "itemName":"Operational Tasks",
    "itemValue": {
    "requested_for":"163544",
    "u_details":"Testing Operation task",
    "u_app_ci": "2833dd29db05e7408cd41582399619da" 
    }
}

with open(r'C:\Users\HP\Desktop\Selenium using python\iris\output.csv', 'w+') as output:
    writer = csv.writer(output)
    for key, value in dict1.items():
        writer.writerow([key, value])