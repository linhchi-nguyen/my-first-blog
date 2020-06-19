from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('title', 'text','thumb','category','location')

         widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control'}),
             'text': forms.Textarea(attrs={'class': 'form-control'}),
             'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
             'location': forms.TextInput(attrs={'class': 'form-control'}),
         }