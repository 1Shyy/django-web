from django.db import models


class Musicdir(models.Model):
    title = models.CharField(max_length=150, verbose_name= 'Исполнитель')
    content = models.TextField(blank=True, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Обложка', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Трек опубликован?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Жанр')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']





