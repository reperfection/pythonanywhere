from dataclasses import field
from django import forms
from .models import Blog


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image']