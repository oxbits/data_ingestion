from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (
    DataFile, 
)
from .tasks import process_file                                             

@receiver(post_save, sender=DataFile)
def my_handler(sender, **kwargs):
    
    file_path = str(settings.MEDIA_ROOT + '/' + str(kwargs['instance'].data_file))

    process_file.delay(file_path)
