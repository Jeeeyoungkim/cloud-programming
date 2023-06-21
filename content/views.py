from django.shortcuts import render, redirect
import json
from django.http import JsonResponse

from .models import Post, Comment

def postList(request,by):
    if by == "all":
        post_list = Post.objects.all().order_by("-created_at")
        context = {
            "post_list" : post_list,
        }
    elif by == "follow":
        followings = request.user.followings.all()
        post_list = Post.objects.filter(author__in = followings).order_by("-created_at")
        context = {
            "post_list" : post_list,
        }
    return render(request,"main.html",context)

def postDetail(request,id):
    post = Post.objects.get(id = id)
    context = {
        "post": post,
    }
    return render(request,"content/content.html",context)

def postSaved(request):
    post_list = request.user.saved_posts.all()
    context = {
        "post_list" : post_list,
    }
    return render(request,"content/bucket.html",context)


def postCreate(request):
    if request.method == "POST":
        post = Post(author = request.user,content = request.POST.get("content"),image = request.FILES.get("image"))
        post.save()
        return redirect("content:post_detail",post.id)
    else:
        return render(request,"content/post.html")

def savePost(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post = Post.objects.get(id = data["post_id"])
        post.saved_user.add(request.user)
        post.save()
        return JsonResponse({"saved" : request.user.saved_posts.count()},status = 200)

def commentCreate(request,post_id):
    if request.method == "POST":
        post = Post.objects.get(id = post_id)
        comment = Comment(author = request.user,content = request.POST.get("content"),post = post)
        comment.save()
        return redirect("content:post_detail",post.id)

