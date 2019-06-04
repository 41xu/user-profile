import django, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UserProfile.settings")
django.setup()

from django.shortcuts import render, render_to_response
from recommend.models import User
from appInfo.models import appInfo
import pandas as pd
import numpy as np
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def userInfo(request):
    if request.method == "POST":
        tel = int(request.POST.get('tel'))
        apps=getTotalApp(tel)
        female,male=calGender(tel)
        age1,age2,age3,age4,age5=calAge(tel)

        return render_to_response("recommend.html",{"flag":True,"apps":apps,
                                                    "female":female,"male":male,
                                                    "age1":age1,"age2":age2,
                                                    "age3":age3,"age4":age4,"age5":age5})
    return render_to_response("recommend.html",{
        "apps":[None]
    })

def getTotalApp(tel):
    apps=[]
    users=User.objects.filter(tel=tel)
    for user in users:
        app_=appInfo.objects.get(appid=user.appid)
        app={
            "appid":app_.appid,
            "appname":app_.name,
            "time":user.time,
            "count":user.count
        }
        apps.append(app)
    return apps



def calGender(tel):
    female = 0.5
    male = 0.5
    users = User.objects.filter(tel=tel)
    for user in users:
        app = appInfo.objects.get(appid=user.appid)
        total = (female + male + (app.female + app.male) * user.time)
        if total != 0:
            female = (female + app.female * user.time) / total
            male = (male + app.male * user.time) / total
        # print(female,male)
    return female, male


def calAge(tel):
    age1 = 0.2
    age2 = 0.2
    age3 = 0.2
    age4 = 0.2
    age5 = 0.2
    users = User.objects.filter(tel=tel)
    for user in users:
        app = appInfo.objects.get(appid=user.appid)
        total = (age1 + age2 + age3 + age4 + age5) + (
                    app.age_24 + app.age_25_30 + app.age_31_35 + app.age_36_40 + app.age_40) * user.time
        if total != 0:
            age1 = (age1 + app.age_24 * user.time) / total
            age2 = (age2 + app.age_25_30 * user.time) / total
            age3 = (age3 + app.age_31_35 * user.time) / total
            age4 = (age4 + app.age_36_40 * user.time) / total
            age5 = (age5 + app.age_40 * user.time) / total
    return age1, age2, age3, age4, age5


if __name__ == '__main__':
    tel = 13900000007
    print(calGender(tel))
    print(calAge(tel))
    print(getTotalApp(tel))

