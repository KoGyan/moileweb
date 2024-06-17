from django.http import JsonResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect



# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_data__lte = timezone.now()).order_by('published_data')
    return render(request,'blog/post_list.html',{'posts':posts})##디버깅 포인트

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
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
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def upload_image(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES['image']
            title = request.POST.get('title', 'No title')
            text = request.POST.get('text', 'No text')
            post = Post.objects.create(author=request.user, title=title, text=text, image=image, created_date=timezone.now())
            return JsonResponse({'message': 'Image uploaded successfully!'}, status=201)
        else:
            return JsonResponse({'error': 'No image found in request.'}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)



