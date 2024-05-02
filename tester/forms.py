from django import forms


class TesterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=128)

    def is_valid():
        if not all([self.username, self.password, isinstance(username, str), isinstance(password, str)]):
            return False

        try:
            tester = Tester.objects.get(username=self.username, password=self.password)
        except Tester.DoesNotExist:
            return HttpResponse("Username or password incorrectly.", status=404)

