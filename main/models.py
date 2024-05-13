from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='images/')  # Adjust upload path as needed
