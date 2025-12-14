from django.contrib import admin
from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Category."""

    list_display = (
        'title',
        'description',
        'slug',
        'created_at',
        'is_published'
    )
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('slug',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Location."""

    list_display = (
        'name',
        'created_at',
        'is_published'
    )
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Post."""

    list_display = (
        'title',
        'text',
        'author',
        'pub_date',
        'category',
        'location',
        'is_published'
    )
    list_editable = ('category', 'location')
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)