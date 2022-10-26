from django.contrib import admin

from .models import Listing, Thread

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_filter = ("author", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class ThreadAdmin(admin.ModelAdmin):
    list_filter = ("user", "receiver",)
    list_display = ("user", "receiver",)

admin.site.register(Listing, ListingAdmin)
admin.site.register(Thread, ThreadAdmin)