from django.shortcuts import render
from .models import Post

posts=[
    {
        'author':'bebito',
        'title':'tu vieja',
        'content':'Puto el que lee',
        'date_posted':'29 sept 24'

    },
    {
        'author':'bebita',
        'title':'Te amoOoooooo',
        'content':'Puto el que lee',
        'date_posted':'29 sept 245'
    }
]



# Create your views here.

def home (request):
    context={'posts':Post.objects.all()}
    
    return render(request,'blog/home.html',context)


def about (request):
    return render(request,'blog/about.html',{'title':'Abt'})

