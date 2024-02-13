from django.contrib import admin
from .models        import *

# Register your models here.

admin.site.register(product)
admin.site.register(category)

# @admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display    = ['user', 'Product','review', 'rate']

admin.site.register(Review, ReviewAdmin)