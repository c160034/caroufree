from django.contrib import admin

from .models import Listing, Author

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_filter = ("author", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Listing, ListingAdmin)
admin.site.register(Author)