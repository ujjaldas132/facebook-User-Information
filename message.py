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
                #uploading the data
                file_path="facebook-data\messages\inbox/"


               


                os.getcwd()
                origin=os.getcwd()


                


                inbox_folder=origin+"\\"+file_path
                os.chdir(inbox_folder)


                


                time_msg={}
                hour_msg={}
                sender={}
                my_name='Ujjal Das'


                for hour in range(24):
                    if hour<10:
                        hour=str(0)+str(hour)
                    hour_msg[str(hour)]=0
                    
                    
                    
                for folder in os.listdir(os.getcwd()):
                    
                    os.chdir(folder)
                    #print(folder.split("_")[0],">>==================.................",os.listdir(),"\n")
                    file=open('message.json','r')
                    data=json.load(file)
                    file.close()
                    
                    
                    if 'title' in data:
                        sender[data['title']]=[len(data['messages']),0,0]
                        
                        
                        
                    
                    for x in data['messages']:
                    
                    #temp=timeConversion(int(int(x['timestamp_ms'])/1000)))
                        temp=timeConversion(int(int(x['timestamp_ms'])/1000))
                    #
                    #print(temp)
                        temp_time=str(temp.split("-")[0])+"/"+str(temp.split("-")[1])+"/"+str(temp.split("-")[2][0:2])
                        if temp_time in time_msg:
                            time_msg[temp_time]+=1
                        else:
                            time_msg[temp_time]=1
                        #print(temp,">>>",temp_time)
                        
                        
                        
                        #hour
                        temp_hour=temp.split('T')[1][0:2]
                        hour_msg[temp_hour]+=1
                        
                        
                        
                        #print(temp,">>>",temp_hour)
                        
                        # confirming the sender or reciever
                        if 'sender_name' in x and 'title' in data:
                            if x['sender_name']==my_name:
                                sender[data['title']][1]+=1
                            else:
                                sender[data['title']][2]+=1
                            
                    os.chdir(inbox_folder)
                    
                    #print(time_msg)


                # #now checking for a whole period

                # In[130]:


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
                        day=1
                        while day<32:
                            if year==cur_year and month>cur_month and day>cur_day:
                                break
                            day_str=str(day)
                            if day<10:
                                day_str="0"+day_str
                            time_str=str(year)+"/"+mon_str+'/'+day_str
                            if time_str not in time_msg:
                                x.append(time_str)
                                y.append(0)
                            else:
                                x.append(time_str)
                                y.append(time_msg[time_str])
                            day+=1
                        month+=1
                #


                # In[ ]:




                data_for_last_day=100


                plt.figure(figsize=(30,10))
                font=5
                plt.bar(x[-data_for_last_day:-1],y[-data_for_last_day:-1],width=0.8)
                plt.xticks(rotation=90)
                plt.rcParams.update({'font.size': font})
                plt.grid(True)

                plt.show()


              


                plt.figure(figsize=(50,20))
                font=40
                plt.bar(hour_msg.keys(),hour_msg.values(),width=0.5)
                plt.xticks(rotation=90)
                plt.rcParams.update({'font.size': font})
                plt.grid(True)

                plt.show()


               


                sender=sorted(sender.items(), key=lambda x: x[1][0],reverse=True)
                #now sender become a list
                msg_friend=pd.DataFrame([(x[1][0],x[1][1],x[1][2]) for x in sender],columns=['total_msg',"by_you","to_you"],index=[x[0] for x in sender])

                no_of_top_sender=20

                print(msg_friend[0:no_of_top_sender])


