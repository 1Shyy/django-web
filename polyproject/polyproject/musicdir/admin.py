from django.contrib import admin
from .models import Musicdir, Category


class MusicdirAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'category', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('category', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Musicdir, MusicdirAdmin)
admin.site.register(Category, CategoryAdmin)
