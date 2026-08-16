from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
import jdatetime

# Create your models here.

class AboutPage(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='عنوان صفحه'
    )

    short_intro = models.TextField(
        max_length=500,
        verbose_name='معرفی کوتاه'
    )

    profile_image = models.ImageField(
        upload_to='core&contact_page/about/',
        verbose_name='تصویر',
        help_text='ابعاد تصویر باید 1500 * 1200 پیکسل (نسبت 4:5) و با ده درصد حاشیه امن باشد.'
    )

    content = CKEditor5Field(
        verbose_name='محتوای اصلی'
    )

    github_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک گیت‌هاب'
    )

    linkedin_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک لینکدین'
    )

    telegram_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک تلگرام'
    )

    iranian_social_link = models.URLField(
        blank=True,
        verbose_name="لینک شبکه اجتماعی داخلی",
        help_text="در صورت تمایل لینک یک شبکه اجتماعی ایرانی را وارد کنید."
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='آخرین بروزرسانی'
    )
    class Meta:
        verbose_name = 'صفحه درباره من',
        verbose_name_plural = 'صفحه درباره من'

    def __str__(self):
        return self.title