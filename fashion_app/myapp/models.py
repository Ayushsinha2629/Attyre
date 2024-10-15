from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    display_name = models.CharField(max_length=255)
    profile_picture_url = models.URLField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers_count = models.PositiveIntegerField(default=0)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Store(models.Model):
    name = models.CharField(max_length=255)
    logo_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Variant(models.Model):
    name = models.CharField(max_length=100)
    options = models.JSONField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.PositiveIntegerField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    timestamp = models.PositiveIntegerField()
    currency = models.CharField(max_length=10, default='USD')
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
    variants = models.ManyToManyField(Variant, related_name='products')

    def __str__(self):
        return self.name

class Music(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.name} by {self.artist}"
    

class Video(models.Model):
    video_url = models.URLField(max_length=500)
    thumbnail_url = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField()
    view_count = models.PositiveIntegerField(default=0)
    duration = models.PositiveIntegerField()  # Duration in seconds
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='videos', blank=True)
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    shares_count = models.PositiveIntegerField(default=0)
    is_liked = models.BooleanField(default=False)  # Typically handled per user
    is_bookmarked = models.BooleanField(default=False)  # Typically handled per user
    music = models.ForeignKey(Music, related_name='videos', on_delete=models.SET_NULL, null=True, blank=True)
    hashtags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Video {self.id} by {self.user.username}"