from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
from .form import CommentForm
class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "blog/index.html", {"post_list": posts})

class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, "blog/blog_detail.html", {"post": post})

class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.post_id = pk
            form.save()
        return redirect("/", pk=pk)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(post_id=pk, ip=ip_client)
            return redirect(f"/{pk}", pk=pk)
        except:
            new_like = Likes()
            new_like.post_id = pk
            new_like.ip = ip_client
            new_like.save()
            return redirect(f"/{pk}")

class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(post_id=pk, ip=ip_client)
            like.delete()
            return redirect(f"/{pk}", pk=pk)
        except:
            return redirect(f"/{pk}")

# Create your views here.
