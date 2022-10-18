from django.shortcuts import render, get_object_or_404

from .models import Listing

def starting_page(request):
    latest_listings = Listing.objects.all().order_by("-date")[:3]
    return render(request, "displays/index.html", {
        "listings": latest_listings
    })

def listings(request):
    all_listings = Listing.objects.all().order_by("-date")
    return render(request, "displays/all-listings.html", {
        "listings": all_listings
    })

def listing_detail(request, slug):
    identified_listing = get_object_or_404(Listing, slug=slug)
    return render(request, "displays/listing-detail.html", {
        "listing": identified_listing
    })
