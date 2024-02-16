from django.db import models
from django.contrib.auth.models import User

class NewReview(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    property = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    length = models.IntegerField()
    reasonableness = models.IntegerField()
    comprehensiveness = models.IntegerField()
    relevancy = models.IntegerField()
    tonality = models.FloatField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    timestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Reviewed by: {self.author}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="properties/%y/%m/%d/" , null=True , default=None)
    bio = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            output_size = (300, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def __str__(self):
        return self.user.username
    
    
from PIL import Image
import uuid
class Property(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=200, null=True , blank=True)
    description = models.CharField(max_length=200, null=True , blank=True)
    location = models.CharField(max_length=200, null=True , blank=True)
    image = models.ImageField(upload_to="properties/%y/%m/%d/" , null=True , default=None)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            output_size = (300, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def __str__(self):
        return self.name