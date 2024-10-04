from rest_framework import serializers

from app.models import Picture


class LoadPictureSerializers(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ['image',]