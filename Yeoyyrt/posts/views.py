from django.shortcuts import render, redirect

from .models import UserPost

def index(request):
    lista_post = UserPost.objects.all()
    context = {'lista_post':lista_post}
    return render(request,'posts/index.html', context)

def new_user_post(request):
    pass