from django.db import models
from django.urls import reverse # new

# Create your models here.
class Surgery(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_opened = models.DateField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('s_detail', args=[str(self.id)])

class Patient(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    surgery = models.ForeignKey(
        Surgery,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('p_detail', args=[str(self.id)])

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    num_patients = models.PositiveIntegerField()
    surgery = models.ForeignKey(
        Surgery,
        on_delete=models.CASCADE,
    )
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('d_detail', args=[str(self.id)])
