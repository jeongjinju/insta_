from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import HashTag, Post, Comment
# Create your views here.

def index(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form':comment_form
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # post가 저장된 후 생성된 id와 hashtag를 연결해 주어야 한다.
            # post안의 content를 띄어쓰기 기준으로 잘라준다.
            for word in post.content.split():
                if word.startswith("#"):
                    # hashtag 추가
                    # # 중복 생성 
                    # # hashtag = HashTag.objects.create(content=word)
                    # # word에 해당되는 content가 있으면 가져오고
                    # # 없으면 create 하기
                    # # get_or_create는 2가지 인자를 반환해준다.
                    # # (object, True or False) : 생성되었다면 True 아니면 False
                    # # hashtag, create = HashTag.objects.get_or_create(content=word)
                    # # create 값을 사용하지 않을 것이므로 [0]번 값만 불러와서 사용
                    hashtag = HashTag.objects.get_or_create(content=word)[0]
                    post.hashtags.add(hashtag)


            return redirect('posts:index')

    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)


def hashtags(request, id):
    hashtag = get_object_or_404(HashTag, id=id)
    
    posts = hashtag.taged_post.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/index.html', context)

def likes(request,id):
    like = get_object_or_404(Post, id=id)
    user = request.user
    if like.like_users.filter(id=user.id):
        like.like_users.remove(user)
    else:
        like.like_users.add(user)
    return redirect("posts:index")

def comment_create(request,id):
    post = get_object_or_404(Post, id=id)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('posts:index')
    
def comment_delete(requestm, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('posts:index')