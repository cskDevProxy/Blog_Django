from django.db import models
from .utils import rename_photo


# Модель записи 
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:        
        ordering = ["-create_date"]

    def __str__(self):
        return self.title

# Фото к записи
class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name = "images"
    )

    image = models.ImageField(upload_to = rename_photo)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Фото для: {self.post.title}"

