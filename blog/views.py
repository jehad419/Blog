from django.shortcuts import render
from blog.models import Post

def post_list_view(request):
    try:
        posts = Post.object.select_related('category','author')
    except Exception as e:
        pass
