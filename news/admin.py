from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'get_photo', 'is_published']
    list_editable = ['is_published', ]

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return mark_safe('<img src="https://picsum.photos/75/">')

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

