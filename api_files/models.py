from django.db import models


class File(models.Model):

    file = models.FileField(max_length=255, upload_to='./files/files')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return 'Файлы'

    class Meta:
        ordering = ['-uploaded_at']
