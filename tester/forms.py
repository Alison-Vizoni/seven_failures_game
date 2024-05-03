from django import forms

from tester.models import Tester


class TesterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super().clean()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            tester = Tester.objects.get(username=username, password=password)
        except Tester.DoesNotExist:
            raise forms.ValidationError("Username or password incorrectly.", code='invalid')

        # TODO validate password
