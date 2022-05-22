from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from client.models import TodoItem
from .forms import TodoForm
from django.contrib.auth.models import User
# Create your views here.



def welcome(request):
    return render(request, 'client/welcome.html')


@login_required
def homepage(request, ):
    print(request.user.id)
    form = TodoForm()
    tasks = TodoItem.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            current_user = request.user
            description = form.cleaned_data['description']
            TodoItem.objects.create(user_id= current_user, description = description)
            return redirect('/')       
    return render(request, 'client/home-page.html', {'form':form , 'tasks': tasks})




@login_required
def edit_task(request, id):
    task_to_edit = TodoItem.objects.get(id = id)
    form = TodoForm(instance=task_to_edit)
    if request.method == 'POST':
        form = TodoForm(instance=task_to_edit, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'client/edit-task.html', {'form': form })




@login_required  
def delete_task(request, id):
    TodoItem.objects.get(id = id).delete()
    return redirect('/')


@login_required
def profile_page(request, id):
    user = User.objects.get(id=id)
    
