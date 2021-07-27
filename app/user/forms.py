from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class NewUser(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password","password2")

    def save_user(self, commit=True):
        user = super(NewUser, self).save_user(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user