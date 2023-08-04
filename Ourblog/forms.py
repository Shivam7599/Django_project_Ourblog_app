from django import forms 
from .models import Poster, Category, Comment


# giving coices to Category as a list
# cats = [('coding', 'coding'), ('sports', 'sports'), ('Entertainment', 'Entertainment'),]  Not A Right Way

choices = Category.objects.all().values_list('name', 'name')
choices_list = []
for i in choices:
    choices_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model = Poster
        # fields = "__all__"
        fields = ('title', 'title_tag', 'author', 'category', 'snippet', 'header_image', 'body' )

        # now we add some style to form
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the title-'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the title-'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'id': 'decision', 'type': 'hidden'}),
            # 'author' : forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Author'}),
            'category' : forms.Select(choices = choices_list, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Enter the Text-'}),
            'snippet' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Poster
        # fields = "__all__"
        fields = ('title', 'title_tag', 'category', 'snippet', 'header_image', 'body')

        # now we add some style to form
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the title-'}),
            'author' : forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Author'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the title-'}),
            'category' : forms.Select(choices = choices_list, attrs={'class': 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Enter the Text-'}),
            }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Enter the Text-'}),
            }