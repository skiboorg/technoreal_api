from django.contrib import admin
from .models import *

# ===========================
# ClientReview
# ===========================
@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('order', 'client_name', 'client_position')
    ordering = ('order',)

# ===========================
# Project Results Inline
# ===========================
class ProjectResultInline(admin.TabularInline):
    model = ProjectResult
    extra = 1

# ===========================
# Project Gallery Inline
# ===========================
class ProjectGalleryImageInline(admin.TabularInline):
    model = ProjectGalleryImage
    extra = 1

# ===========================
# Project Admin
# ===========================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_on_main')
    inlines = [ProjectResultInline, ProjectGalleryImageInline]
    filter_horizontal = ('services',)  # удобно выбирать связанные услуги

# ===========================
# Service Admin
# ===========================
class ProjectInlineForService(admin.TabularInline):
    model = Service.projects.through  # связь ManyToMany через промежуточную таблицу
    extra = 1

class ServiceGalleryImageInlineForService(admin.TabularInline):
    model = ServiceGalleryImage  # связь ManyToMany через промежуточную таблицу
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'show_on_main')
    inlines = [ProjectInlineForService,ServiceGalleryImageInlineForService]
    ordering = ('order',)
    filter_horizontal = ('projects',)

class VariantOptionlineForService(admin.TabularInline):
    model = VariantOption  # связь ManyToMany через промежуточную таблицу
    extra = 1

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [VariantOptionlineForService]