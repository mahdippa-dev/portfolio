from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان پروژه', help_text='عنوان پروژه را وارد کنید.')
    short_description = models.TextField(max_length=250, verbose_name='توضیح کوتاه',
                                         help_text='توضیح کوتاه برای نمایش در صفحه اصلی')

    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='اسلاگ'
    )

    description = CKEditor5Field(
        verbose_name="توضیحات اصلی پروژه"
    )

    cover_desktop = models.ImageField(
        upload_to="projects/covers/desktop/",
        verbose_name="تصویر کاور دسکتاپ",
        help_text="نسبت تصویر 675 * 1200 پیکسل (16:9) و با ده درصد حاشیه امن باشد."
    )

    cover_mobile = models.ImageField(
        upload_to="projects/covers/mobile/",
        verbose_name="تصویر کاور موبایل",
        help_text="نسبت تصویر باید 900 * 600 (2:3) و با ده درصد حاشیه امن باشد."
    )

    github_link = models.URLField(
        blank=True,
        null=True,
        verbose_name="لینک گیت‌هاب"
    )

    live_link = models.URLField(
        blank=True,
        null=True,
        verbose_name="لینک سایت"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="نمایش در صفحه اصلی"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش",
        help_text="عدد کوچک‌تر، زودتر نمایش داده می‌شود."
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"

    def __str__(self):
        return self.title