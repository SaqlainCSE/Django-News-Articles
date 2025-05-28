from django.contrib import admin
from . models import User, Post, Category, Tag, Comment, Like, Message

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'role', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    list_filter = ('role', )
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'view_count', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('status', 'category', 'created_at', 'updated_at')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at', 'updated_at')
    search_fields = ('content', 'author__username', 'post__title')
    list_filter = ('created_at', 'updated_at')
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    search_fields = ('post__title', 'user__username')
    list_filter = ('created_at',)
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','number', 'subject', 'message', 'created_at')
    search_fields = ('subject', 'name', 'email', 'number')
    list_filter = ('created_at',)