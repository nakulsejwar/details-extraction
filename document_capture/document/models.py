from django.db import models

class Aadhar(models.Model):
    aadhar_number = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.aadhar_number
