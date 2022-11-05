from django.db import models

# Create your models here.
class calendarModel(models.Model):
    description = models.CharField(max_length = 100,null=True,blank=True)
    startDate = models.DateField()
    endDate = models.DateField(null=True,blank=True)
    startTime = models.TimeField(null=True,blank=True)
    endTime = models.TimeField(null=True,blank=True)
