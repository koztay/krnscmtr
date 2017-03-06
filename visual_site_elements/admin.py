from django.contrib import admin
# here below is for Flatpages CKEditor integration
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from ckeditor.widgets import CKEditorWidget

from .models import Brand, BrandImage


# FlatPages CKEditor integration
class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)


class BrandImageInline(admin.StackedInline):
    extra = 1
    model = BrandImage


class BrandAdmin(admin.ModelAdmin):
    inlines = [
        BrandImageInline,
    ]

    class Meta:
        model = Brand

admin.site.register(Brand, BrandAdmin)

