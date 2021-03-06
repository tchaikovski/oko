from django import forms
from django.forms import ModelForm
from .models import Quote


class QuoteForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Quote
        fields = [
            'name', 'position', 'company', 'address', 'email', 'phone',
            'web', 'description', 'sitestatus', 'priority', 'jobfile'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Позиция'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Компания'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Е-Майл'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Сайт'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Описание'}),
            'sitestatus': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Статус'}),
            'priority': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Приоритет'}),
            'jobfile': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload'}),
        }

        #TODO: не работает empty_label
        empty_label = {
            'sitestatus': 'None',
            'priority': None,
        }
