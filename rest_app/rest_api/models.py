from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=256)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name