from django.contrib import admin

from helper.models import Helper, Category


@admin.register(Helper)
class HelperAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'updated_at', 'created_at',)
    list_filter = ('status',)
    search_fields = ('title', 'body',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview', 'updated_at', 'created_at',)
    search_fields = ('title',)
