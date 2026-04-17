from django import forms
from .models import Post

class New_Post(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','text','about','author','status']
        
        
class SearchForm(forms.Form):
    search=forms.CharField(max_length=30)
        