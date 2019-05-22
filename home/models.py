from django.db import models

# Create your models here.

class Stone(models.Model):
    stone= models.CharField(max_length=100)
    shortdesc = models.CharField(max_length=100 , null=True)
    description = models.TextField()
    images = models.ImageField(upload_to='images/', blank=True)
    images2 = models.ImageField(upload_to='images/', blank=True)
    images3 = models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.stone[:100]