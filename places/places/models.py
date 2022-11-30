from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    #Measurements 

    def __str__(self):
        return '%s %s' % (self.value, self.unit)