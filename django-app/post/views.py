from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = Post.object.get(pk=post_pk)
        post.delete()
        return redirect('post:post_list')
    return HttpResponse('삭제인가요 진짜로?')

def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context={
        'post':post
    }
    return render(request,'post:post_detail',context)