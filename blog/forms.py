from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		geeks_field = forms.ImageField()
		fields = ('poster', 'title', 'genre', 'text')