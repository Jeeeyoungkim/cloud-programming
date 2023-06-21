from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = "account"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = "account/signin.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',signup,name = "signup"),
    path('findid/',find_id,name = "find_id"),
    path('findPW/',find_pw,name = "find_pw"),
    path('resetPW/',reset_pw,name = "reset_pw"),
    path("user/update/",userUpdate,name = "user_update"),
    path("user/detail/<str:nickname>/",userDetail,name = "user_detail"),
    path("sad/",addSad,name = "add_sad"),
    path("follow/",follow,name = "follow"),
    path("unFollow/",unFollow,name = "unFollow"),
    path("followings/<str:nickname>/",followings,name = "followings"),
    path("followers/<str:nickname>/",followers,name = "followers"),
]
