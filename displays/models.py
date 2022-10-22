from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone

# Create your models here.

# class Author(models.Model):
#     username = models.CharField(max_length=50)
#     email_address = models.EmailField()

#     def __str__(self) -> str:
#         return self.username

class Listing(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="listings", null=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")

# class Thread(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

# class Message(models.Model):
#     thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="+", blank=True, null=True)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
#     body = models.CharField(max_length=1000)
#     image = models.ImageField(upload_to="messages", blank=True, null=True)
#     date = models.DateTimeField(default=timezone.now)
#     is_read = models.BooleanField(default=False)