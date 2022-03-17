from django.db import models
from pydicom import dcmread

# Create your models here.
class DICOMFile(models.Model):
    file = models.FileField(upload_to='files')

    @property
    def file_data(self):
        ds = dcmread(self.file.file.name)
        return convert_to_dict(ds)


def convert_to_dict(dataset):
    data_dict = {}
    for data_element in dataset:
        if data_element.VR == "SQ":   # a sequence
            data_dict[data_element.name] = ""
            for sequence_item in data_element.value:
                convert_to_dict(sequence_item)
        else:
            repr_value = repr(data_element.value)
            if len(repr_value) > 50:
                repr_value = repr_value[:50] + "..."
            data_dict[data_element.name] = repr_value
    return data_dict