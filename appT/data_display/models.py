from django.db import models
from django.utils import timezone

# Create your models here.

class RawData(models.Model):
    dateTime = models.DateTimeField()
    value = models.FloatField()

    def value_was_too_high(self):
        return self.value >= 300
    
    def value_was_too_low(self):
        return self.value <= 130
    
    def __str__(self) -> str:
        return f"{{{self.dateTime}}}:{{{self.value}}}"
    
class Data15T(RawData):
    pass

class Data60T(RawData):
    pass

class Data1D(RawData):
    pass