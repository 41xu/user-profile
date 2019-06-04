from django.urls import path,re_path
from . import views

urlpatterns=[
    path('',views.main),
    re_path(r"(\w+)/",views.appInfo),
]
