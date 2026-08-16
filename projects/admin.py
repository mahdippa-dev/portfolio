from django.contrib import admin

# Register your models here.

from .models import Project
import jdatetime


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'display_order', 'jalali_created_at')
    list_filter = ('is_featured',)
    search_fields = ('title',)

    def jalali_created_at(self, obj):
        if obj.created_at:
            return jdatetime.datetime.fromgregorian(
                datetime=obj.created_at
            ).strftime('%Y/%m/%d - %H:%M')

        return '-'

    jalali_created_at.short_description = 'تاریخ ایجاد'