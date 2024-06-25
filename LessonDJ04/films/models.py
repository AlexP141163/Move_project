from django.db import models
#from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class New_film(models.Model):
    title = models.CharField('Название фильма',max_length=50)
    description_film = models.TextField('Описание фильма')
    feedback_film = models.TextField('Отзыв о фильме')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.CharField('Автор', max_length=100)
    image = models.ImageField('Изображение', upload_to='films/img/')

    def __str__(self):
        # Возвращает строку с названием статьи, автором, датой публикации и началом текста статьи
        preview_text = self.feedback_film[:50] + '...' if len(self.feedback_film) > 50 else self.feedback_film
        return f"{self.title} by {self.author} on {self.pub_date.strftime('%Y-%m-%d %H:%M')}, Preview: {preview_text}"

    class Meta:  # Встроенный класс, обязательно 'Meta' созданную таблицу 'New_post' переводит ее на русский язык.
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'