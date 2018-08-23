from django import forms
from django.core import validators
from django_app.models import OurUsers


class UserForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        validators=[validators.MaxLengthValidator(15),
                    validators.MinLengthValidator(2),
                    validators.RegexValidator(r'^[A-Za-z]*$')])
    last_name = forms.CharField(
        required=True,
        validators=[validators.MaxLengthValidator(15),
                    validators.MinLengthValidator(2),
                    validators.RegexValidator(r'^[A-Za-z]*$')])
    email = forms.EmailField()


class UserModelForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = OurUsers
        fields = "__all__"
