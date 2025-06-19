from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_completed')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title',)

admin.site.register(Todo)
# Register your models here.
