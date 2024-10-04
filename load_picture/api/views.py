from rest_framework import generics, status
from rest_framework.response import Response

from api.serializers import LoadPictureSerializers


class LoadPictureView(generics.CreateAPIView):

    serializer_class = LoadPictureSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
