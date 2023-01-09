from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class TodoListView(ListView):
    model=Todo
    template_name = 'home.html'
    context_object_name = 'list'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'task'

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('item','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetails',kwargs={'pk':self.object.id})


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'delete_data.html'
    success_url = reverse_lazy('todoapp:cbvhome')

# Create your views here.

def index(request):
    list=Todo.objects.all()
    if request.method=="POST":
        item=request.POST.get('item')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        todo=Todo(item=item,priority=priority,date=date)
        todo.save()
    return render(request,'index.html',{'list':list})

def delete_task(request,id):
    if request.method=='POST':
        item=Todo.objects.get(id=id)
        item.delete()
        return redirect('/')
    return render(request,'delete.html')

def edit_task(request,id):
    task=Todo.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'f':f})