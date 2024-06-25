from .models import New_film
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput

class New_FilmForm(ModelForm):
    class Meta:
        model = New_film
        fields = ['title', 'description_film', 'feedback_film', 'pub_date', 'author']
        widgets = {
            'title': TextInput(attrs={'class':'form-control', 'placeholder': 'Заголовок фильма'}),
            'description_film': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
            'feedback_film': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв о фильме'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Время публикации'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'})
        }