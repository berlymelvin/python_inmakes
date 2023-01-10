from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import Movie


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request, "index.html",context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request, 'detail.html',{'movie':movie})

def new_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        year=request.POST.get('year')
        desc=request.POST.get('desc')
        image=request.FILES['image']
        movie=Movie(name=name,desc=desc,year=year,image=image)
        movie.save()

    return render(request, 'new-movie.html')

def update_movie(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})

def delete_movie(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete-movie.html')
