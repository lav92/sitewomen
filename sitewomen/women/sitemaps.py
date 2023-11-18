from django.contrib.sitemaps import Sitemap
from .models import Women


class PostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Women.published.all()

    def lastmod(self, obj):
        return obj.time_update


class SubjectSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.85

    def items(self):
        return Subject.objects.filter(is_active=1, volume__gt=0)

    def lastmod(self, obj):
        return obj.time_update
