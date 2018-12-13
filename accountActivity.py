import os
import json
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



year_join=2015
month_join=10


def timeAddition(df,timestamp):
   
    year=[timeConversion(x).split("-")[0] for x in df[str(timestamp)]]
    month=[timeConversion(x).split("-")[1] for x in df[str(timestamp)]]
    day=[timeConversion(x).split("-")[2][0:2] for x in df[str(timestamp)]]
    hour=[timeConversion(x).split("T")[1][0:2] for x in df[str(timestamp)]]
    df['Year']=year
    df['Month']=month
    df['Day']=day
    df['Hour']=hour
    del df['timestamp']
    
def timeConversion(value):
    if value==0:
        return "UNKNOWN"
    else:
        return datetime.datetime.fromtimestamp(value).isoformat()


def yearlyOverview(df,column):
    counts=df[column].value_counts()

    temp=sorted(counts.index)
    small_year=year_join
    small_month=month_join
    cur_year=int(datetime.datetime.today().strftime('%Y-%m-%d').split("-")[0])
    cur_month=int(datetime.datetime.today().strftime('%Y-%m-%d').split("-")[1])
    for year in range(small_year,cur_year+1):
        month=1
        while month<13:
            if year==year_join and month==1:
                month=month_join
            if year==cur_year and month>cur_month:
                break
            mon_str=str(month)
            if month<10:
                mon_str="0"+str(month)
            time_str=str(year)+"/"+mon_str
            if time_str not in temp:
                counts[time_str]=0
            month+=1

    x=[]
    y=[]

    for indx in sorted(counts.index):
        x.append(indx)
        y.append(counts[indx])
        
    return [x,y]



#most post get in which hour
def hourAnalysis(df):
    count_h=df['Hour'].value_counts()


    temp=sorted(count_h.index)

    for hour in range(0,24):
        hour_str=str(hour)
        if hour<10:
            hour_str="0"+str(hour)

        if hour_str not in temp:
            count_h[hour_str]=0




    x=[]
    y=[]

    for indx in sorted(count_h.index):
        x.append(indx)
        y.append(count_h[indx])
    return [x,y]


def main():

    #uploading the data
    file_path="facebook-data/security_and_login_information/"


    file_name="account_activity.json"
    file=open(file_path+file_name,'r')
    data=json.load(file)
    file.close()




    df=pd.DataFrame(data['account_activity'])
    df






        
        
    timeAddition(df,'timestamp')




    df["year_month"]=df["Year"]+"/"+df["Month"]
    df['y_m_d']=df["Year"]+"/"+df["Month"]+"/"+df["Day"]
    df


    # In[52]:


    font=10
    plt.figure(figsize=(30,30))
   
    m,n=df.shape
    area = (30 * np.random.rand(n))**2
    colors = (np.random.rand(n),np.random.rand(n),np.random.rand(n),)
    ######
    plt.scatter(df['y_m_d'],df['Hour'], s=230, c='blue', alpha=0.5,marker="s")
    plt.xticks(rotation=90)
    plt.rcParams.update({'font.size': font})
    plt.grid(True)
    plt.title("hour vs day")
    plt.xlabel("day")
    plt.ylabel("hour")
    plt.show()


    # In[51]:


    font=10
    plt.figure(figsize=(30,30))
    plt.scatter(df['year_month'],df['Day'], s=10000, c='red', alpha=0.5,marker="$facebook$")
    plt.xticks(rotation=90)
    plt.rcParams.update({'font.size': font})
    plt.grid(True)
    plt.title("day vs month")
    plt.xlabel("month")
    plt.ylabel("Day")
    plt.show()


    # In[50]:






    [x,y]=yearlyOverview(df,"year_month")


    font=10
    plt.figure(figsize=(30,30))
    plt.bar(x,y)
    plt.xticks(rotation=90)
    plt.rcParams.update({'font.size': font})
    plt.grid(True)
    plt.title("no of activity per month")
    plt.xlabel("month")
    plt.ylabel("no of activity")
    plt.show()





    [x,y]=hourAnalysis(df)


    font=20
    plt.figure(figsize=(30,30))
    plt.bar(x,y)
    plt.xticks(rotation=90)
    plt.rcParams.update({'font.size': font})
    plt.grid(True)
    plt.title("no of activity in each hour")
    plt.xlabel("hour")
    plt.ylabel("no of activity")
    plt.show()

