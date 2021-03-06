from django.contrib import admin
from .models import feed, comments, request, resource

# Register your models here.
admin.site.register(feed)
# admin.site.register(comments)
admin.site.register(request)
admin.site.register(resource)