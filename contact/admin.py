import jdatetime
from django.contrib import admin
from .models import ContactMessage


# Register your models here.

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'email',
        'subject',
        'jalali_updated_at',
    )

    search_fields = (
        'name',
        'phone',
        'email',
        'subject',
    )

    list_filter = (
        'created_at',
    )

    readonly_fields = (
        'created_at',
    )

    def jalali_updated_at(self, obj):
        if obj.created_at:
            return jdatetime.datetime.fromgregorian(
                datetime=obj.created_at
            ).strftime('%Y/%m/%d - %H:%M')

        return '-'

    jalali_updated_at.short_description = 'آخرین بروزرسانی'
