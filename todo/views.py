from django.shortcuts import render, redirect
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
    todos = Todo.objects.all().order_by('-created_at')
    print("🧾 Dữ liệu trong DB:", todos)  # thêm dòng này để in ra terminal
    print("📦 Todos sẽ render:", list(todos))
    return render(request, 'todo/todo_list.html', {'form': form, 'todos': todos})
        

                    