from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("listings", views.AllListingsView.as_view(), name="listings-page"),
    path("listings/<slug:slug>", views.SingleListingView.as_view(),
         name="listing-detail-page")
]
