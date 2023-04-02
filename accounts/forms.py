from django import forms

from new_app.models import Vacancy


class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
    )


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ("text", "author")
        labels = {
            'author': 'Автор',
            'text': 'Текст',
        }