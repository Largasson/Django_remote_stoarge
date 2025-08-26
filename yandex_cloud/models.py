from yandex_cloud.custom_media_storage import MediaStorage
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

media_storage = MediaStorage()


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos/", storage=media_storage)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Photo)
def delete_file_from_storage(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
