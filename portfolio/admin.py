from django.contrib import admin
from django.db import models
from .models import Project, ProjectImage, PortfolioShortIntro
from ckeditor.widgets import CKEditorWidget


class ProjectImageInline(admin.StackedInline):
    extra = 1
    model = ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ProjectImageInline,
    ]

    class Meta:
        model = Project


class PortfolioShortIntroAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(Project, ProjectAdmin)
admin.site.register(PortfolioShortIntro, PortfolioShortIntroAdmin)

