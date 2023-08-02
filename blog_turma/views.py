from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect
from .forms import PostForm
#O ponto antes do models significa diretório atual, antes eu escrevia from blog_turma.models import Post.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog_turma/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_turma/post_detail.html', {'post': post})

def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST,
          request.FILES)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'blog_turma/post_edit.html', {'form': form})

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog_turma/post_edit.html', {'form': form})

# def upload_view(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save()
#             # Lógica adicional, se necessário
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'upload.html', {'form': form})
