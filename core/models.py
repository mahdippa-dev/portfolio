from django.db import models


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, verbose_name='عناون نمایشی در پنل ادمین')
    description = models.TextField(max_length=2000, verbose_name='متن توضیحات',
                                   help_text='متن درباره من رو اینجا بنویسید.')

    class Meta:
        verbose_name = 'درباره من',
        verbose_name_plural = 'درباره من'

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    name = models.CharField(unique=True, max_length=100, help_text='نام دسته مهارت را وارد کنید.',
                            verbose_name='دسته مهارت')
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name='ترتیب نمایش',
        help_text='عدد کوچک‌تر زودتر نمایش داده می‌شود.'
    )

    description = models.TextField(
        max_length=300,
        blank=True,
        verbose_name='توضیحات دسته',
        help_text='توضیح کوتاهی درباره این دسته از مهارت‌ها وارد کنید.'
    )

    class Meta:
        verbose_name = 'دسته بندی مهارت',
        verbose_name_plural = 'دسته بندی مهارت ها'

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.PROTECT,
        related_name="skills", verbose_name='دسته بندی')
    title = models.CharField(max_length=200, help_text='عنوان مهارت را وارد کنید.', verbose_name='عنوان مهارت')
    skill_image = models.ImageField(verbose_name='تصویر مهارت',
                                    help_text='تصویر مهارت را وارد کنید. حداقل ابعاد 80 * 80 پیکسل (1:1)',
                                    upload_to='core&contact_page/skills/icons/', )
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name='ترتیب نمایش',
        help_text='عدد کوچک‌تر زودتر نمایش داده می‌شود.'
    )
    displayStatus = models.BooleanField(default=True, verbose_name='وضعیت نمایش',
                                        help_text='در صورت غیر فعال بودن، نمایش داده نمی شود.')

    class Meta:
        verbose_name = 'مهارت',
        verbose_name_plural = 'مهارت ها'

    def __str__(self):
        return self.title


class Footer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="نام"
    )

    description = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="توضیحات"
    )

    github_link = models.URLField(
        verbose_name="لینک GitHub"
    )

    linkedin_link = models.URLField(
        verbose_name="لینک LinkedIn"
    )

    instagram_link = models.URLField(
        blank=True,
        verbose_name="لینک Instagram"
    )

    telegram_link = models.URLField(
        blank=True,
        verbose_name="لینک Telegram"
    )

    iranian_social_link = models.URLField(
        blank=True,
        verbose_name="لینک شبکه اجتماعی داخلی",
        help_text="در صورت تمایل لینک یک شبکه اجتماعی ایرانی را وارد کنید."
    )

    email = models.EmailField(
        blank=True,
        verbose_name="ایمیل"
    )

    class Meta:
        verbose_name = "فوتر"
        verbose_name_plural = "فوتر"

    def __str__(self):
        return self.name
