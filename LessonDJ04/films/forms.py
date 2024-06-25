from .models import New_film
from django.forms import ModelForm

class New_FilmForm(ModelForm):
    class Meta:
        model = New_film
        fields = ['title', 'description_film', 'feedback_film', 'pub_date', 'author']