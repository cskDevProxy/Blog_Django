from django.db import models
from .utils import rename_photo, rename_file


# Модель Тегов 
class Tegi(models.Model):
    name = models.CharField("Название тега", max_length=200, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

# Модель записи 
class Post(models.Model):
    STATUS_LIST = [('draft', 'Черновик'), ('published', 'Опубликовано')]

    title = models.CharField("Название", max_length=200)
    text = models.TextField("Текст записи")
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    status = models.CharField("Статус записи", max_length=30, blank=False ,choices=STATUS_LIST, default='draft' )

    tegs = models.ManyToManyField(Tegi, related_name='posts', verbose_name="Теги")

    class Meta:        
        ordering = ["-created_date"]
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.title

# Фото к записи
class PostImage(models.Model):
    # связь с постами
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name = "images"
    )

    image = models.ImageField("Изображения", upload_to = rename_photo)
    caption = models.CharField("Краткое описание", max_length=200, blank=True)

    class Meta:
        verbose_name = "Фотографии"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"Фото для: {self.post.title}"

# Новость
class News(models.Model):
    news_text = models.TextField("Новость")
    news_date = models.DateTimeField("Дата", auto_now_add=True)
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.news_text[:50]

# Файлы
class PostFile(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="files"
    )

    file = models.FileField("Файл", upload_to= rename_file)
    name = models.CharField("Название", max_length=200)
    
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
    
    def __str__(self):
        return f"{self.name} для: {self.post.title}"
