from django.utils.safestring import mark_safe

from .models import *
from django.contrib import admin



class WomenAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    admin.site.site_title = 'Админ-панель сайта рецептов'
    admin.site.site_header = 'Админ-панель сайта рецептов'

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        else:
            return "Нет фото"

    get_html_photo.short_description = "Миниатюра"

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)


