from django.contrib import admin
from .models import VideoData
# Register your models here.


@admin.register(VideoData)
class VideoDataAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'publishing_datetime')
    list_display = ('title',)
    list_filter = ('title', 'publishing_datetime')
    ordering = ('-publishing_datetime',)
    search_fields = ('title__icontains', 'description__icontains')
    date_hierarchy = 'publishing_datetime'
    pass
