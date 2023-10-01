from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import FilesSerializer
from .tasks import validate_file
from .models import File


class FileListView(generics.ListAPIView):
    '''Список файлов'''

    queryset = File.objects.all()
    serializer_class = FilesSerializer



class FileDownloadView(APIView):
    '''Валидация пост запроса'''

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FilesSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pk = serializer.data['id']
            validate_file.delay(pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


