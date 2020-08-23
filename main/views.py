from django.shortcuts import render

# Create your views here.
from post.models import Post


def index(request):
    posts = Post.objects.all()[0:3]

    return render(request, 'main/mainpage.html', {'posts' : posts})
