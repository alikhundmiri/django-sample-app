from django import forms
from .models import Post, Detail

class PostForm(forms.ModelForm):
    person_name = forms.CharField()
    person_job = forms.CharField()
    class Meta:
        model = Post
        fields = [
            "person_name",
            "person_job",
        ]

class DetailForm(forms.ModelForm):
    details = forms.CharField()
    
    
    class Meta:
        model = Post
        fields = [
            "details",
        ]