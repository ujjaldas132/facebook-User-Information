import os
import json
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def timeConversion(value):
    if value==0:
        return "UNKNOWN"
    else:
        return datetime.datetime.fromtimestamp(value).isoformat()



def main():
    

    file_path="facebook-data\likes_and_reactions/"


    file_name="posts_and_comments.json"
    file=open(file_path+file_name,'r')
    data=json.load(file)
    file.close()




    data_extract=data['reactions']




    reactions={}
    time_count={}
    hour_count={}
    for i in range(24):
        hour_str=str(i)
        if i <10:
            hour_str=str(0)+hour_str
        hour_count[hour_str]=0
        
    for x in data_extract:
        if x['data'][0]['reaction']['reaction'] in reactions:
            reactions[x['data'][0]['reaction']['reaction']]+=1
        else:
            reactions[x['data'][0]['reaction']['reaction']]=1
            
            
         
        temp=timeConversion(int(x['timestamp']))
      
        temp_time=str(temp.split("-")[0])+"/"+str(temp.split("-")[1])
        if temp_time in time_count:
            time_count[temp_time]+=1
        else:
            time_count[temp_time]=1
           
            
            
            
            
        temp_hour=temp.split('T')[1][0:2]
        hour_count[temp_hour]+=1





    year_join=2015
    month_join=10
    x=[]
    y=[]

    small_year=year_join
    small_month=month_join
    cur_year=int(datetime.datetime.today().strftime('%Y-%m-%d').split("-")[0])
    cur_month=int(datetime.datetime.today().strftime('%Y-%m-%d').split("-")[1])
    cur_day=int(datetime.datetime.today().strftime('%Y-%m-%d').split("-")[2])

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
            if time_str not in time_count:
                x.append(time_str)
                y.append(0)
            else:
                x.append(time_str)
                y.append(time_count[time_str])
            
            month+=1
   


  


    total_reaction=sum(reactions.values())
    plt.figure(figsize=(30,10))
    font=15
    plt.rcParams.update({'font.size': font})
    total_reaction
    plt.pie([x for x in reactions.values()],labels=[x for x in reactions.keys()])
    plt.title("pie visulisation of no of different reactions")

    temp=[x for x in reactions.keys()]
    for i in range(len(temp)):
        react=temp[i]
        react=react+'>>'+str(reactions[react])
        temp[i]=react
    plt.legend(temp)


    plt.show()


 



    plt.figure(figsize=(30,10))
    font=15
    plt.bar(x,y)
    plt.xticks(rotation=90)
    plt.rcParams.update({'font.size': font})
    plt.grid(True)
    plt.title("No of reaction Vs every month")
    plt.xlabel("Months")
    plt.ylabel("No of reactions")

    plt.show()






