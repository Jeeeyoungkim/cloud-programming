from django.urls import path
from .views import *

app_name = "content"

urlpatterns = [
    path("post/list/<str:by>/",postList,name = "post_list"),
    path("post/<int:id>/",postDetail,name = "post_detail"),
    path("post/saved/",postSaved,name = "post_saved"),
    path("post/create/",postCreate,name = "post_create"),
    path("post/save/",savePost,name = "post_save"),

    path("comment/create/<int:post_id>",commentCreate,name = "comment_create"),



]
