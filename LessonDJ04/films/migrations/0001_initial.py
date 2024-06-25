# Generated by Django 5.0.6 on 2024-06-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New_film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название фильма')),
                ('description_film', models.TextField(verbose_name='Описание фильма')),
                ('feedback_film', models.TextField(verbose_name='Отзыв о фильме')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]