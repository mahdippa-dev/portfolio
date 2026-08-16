from django.contrib import admin

# Register your models here.
from .models import SkillCategory, About, Skill, Footer


@admin.register(About)
class aboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        # فقط اگر هیچ رکوردی وجود نداشت اجازه ساخت بده
        return not About.objects.exists()


@admin.register(SkillCategory)
class SkillcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'category', 'displayStatus')
    list_filter = ('category', 'displayStatus')


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'telegram_link',
        'github_link',
        'linkedin_link',
    )

    def has_add_permission(self, request):
        # فقط اگر هیچ رکوردی وجود نداشت اجازه ساخت بده
        return not Footer.objects.exists()
