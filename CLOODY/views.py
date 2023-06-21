from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def index(request):
    print(authenticate(request,username="jomulagy988@gmail.com",password = "1234"))
    if request.user.is_authenticated:
        return redirect("content:post_list","all")
    else:
        return render(request,"start.html")
