from django.contrib import admin

from .models import Post, PostImage, News, PostFile

class PostImageInline(admin.TabularInline):    
    model = PostImage    
    extra = 1

class PostFileInline(admin.TabularInline):
    model = PostFile
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):   
    inlines = [PostImageInline, PostFileInline]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):    
    list_display = ["post", "image", "caption"]

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):   
    list_display = ("news_date", "news_text") 

@admin.register(PostFile)
class PostFileAdmin(admin.ModelAdmin):
    list_display = ["post", "file", "name"]
