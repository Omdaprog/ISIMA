from django.contrib import admin
from .models import PdfStore, PdfImages

admin.site.register(PdfStore)
admin.site.register(PdfImages)