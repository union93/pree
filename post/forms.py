from django import forms
from .models import Post

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='검색하기')

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']

