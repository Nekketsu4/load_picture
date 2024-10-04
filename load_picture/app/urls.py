from django.urls import path

from app.views import load_picture, detail
from api.views import  LoadPictureView


app_name = 'app'
urlpatterns = [
    path('detail/<int:pk>/', detail, name='detail'),
    path('api/v1/load/', LoadPictureView.as_view(), name='load_p_view'),
    path('load/', load_picture, name='load_p'),
    ]
