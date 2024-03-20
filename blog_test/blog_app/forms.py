from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Title"}
        ),
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a post"}
        )
    )


class CommentForm(forms.Form):
    post_id = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "post_id"}
        ),
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label= ("Password"), strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
