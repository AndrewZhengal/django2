from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Author, Category, Newsletter, Comment


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'short_description')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Newsletter)
admin.site.register(Comment)
