from django import forms
from .models import PostMain


# Форма для создания/редактирования главных постов
class PostMainForm(forms.ModelForm):
    class Meta:
        model = PostMain
        fields = ['title', 'slug', 'content', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}
