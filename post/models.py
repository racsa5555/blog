from django.db import models
from category.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, 
        null=True,
        related_name='posts'
    )
    owner = models.ForeignKey(
        'auth.User', 
        related_name='posts',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return self.title
