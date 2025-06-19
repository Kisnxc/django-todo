from django.shortcuts import render, redirect, get_object_or_404 
from .forms import TodoForm
from .models import Todo

def todo_list_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list_create')
    else:
        form = TodoForm()
    todos_pending = Todo.objects.filter(is_completed = False).order_by('-created_at')
    todos_done = Todo.objects.filter(is_completed = True).order_by('-created_at')
    return render(request, 'todo/todo_list.html', {
        'form': form, 
        'todos_pending': todos_pending,
        'todos_done': todos_done,
    })

def delete_todo(request,todo_id):
    todo = get_object_or_404(Todo, id = todo_id)
    todo.delete()

    return redirect('todo_list_create')
def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id = todo_id)
    todo.is_completed = True
    todo.save()
    print(f"✅ Đã đánh dấu hoàn thành: {todo.title}")

    return redirect('todo_list_create')
    


        

                    