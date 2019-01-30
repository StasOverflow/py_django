from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    content = forms.CharField(label='Content', max_length=300)
