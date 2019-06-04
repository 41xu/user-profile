import django,os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UserProfile.settings")
django.setup()


import math
from django.http import HttpResponse
from django.template import loader
from pyecharts import Line3D, Pie
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from appInfo.models import appInfo


REMOTE_HOST = 'http://chfw.github.io/jupyter-echarts/echarts'


@csrf_exempt
def chart(request):
    if request.method=="POST":
        appid=int(request.POST.get('appid'))
        template=loader.get_template('chart.html')
        age_pie=calage(appid)
        gender_pie=calgender(appid)
        context=dict(
            host=REMOTE_HOST,
            myechart_gender=gender_pie.render_embed(),
            script_list_gender=gender_pie.get_js_dependencies(),
            myechart_age=age_pie.render_embed(),
            script_list_age=age_pie.get_js_dependencies()
        )
        return HttpResponse(template.render(context,request))
    return render_to_response('chart.html')



def line3d():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D line plot demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True,
               visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    return line3d

def calage(appid):
    app=appInfo.objects.get(appid=appid)
    attr=['24岁以下','25-30岁','31-35岁','36-40岁','40岁以上']
    pie=Pie(app.name+"年龄分布")
    pie.add("",attr,[app.age_24,app.age_25_30,app.age_31_35,app.age_36_40,app.age_40],is_label_show=True)
    return pie

def calgender(appid):
    app=appInfo.objects.get(appid=appid)
    attr=['male','female']
    pie=Pie(app.name+"性别比例")
    pie.add("",attr,[app.male,app.female],is_label_show=True)
    return pie

if __name__=='__main__':
    calage(10001)