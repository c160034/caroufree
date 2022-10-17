from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("listings", views.listings, name="listings-page"),
    path("listings/<slug:slug>", views.listing_detail,
         name="listing-detail-page")
]
