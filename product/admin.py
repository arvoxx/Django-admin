
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'price',
        'discount_price',
        'stock',
        'is_active',
        'create_at',
    )

    list_filter = ('category', 'is_active', 'create_at')
    search_fields = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('price', 'stock', 'is_active')
    readonly_fields = ('create_at',)
    ordering = ('-create_at',)
    list_per_page = 20
