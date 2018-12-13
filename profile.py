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





class information:
                def __init__(self,data):
                                self.data=data
                                self.name=data['name']['full_name']
                                self.birthday=str(data['birthday']['day'])+'/'+str(data['birthday']['month'])+'/'+str(data['birthday']['year'])
                                self.email=data['emails']
                                self.gender=data['gender']['pronoun']
                                self.joined=timeConversion(data['registration_timestamp'])
                                self.curCity=data['current_city']
                                self.homcity=data['hometown']
                                self.plc_lived=data['places_lived']

                def relationship(self):
                                people={}
                                for member in self.data['family_members']:
                                                relation=member['relation']
                                                if relation in people:
                                                                people[relation]+=[member['name']]
                                                else:
                                                               people[relation] =[member['name']]
                                return people
                                                

                
                def place(self):
                                home_city=str(self.homcity['name'])+'      from: '+str(timeConversion(self.homcity['timestamp']))
                                cur_city=str(self.curCity['name'])+'      from: '+str(timeConversion(self.curCity['timestamp']))
                                place_lived=[]
                                for place in self.plc_lived:
                                                place_lived=place_lived+[str(place['place'])+'      from: '+str(timeConversion(place['start_timestamp']))]
                                
                                print("home place: "+home_city+"\n")
                                print("current city:  "+cur_city+"\n")
                                print("place lived: ")
                                for x in place_lived:
                                                print(x)


                def education(self):
                                data=self.data['education_experiences']
                                schools=[]
                                graduated="UNKNOWN"
                                name="unknown"
                                description="UNKNOWN"
                                endTime="UNKNOWN"
                                startTime="UNKNOWN"
                                school_type="UNKNOWN"
                                
                                
                                for college in data:
                                                name=college['name']
                                                
                                                if 'graduated' in college:
                                                                graduated=str(college['graduated'])
                                                else:
                                                                graduated="UNKNOWN"

                                                if 'description' in college:
                                                                description=college['description']
                                                else:
                                                                description="UNKNOWN"

                                                if 'end_timestamp' in college:
                                                                endTime=str(timeConversion(college['end_timestamp']))
                                                else:
                                                                endTime="UNKNOWN"

                                                if 'start_timestamp' in college:
                                                                startTime=str(timeConversion(college['start_timestamp']))
                                                else:
                                                                startTime="UNKNOWN"

                                                if 'school_type' in college:
                                                                school_type=college['school_type']
                                                else:
                                                                school_type="UNKNOWN"


                                                temp="name:  "+name+"\n"+"description:  "+"schooltype:  "+school_type+"\n"+"description"+description+"\n"+"graduated:  "+graduated+"\n"+"started:  "+startTime+"\n"+"ended:  "+endTime+"\n\n\n"
                                                schools+=[temp]
                                return schools

                def work(self):
                                data=self.data['work_experiences']
                                company=[]
                                employer="UNKNOWN"
                                location="unknown"
                                description="UNKNOWN"
                                endTime="UNKNOWN"
                                startTime="UNKNOWN"
                                title="UNKNOWN"
                                
                                
                                for insti in data:
                                                employer=insti['employer']
                                                
                                                if 'title' in insti:
                                                                title=str(insti['title'])
                                                else:
                                                                title="UNKNOWN"

                                                if 'description' in insti:
                                                                description=insti['description']
                                                else:
                                                                description="UNKNOWN"

                                                if 'end_timestamp' in insti:
                                                                endTime=str(timeConversion(insti['end_timestamp']))
                                                else:
                                                                endTime="UNKNOWN"

                                                if 'start_timestamp' in insti:
                                                                startTime=str(timeConversion(insti['start_timestamp']))
                                                else:
                                                                startTime="UNKNOWN"

                                                if 'location' in insti:
                                                                location=insti['location']
                                                else:
                                                                location="UNKNOWN"


                                                temp="employer:  "+employer+"\n"+"location:  "+location+"\n"+"description:  "+description+"\n"+"title:  "+title+"\n"+"started:  "+startTime+"\n"+"ended:  "+endTime+"\n\n\n"
                                                company+=[temp]
                                return company


                def pages(self):
                                data=self.data['pages']
                              
                                df=pd.DataFrame(data)
                                df=df.rename(index=str,columns={'name':'Category','pages':'Name of the Pages'})
                                
                                graph_x=[]
                                graph_y=[]
                                for i in range(df.shape[0]):
                                    
                                    graph_y+=[len(df.iloc[i][1])]
                                    graph_x+=[df.iloc[i][0]]
                                plt.figure(1)
                                plt.bar(graph_x,graph_y)
                                plt.xticks(rotation=90)
                                plt.xlabel("category")
                                plt.ylabel("no of pages")
                                plt.title("category vs no of pages")
                                
                                plt.figure(2)
                                
                                i=graph_x.index('Other')
                                graph_x.remove('Other')
                                graph_y.remove(graph_y[i])
                                plt.xticks(rotation=90)
                                plt.bar(graph_x,graph_y)
                                plt.xlabel("category")
                                plt.ylabel("no of pages")
                                plt.title("category vs no of pages without others")
                                plt.show()
                                return df





                def groups(self):
                                data=self.data['groups'].copy()
                                for x in data:
                                                temp=x['timestamp']
                                                t=timeConversion(temp)
                                                
                                                t=t.split('-')
                                                x['Year']=t[0]
                                                x['Month']=t[1]
                                                x['Day']=t[2][0:2]
                                                x['Hour']=t[2][3:5]
                                                x['Minute']=t[2][6:8]
                                                x['Second']=t[2][9:]
                                                del x['timestamp']
                                df=pd.DataFrame(data)
                                col=['name','Year','Month',"Day","Hour","Minute","Second"]
                                df=df[col]
                                yearly={}
                                Monthly={'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0}
                                daily={'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0}
                                Hourly={"00":0,'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0}
                                (m,n)=df.shape
                                for i in range(m):
                                                year=df.iloc[i][1]
                                                if year in yearly:
                                                                yearly[year]+=1
                                                else:
                                                                yearly[year]=0
                                        
                                                Monthly[df.iloc[i][2]]+=1
                                    
                                    
                                                day=df.iloc[i][3]
                                                if day in daily:
                                                                daily[day]+=1
                                                else:
                                                                daily[day]=0
                                    
                                        
                                    
                                                hour=df.iloc[i][4]
                                                if hour in Hourly:
                                                                Hourly[hour]+=1
                                                else:
                                                                Hourly[hour]=0
                                        
                                        
                                for i in range(13,32):
                                                if str(i) not in daily:
                                                                daily[str(i)]=0
                                for i in range(13,25):
                                                if str(i) not in Hourly:
                                                                Hourly[str(i)]=0

                                graph_x=[]
                                graph_y=[]
                                for item in sorted(yearly):
                                                graph_x.append(item)
                                                graph_y.append(yearly[item])
                                plt.figure(1)
                                plt.bar(graph_x,graph_y)
                                plt.xticks(rotation=90)
                                plt.xlabel("YEARS")
                                plt.ylabel("NO OF GROUPS JOINED")
                                plt.title("YEARLY ANALYSIS OF GROUP JOINED")
                                #plt.show()


                                graph_x=[]
                                graph_y=[]
                                for item in sorted(Monthly):
                                                graph_x.append(item)
                                                graph_y.append(Monthly[item])
                                plt.figure(2)
                                plt.bar(graph_x,graph_y)
                                plt.xticks(rotation=90)
                                plt.xlabel("MONTHS")
                                plt.ylabel("NO OF GROUPS JOINED")
                                plt.title("MONTHLY ANALYSIS OF GROUP JOINED")
                                


                                graph_x=[]
                                graph_y=[]
                                for item in sorted(daily):
                                                graph_x.append(item)
                                                graph_y.append(daily[item])
                                plt.figure(3)
                                plt.bar(graph_x,graph_y)
                                plt.xticks(rotation=90)
                                plt.xlabel("DAYS")
                                plt.ylabel("NO OF GROUPS JOINED")
                                plt.title("DAILY ANALYSIS OF GROUP JOINED")
                                


                                        
                                graph_x=[]
                                graph_y=[]
                                for item in sorted(Hourly):
                                                graph_x.append(item)
                                                graph_y.append(Hourly[item])
                                plt.figure(4)
                                plt.bar(graph_x,graph_y)
                                plt.xticks(rotation=90)
                                plt.xlabel("TIME-HOURS")
                                plt.ylabel("NO OF GROUPS JOINED")
                                plt.title("HOURLY ANALYSIS OF GROUP JOINED")
                                plt.show()

                                return df


                
    

                                                
                                                




def main():
                
                file_path="facebook-data\profile_information/"
                file_name="profile_information.json"
                file=open(file_path+file_name,'r')
                data=json.load(file)
                file.close()

                

                main_data=data['profile']
                profile=information(main_data)




                #name
                print(profile.name)
                #date of birth
                print(profile.birthday)
                #gender
                print(profile.gender)
                #email
                print(profile.email)
                #date and timing of joining
                print("joined facebook:  ",profile.joined)
                #places you been
                profile.place()
                #family member
                family_members=profile.relationship()
                for members in family_members:
                                print(members+str(" :: ")+str(family_members[members]))

                #education detail

                for college in profile.education():
                                print(college)

                #work  detail

                for company in profile.work():
                                print(company)

                #pages you like
                pages=profile.pages()
                pages

                #group you joined'
                group=profile.groups()
                
