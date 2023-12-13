from django.db import models
from django.utils import timezone

# Create your models here.

class TimeSeries(models.Model):
    dateTime = models.DateTimeField()
    value = models.FloatField()

    def value_was_too_high(self):
        return self.value >= 300
    
    def value_was_too_low(self):
        return self.value <= 130
    
    def __str__(self) -> str:
        return f"{{{self.dateTime}}}:{{{self.value}}}"