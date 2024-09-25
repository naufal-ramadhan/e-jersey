import uuid
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

     JERSEY_TYPE = [
        ("club", "Club Jersey"),
        ("nation", "Nation Jersey"),
    ]

     user = models.ForeignKey(User, on_delete=models.CASCADE)
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     name = models.CharField(max_length=255)
     price = models.IntegerField()
     description = models.TextField()
     type = models.CharField(max_length=255, choices=JERSEY_TYPE)
     club = models.CharField(max_length=255)
     slug = models.SlugField(blank=True, unique=True)

     def __str__(self):
          return f"name : {self.name}, type : {self.type}, club : {self.club}"
     
     def save(self, *args, **kwargs):
          if not self.slug:
               self.club = slugify(self.name).replace("-", "")
               self.slug = slugify(self.name)
          super(Product, self).save(*args, **kwargs)