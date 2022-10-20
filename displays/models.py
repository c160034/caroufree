from django.db import models

# Create your models here.

class Author(models.Model):
    username = models.CharField(max_length=50)
    email_address = models.EmailField()

    def __str__(self) -> str:
        return self.username

class Listing(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="listings", null=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="listings")