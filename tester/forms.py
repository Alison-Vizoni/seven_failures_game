from django import forms
from django.contrib.auth.hashers import verify_password

from tester.models import Tester


class TesterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super().clean()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            tester = Tester.objects.get(username=username)
        except Tester.DoesNotExist:
            raise forms.ValidationError("Username or password incorrectly.", code='invalid')

        is_correct, _ = verify_password(password, tester.password)
        if not is_correct:
            raise forms.ValidationError("Username or password incorrectly.", code='invalid')
