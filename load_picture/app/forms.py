from django import forms

from app.models import Picture


class CreateLoadPictureForm(forms.ModelForm):

    image = forms.FileField(max_length=200, label="", )

    class Meta:
        model = Picture
        fields = ['image']
