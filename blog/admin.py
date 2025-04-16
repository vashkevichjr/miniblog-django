from django.contrib import admin
from django.template.defaultfilters import title
from blog.models import Post, Comment, Likes


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "post")

@admin.register(Likes)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('ip','post')
# Register your models here.
