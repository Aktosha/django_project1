from django.contrib import admin
from .models import Posts


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp', 'publish']
    search_fields = ['id', 'title', 'description']


admin.site.register(Posts, PostAdmin)
