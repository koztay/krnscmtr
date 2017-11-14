from django.contrib import admin
# here below is for Flatpages CKEditor integration
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from ckeditor.widgets import CKEditorWidget

from .models import BrandImage, SliderImageThumb, SliderImage


# FlatPages CKEditor integration
class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)
admin.site.register(BrandImage)
admin.site.register(SliderImage)
admin.site.register(SliderImageThumb)

