import requests
import pandas as pd
import datetime
import calendar
import os
r = requests.get('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd0000010383c9072fc6459b4bbb9817c4d522c6&format=json&offset=0&limit=2000')
x=r.json()
data=pd.DataFrame(x['records'])
date=data['last_update'][0]
date_x=date.split(" ")[0]
date_pa=datetime.datetime.now().strftime("%p")
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d-%m-%Y').weekday() 
    return (calendar.day_name[born])
day=findDay(date_x)
path='/home/siddharth/Semester_V/DS250/DS250_Project/CSV/'
name_csv=date+date_pa+" "+day
data.to_csv(os.path.join(path,(name_csv+'.csv')))
