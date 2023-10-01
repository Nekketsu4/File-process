
from django.contrib import admin
from django.urls import path
from api_files.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', FileDownloadView.as_view()),
    path('files/', FileListView.as_view()),
]
