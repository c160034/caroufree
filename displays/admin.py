from django.contrib import admin

from .models import Listing, User

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_filter = ("user", "date",)
    list_display = ("title", "date", "user",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Listing, ListingAdmin)
admin.site.register(User)