from django.contrib import admin
from .models import Stock # Stock is class in models.py
# Register your models here.

admin.site.register(Stock)