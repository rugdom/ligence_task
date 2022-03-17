from rest_framework import serializers
from api.models import DICOMFile


class DICOMFileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DICOMFile
        fields = ['pk', 'file']


class DICOMFileDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DICOMFile
        fields = ['pk', 'file', 'file_data']
        