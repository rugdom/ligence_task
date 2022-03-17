import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()

from pydicom import dcmread
from datetime import datetime, timedelta
from django.core.files import File
from api.models import DICOMFile
 
ds = dcmread("image-00000.dcm")
patients = ['Tom', 'John', 'Lucy', 'Ben', 'Emma']
study_datetime = datetime.now()

for idx, patient in enumerate(patients, start=1):
    ds.PatientName = patient
    ds.StudyDate = study_datetime.strftime('%Y%m%d')
    ds.StudyTime = study_datetime.strftime('%H%M%S')
    study_datetime = study_datetime + timedelta(days=1, hours=1)
    file_path = f'image-0{idx}.dcm'
    ds.save_as(file_path)
    with open(file_path, 'rb') as f:
        file = File(f)
        dicom_file = DICOMFile(file=file)
        dicom_file.save()
    