from django import forms

from .models import Post , Comment, People, Places ,Comment2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name','title','image')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'text',)

class Comment2Form(forms.ModelForm):

    class Meta:
        model = Comment2
        fields = ('name', 'text',)

class PeopleForm(forms.ModelForm):

    class Meta:
        model = People
        fields = ('name', 'title', 'image_people',)


class PlacesForm(forms.ModelForm):

    class Meta:
        model = Places
        fields = ('name','title', 'image_places',)

class loginForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'password', )


class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2', )
