from django.contrib.auth.models import User
from django import forms
from .models import Attempt



class UserForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AttemptForm(forms.ModelForm):
    class Meta:
        model = Attempt
        fields = ('user', 'challenge', 'file')


