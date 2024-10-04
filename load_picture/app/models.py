from django.db import models


class Picture(models.Model):

    image = models.ImageField(
        upload_to='media/',
        blank=True
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
