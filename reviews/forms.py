from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Review, Comment

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="",
    )
    password2 = forms.CharField(
        label=("비밀번호 확인"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="",
    )

    class Meta:
        model = get_user_model()
        fields = ("username",)
        labels = {
            'username' : "아이디",
        }
        help_texts = {
            'username' : "",
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username',)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs = {
            "placeholder": "댓글을 작성해 주세요",
        }
        self.fields["content"].help_text = None

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'image', 'grade']