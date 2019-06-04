from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

# Create your views here.

@csrf_exempt
def register(request):
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        count=User.objects.filter(name=name)
        if len(count)==0:
            user=User(name=name,password=password)
            user.save()
            return HttpResponse("<p> 注册成功！</p>")
        else:
            return render_to_response('register.html',{'error':
                                                       "用户已存在，请重新输入用户名或直接登录"})
    return render_to_response('register.html')