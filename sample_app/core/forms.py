from django import forms
from .models import Post

class PostForm(forms.ModelForm):


    person_name = forms.CharField()
    person_job = forms.CharField()
    # tags = forms.ModelMultipleChoiceField(queryset = taggers.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Post
        fields = [
            "person_name",
            "person_job",
            # "tags"
        ]