from django.contrib import admin

from .models import Post, PostImage

class PostImageInline(admin.TabularInline):    
    model = PostImage    
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):   
    inlines = [PostImageInline]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):    
    list_display = ["post", "image", "caption"]
