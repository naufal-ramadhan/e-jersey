from django.db import models
from django.utils.text import slugify

# Create your models here.
class Jersey(models.Model):
     name = models.CharField(max_length=255)
     price = models.IntegerField()
     description = models.TextField()
     type = models.CharField(max_length=255)
     club = models.CharField(max_length=255)
     slug = models.SlugField(blank=True, unique=True)

     def __str__(self):
          return f"name : {self.name}, type : {self.type}, club : {self.club}"
     
     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.name)
          super(Jersey, self).save(*args, **kwargs)