from django.contrib import sitemaps
from django.urls import reverse

from projects.models import Project


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "home",
            "about",
            "skills",
            "projects",
            "contact",
        ]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(sitemaps.Sitemap):
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse(
            "project_detail",
            kwargs={"slug": obj.slug}
        )

    def lastmod(self, obj):
        return obj.updated_at
