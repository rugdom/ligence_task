from api.models import DICOMFile
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from api.serializers import DICOMFileSerializer, DICOMFileDetailSerializer


class DICOMFileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DICOMFile.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DICOMFileDetailSerializer
        else : 
            return DICOMFileSerializer


class DownloadFileView(APIView):
    def get(self, request, filename):
        file_path = f'files/{filename}'
        dicom_file = get_object_or_404(DICOMFile, file=file_path)
        response = HttpResponse(open(dicom_file.file.path, 'rb'), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename={dicom_file.file.name}'
        return response
