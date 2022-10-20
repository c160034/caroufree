from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Listing
from .forms import ListingForm

class StartingPageView(ListView):
    template_name = "displays/index.html"
    model = Listing
    ordering = ["-date"]
    context_object_name = "listings"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def starting_page(request):
#     latest_listings = Listing.objects.all().order_by("-date")[:3]
#     return render(request, "displays/index.html", {
#         "listings": latest_listings
#     })

class AllListingsView(ListView):
    template_name = "displays/all-listings.html"
    model = Listing
    ordering = ["-date"]
    context_object_name = "listings"

# def listings(request):
#     all_listings = Listing.objects.all().order_by("-date")
#     return render(request, "displays/all-listings.html", {
#         "listings": all_listings
#     })

class SingleListingView(DetailView):
    template_name = "displays/listing-detail.html"
    model = Listing

# def listing_detail(request, slug):
#     identified_listing = get_object_or_404(Listing, slug=slug)
#     return render(request, "displays/listing-detail.html", {
#         "listing": identified_listing
#     })

class NewListingView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "displays/new-listing.html"
    success_url = "/displays"
