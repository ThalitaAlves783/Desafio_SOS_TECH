from django.shortcuts import render
from listatech.models import Post
from listatech.forms import Postlink

# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html',{'posts':posts},)
