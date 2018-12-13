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


    

def main():
    
    #uploading the data
    file_path="facebook-data/friends/"


    file_name="friends.json"
    file=open(file_path+file_name,'r')
    data1=json.load(file)
    file.close()

    file2_name="received_friend_requests.json"
    file=open(file_path+file2_name,'r')
    data2=json.load(file)
    file.close()

    file3_name="rejected_friend_requests.json"
    file=open(file_path+file3_name,'r')
    data3=json.load(file)
    file.close()

    file4_name="removed_friends.json"
    file=open(file_path+file4_name,'r')
    data4=json.load(file)
    file.close()

    file5_name="sent_friend_requests.json"
    file=open(file_path+file5_name,'r')
    data5=json.load(file)
    file.close()


   



    df1=pd.DataFrame(data1['friends'])

    df2=pd.DataFrame(data2['received_requests'])

    df3=pd.DataFrame(data3['rejected_requests'])


    df4=pd.DataFrame(data4['deleted_friends'])

    df5=pd.DataFrame(data5['sent_requests'])



    
    list_dataFrame=[df1,df2,df3,df4,df5]

    for dataFrames in list_dataFrame:
        timeAddition(dataFrames,'timestamp')


   

    for dataFrames in list_dataFrame:
        dataFrames["year_month"]=dataFrames["Year"]+"/"+dataFrames["Month"]


    # In[14]:


    for dataFrames in list_dataFrame:
        dataFrames=dataFrames.sort_values(by='year_month',ascending=True)









    x_list=[]
    y_list=[]
    for dataFrames in list_dataFrame:
        [x,y]=yearlyOverview(dataFrames,"year_month")
        x_list.append(x)
        y_list.append(y)
        #plt.bar(x,y)

    new_y=[]
    for y in y_list:
        temp=0
        new_list=[]
        for i in range(len(y)):
            temp+=y[i]
            new_list.append(temp)
        new_y=new_y+[new_list]

        






    plt.figure(figsize=(20,20))
    font=20
    w=.5

    plt.bar(x_list[1],y_list[1],width=-(w),align= 'edge',color='crimson')
    plt.plot(x_list[1],[y/4 for y in new_y[1]],color='crimson')

    plt.bar(x_list[4],y_list[4],width=w,align= 'center',color='darkgreen')
    plt.plot(x_list[4],[y/4 for y in new_y[4]],color='darkgreen')
    plt.legend(['total sent_requests in 1/4 scale','sent_requests','total received_requests in 1/4 scale','received_requests'])


    plt.xticks(rotation=90)
    plt.rcParams.update({'font.size': font})
    plt.grid(True)

    plt.show()




    plt.figure(figsize=(20,20))

    w=0.9

    plt.bar(x_list[0],y_list[0],width=-(w/2),align= 'edge')
    plt.plot(x_list[0],[y/10 for y in new_y[0]],color='crimson')
    plt.legend(['total friends in 1/10 scale','Friends I Make'])


    plt.xticks(rotation=90)
    plt.rcParams.update({'font.size': font})
    plt.grid(True)

    plt.show()


  


    plt.figure(figsize=(20,20))
    w=.4
    plt.bar(x_list[2],y_list[2],width=-w,align= 'edge',color='darkgreen')
    plt.plot(x_list[1],[y for y in new_y[2]],color='darkgreen')
    plt.bar(x_list[3],y_list[3],width=w,align= 'edge',color='crimson')
    plt.plot(x_list[1],[y for y in new_y[3]],color='crimson')
    plt.legend(['total removed frinds','removed frinds','total rejected requests','rejected requests'])
    plt.xticks(rotation=90)
    plt.rcParams.update({'font.size': font})
    plt.grid(True)
    plt.show()

