from django.db import models
from django.shortcuts import reverse

class PdfStore(models.Model):
    title = models.CharField(max_length=100)
    matire = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("isima_trivez:detail", kwargs={
            'slug': self.slug
        })

class PdfImages(models.Model):
    post = models.ForeignKey(PdfStore, on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True)