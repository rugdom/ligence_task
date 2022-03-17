from django.contrib import admin
from django.urls import path, include
from api.views import DownloadFileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('files/<str:filename>/', DownloadFileView.as_view())
]
