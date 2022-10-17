from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def starting_page(request):
    return render(request, "displays/index.html")

def listings(request):
    return render(request, "displays/all-listings.html")

def listing_detail(request, slug):
    return render(request, "displays/listing-detail.html")
