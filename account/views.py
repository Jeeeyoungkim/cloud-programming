from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from .models import User
from .forms import UserForm
from content.models import Post

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                nickname = request.POST["nickname"],
            )
            auth.login(request, user)  # 로그인
            return redirect('main:index')
        else:
            # form = UserForm()
            print(form.errors)
            return render(request,"account/signup.html",{"form":form})

    return render(request,"account/signup.html")

def find_id(request):
    if request.method == "POST":
        data = json.loads(request.body)
        nickname = data["nickname"]
        if User.objects.filter(nickname = nickname).exists():
            user = User.objects.get(nickname = nickname)
            context = {
                'nickname' : user.nickname,
                'email' : user.username
            }
            return JsonResponse(context,status = 200)
        else:
            return JsonResponse({},status = 400)
    return render(request,"account/findID.html")

def find_pw(request):
    if request.method == "POST":
        username = request.POST.get("username")
        if User.objects.filter(username = username).exists():
            current_site = get_current_site(request)
            domain = current_site.domain
            link = reverse("account:reset_pw")
            full_link = f'http://{domain}{link}'

            subject = 'CLOODY 비밀번호 재설정 링크입니다.'
            message = '아래 url을 클릭하세요.\n [비밀번호 재설정하기] ' + full_link
            from_email = 'cloody450@gmail.com'
            recipient_list = [username]

            send_mail(subject, message, from_email, recipient_list)
        else:
            pass
        return redirect("account:find_pw")

    else:
        return render(request,"account/findPW.html")

def reset_pw(request):
    if request.method == "POST":
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            if request.POST.get("new_password1") == request.POST.get("new_password2"):
                user = User.objects.get(username = username)
                user.set_password(request.POST.get("new_password1"))
                user.save()
                return redirect("main:index")
            else:
                return render(request,"account/resetPW.html",{"message" : "비밀번호가 다릅니다."})
        else:
            return render(request,"account/resetPW.html",{"message" : "존재하지 않는 아이디 입니다."})
    else:
        return render(request,"account/resetPW.html")

def userUpdate(request):
    if request.method == "POST":
        request.user.nickname = request.POST.get("nickname")
        request.user.introduction = request.POST.get("introduce")
        request.user.image = request.FILES.get("image")
        request.user.save()

    return render(request,"content/profileEdit.html")

def userDetail(request,nickname):
    cur_user = User.objects.get(nickname = nickname)
    post_list = Post.objects.filter(author = cur_user).order_by("-created_at")
    context = {
        "cur_user" : cur_user,
        "post_list" :post_list,
    }
    return render(request,"content/profile.html",context)

def addSad(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data["post_id"][4:])
        post = Post.objects.get(id = data["post_id"][4:])
        if not post.sad_users.all().filter(id = request.user.id).exists():
            request.user.is_sad.add(post)
        count = post.sad_users.all().count()
    return JsonResponse({"count":count},status = 200)

def follow(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data["user_nickname"])
        user = User.objects.get(nickname = data["user_nickname"])
        if not user.followings.all().filter(id = request.user.id).exists():
            request.user.followings.add(user)

    return JsonResponse({},status = 200)

def unFollow(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data["user_nickname"])
        user = User.objects.get(nickname = data["user_nickname"])
        if user.followers.all().filter(id = request.user.id).exists():
            request.user.followings.remove(user)
            print(1)
    return JsonResponse({},status = 200)

def followings(request,nickname):
    user = User.objects.get(nickname=nickname)
    followings = user.followings.all()
    my_followings = request.user.followings.all()
    context = {
        "followings" :followings,
        "my_followings" : my_followings,
    }
    return render(request,"content/following.html",context)

def followers(request,nickname):
    user = User.objects.get(nickname=nickname)
    followers = user.followers.all()
    my_followers = request.user.followers.all()
    context = {
        "followers" :followers,
        "my_followers" : my_followers,
    }
    return render(request,"content/follower.html",context)
