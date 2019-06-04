import django,os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UserProfile.settings")
django.setup()

import pandas as pd
from recommend.models import User
from appInfo.models import appInfo



def createUserTable():
    data=pd.read_csv('userdata.txt',sep='|',names=['tel','appid','useDate','useTime'])
    print(data)
    for i in range(len(data)):
        user=User(
            tel=data.loc[i]['tel'],
            appid=data.loc[i]['appid'],
            useDate=data.loc[i]['useDate'],
            useTime=data.loc[i]['useTime'],
        )
        user.save()


def createAppTalbe():
    data=pd.read_csv('appTab.txt',sep='|',names=[
        'appid','name','male','female','age_24','age_25_30','age_31_35','age_36_40','age_40'
    ])
    for i in range(len(data)):
        app=appInfo(
            appid=data.loc[i]['appid'],
            name=data.loc[i]['name'],
            male=data.loc[i]['male'],
            female=data.loc[i]['female'],
            age_24=data.loc[i]['age_24'],
            age_25_30=data.loc[i]['age_25_30'],
            age_31_35=data.loc[i]['age_31_35'],
            age_36_40=data.loc[i]['age_36_40'],
            age_40=data.loc[i]['age_40'],
        )
        app.save()

def UserDataProcess():
    data=pd.read_csv('userdata.txt',sep='|',names=['tel','appid','useDate','useTime'])
    newdata=pd.DataFrame(columns=['tel','appid','time','count'])
    test=data.groupby('tel')
    # print(test.get_group(13900000007).groupby('appid').sum())
    # temp=test.get_group(13900000007).groupby('appid').sum()
    # print(temp.loc[temp.index[0]]['useTime'])
    # print(test.get_group(13900000007).groupby('appid').count())

    user=pd.read_csv('newdata.csv')['tel']
    total=len(user)
    user=iter(user)
    count=0
    while count<total:
        cur=next(user)
        temp=test.get_group(cur).groupby('appid').sum()
        temp2=test.get_group(cur).groupby('appid').count()
        apps=temp.index
        for app in apps:
            time=temp.loc[app]['useTime']
            c=temp2.loc[app]['tel']
            newdata=newdata.append({"tel":cur,"appid":app,"time":time,"count":c},ignore_index=True)
        count+=1

    newdata.to_csv('data.csv')


def userTalbeNew():
    data=pd.read_csv('data.csv')
    for i in range(len(data)):
        user=User(
            id=i,
            tel=data.loc[i]['tel'],
            appid=data.loc[i]['appid'],
            time=data.loc[i]['time'],
            count=data.loc[i]['count']
        )
        user.save()







if __name__=='__main__':
    # createUserTable()
    # createAppTalbe()
    # UserDataProcess()
    userTalbeNew()