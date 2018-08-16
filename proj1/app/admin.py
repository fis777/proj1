from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin
from .models import Genre

admin.site.register(Genre, MPTTModelAdmin)