from django.db import models


# Create your models here.
class Post(models.Model):
    DRAFT = 0
    PUBLISH = 1
    REJECTED = 2
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISH, 'Publish'),
        (REJECTED, 'Rejected'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    keywords = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField()
    meta_keywords = models.TextField(max_length=500, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
