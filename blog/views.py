from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Task
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, TaskForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def about(request):
    return render(request, 'blog/about.html', {})
    
def abouts_detail(request):
    check = get_object_or_404
    return render(request, 'blog/abouts_detail.html', {})

def todolist(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('checklist')

    context = {'tasks':tasks, 'form': form}
    return render(request, 'blog/checklist.html', context)


def todo_detail(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
             form.save()
        return redirect('checklist')

    context = {'form': form}
    return render(request, 'blog/todo_detail.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('checklist')


    context = {'item': item}
    return render(request, 'blog/delete.html', context)


