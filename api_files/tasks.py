from celery import shared_task



FORMAT = ['txt', 'pdf', 'jpg', 'png']

@shared_task
def validate_file(pk):
    from .models import File

    file = File.objects.get(pk=pk)
    format = ''.join((str(file.file)).split('.')[-1:])

    if format in FORMAT:
        file.processed = True
        file.save()









