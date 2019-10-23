from django.shortcuts import render
from .forms import PostForm
# Create your views here.

def index(request):
    return render(request, 'posts/index.html')

def create(request):
    if request.method == "POST":
        pass
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)