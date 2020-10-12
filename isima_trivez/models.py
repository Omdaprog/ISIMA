from django.db import models
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('Cours','cours'),
    ('TD','TD'),
    ('DS','DS'),
    ('EX','Examen'),
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    matire = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    description = models.TextField()
    nature = models.CharField(choices=CATEGORY_CHOICES, max_length=5,)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("isima_trivez:detail", kwargs={
            'slug': self.slug
        })

class UploadImages(models.Model):
    post = models.ForeignKey(Post, default=None ,on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True,upload_to='images/')
    
    def __str__(self):
        return self.post.title
