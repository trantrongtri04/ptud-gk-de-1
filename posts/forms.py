from django.forms import ModelForm
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image_url','author','author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']