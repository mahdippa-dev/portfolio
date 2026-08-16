from django.contrib import admin
from .models import AboutPage
import jdatetime


# Register your models here.

@admin.register(AboutPage)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile_image', 'jalali_updated_at')

    def jalali_updated_at(self, obj):
        if obj.updated_at:
            return jdatetime.datetime.fromgregorian(
                datetime=obj.updated_at
            ).strftime('%Y/%m/%d - %H:%M')

        return '-'

    jalali_updated_at.short_description = 'آخرین بروزرسانی'

    def has_add_permission(self, request):
        # فقط اگر هیچ رکوردی وجود نداشت اجازه ساخت بده
        return not AboutPage.objects.exists()
