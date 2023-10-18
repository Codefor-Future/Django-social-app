from django import forms
from .models import Rweet


class RweetForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(attrs={
                               "placeholder": "Say something...",
                               "class": "textarea is-success is-medium",
                           }), label="",
                           )

    class Meta:
        model = Rweet
        exclude = ("user", )
