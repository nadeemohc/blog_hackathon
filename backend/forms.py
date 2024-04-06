from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = ['image', 'title', 'description']
    widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    }
    help_texts = {
      'title': 'Required. 50 characters or fewer.',
      'description': 'Add a description for your blog post.',
    }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['blog_post', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }