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


def plotting(x,y,z,width=0.4,title=None,xlabel=None,ylabel=None,font=10,fig_size=(10,10)):
    
    plt.figure(figsize=fig_size)
    plt.bar(x,y,width=.2,align= 'edge')
    plt.bar(x,z,width=-.2,align= 'edge')
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    plt.rcParams.update({'font.size': font})
    plt.legend(['Post by You','Post to your timeline by others'])
    plt.show()

    
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






def monthlyAnalysis(df):
    count_m=df['Month'].value_counts()
    
    temp=sorted(count_m.index)

    for month in range(1,13):
        mon_str=str(month)
        if month<10:
            mon_str="0"+str(month)

        if mon_str not in temp:
            count_m[mon_str]=0

    x=[]
    y=[]

    for indx in sorted(count_m.index):
        x.append(indx)
        y.append(count_m[indx])
    return[x,y]




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



def typeOfPost(df):
    temp_df=df.copy()

    tag_line={}

    tag_line['Shared']='shared'
    tag_line['Write']='wrote on'#write on someone's timeline
    tag_line['Upload']='added'#to your timeline or other
    tag_line['Reaction']='feeling'
    tag_line['Celebration']='celebrated'#celebration
    tag_line['Posted']='posted in'#to group 
    tag_line['Review']='reviewed'#review place book ,place etc
    tag_line['Update']='updated'#update your status or info

    for x in temp_df:
        if str(x)!='title':
            del temp_df[str(x)]
    

    temp_df=temp_df.dropna()

    
    y=[]
    x=[]

    
    for tags in tag_line:
        filter=temp_df['title'].str.contains(tag_line[tags])
        [m,n]=temp_df[filter].shape
        y.append(m)
        x.append(tags)
    return [x,y]




def main():
    
    file_path="facebook-data\posts/"


    file_name="your_posts.json"
    file=open(file_path+file_name,'r')
    data=json.load(file)
    file.close()

    file2_name="other_people's_posts_to_your_timeline.json"
    file=open(file_path+file2_name,'r')
    data2=json.load(file)
    file.close()



    data=data['status_updates']
    df=pd.DataFrame(data)

    #data2
    data2=data2['wall_posts_sent_to_you']
    df2=pd.DataFrame(data2)


 
    "convert the timr into readable  form"
    timeAddition(df,'timestamp')
    #df

    "convert the timr into readable  form"
    timeAddition(df2,'timestamp')



    df["mon_year"]=df["Year"]+"/"+df["Month"]
    

    df2["mon_year"]=df2["Year"]+"/"+df2["Month"]
   


    year_join=2015
    month_join=10




    [x,y]=yearlyOverview(df,"mon_year")
    [x1,y1]=yearlyOverview(df2,"mon_year")

    
    plotting(x,y,y1,3,"Monthly distribution of posts to your timeline ","year/months","no of posts",10,(10,10))






    [x,y]=monthlyAnalysis(df)

    [x2,y2]=monthlyAnalysis(df2)
    plotting(x,y,y2,2,"no of posts in every month","months","no of posts",10,(10,10))
            






    [x,y]=hourAnalysis(df)
    

    [x2,y2]=hourAnalysis(df2)
    plotting(x2,y,y2,2,"no of posts in every hours to your timeline","Hours","no of posts",10,(10,10))


  


    datetime.datetime.today().strftime('%Y-%m-%d')


   




    [x,y]=typeOfPost(df)
    [x2,y2]=typeOfPost(df2)
    plotting(x,y,y2,2,"dfferent type of posts","category","no of posts",10,(10,10))
    
