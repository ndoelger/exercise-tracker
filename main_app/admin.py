from django.contrib import admin
from .models import Exercise, Completion, Photo

# Register your models here.
admin.site.register(Exercise)
admin.site.register(Completion)
admin.site.register(Photo)