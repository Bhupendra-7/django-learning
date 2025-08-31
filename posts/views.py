from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms


def posts_lists(request):
    posts = Post.objects.all().order_by('-date')
    context = {
        'posts': posts,
    }
    return render(request,'posts/posts_list.html',context)

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request,'posts/post_page.html',context)


@login_required(login_url='/users/login/')
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save with user
            newpost = form.save(commit=False) #“Let me finish preparing this object before saving it.”
            newpost.author = request.user
            newpost.save()                    # now save to DB
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})

