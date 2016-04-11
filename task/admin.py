from django.contrib import admin

from .models import Tag, Task, Attach


class AttachInline(admin.TabularInline):
    model = Attach
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    inlines = [AttachInline]
    list_display = ['title', 'owner', 'created_time', 'last_modified']
    list_filter = ['last_modified',]
    search_fields = ['title']


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag)
admin.site.register(Attach)
