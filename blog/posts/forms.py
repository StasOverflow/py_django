from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

    def clean_title(self):
        data = self.cleaned_data['title']
        if len(data) < 5:
            raise forms.ValidationError("Title name is way too short!")
        return data

    def clean_content(self):
        data = self.cleaned_data['content']
        if len(data) < 30:
            raise forms.ValidationError("Pls, write some more text content")
        return data


class PostFormBackup(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    content = forms.CharField(label='Content', max_length=300)

    def clean_title(self):
        data = self.cleaned_data['title']
        if len(data) < 5:
            raise forms.ValidationError("Title name is way too short!")
        return data

    def clean_content(self):
        data = self.cleaned_data['content']
        if len(data) < 30:
            raise forms.ValidationError("Pls, write some more text content")
        return data

