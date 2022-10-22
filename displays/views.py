from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.defaultfilters import slugify
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Listing
from .forms import ListingForm, CreateUserForm


class StartingPageView(ListView):
    template_name = "displays/index.html"
    model = Listing
    ordering = ["-date"]
    context_object_name = "listings"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllListingsView(ListView):
    template_name = "displays/all-listings.html"
    model = Listing
    ordering = ["-date"]
    context_object_name = "listings"

class SingleListingView(DetailView):
    template_name = "displays/listing-detail.html"
    model = Listing


class NewListingView(View):
    def get(self, request):
        form = ListingForm()
        return render(request, "displays/new-listing.html", {'form': form})

    def post(self, request):
        form = ListingForm(request.POST, request.FILES)
        title = request.POST.get('title')
        strtime = "".join(str(datetime.datetime.now()).split("."))
        string = "%s-%s" % (title,strtime[7:])
        slug = slugify(string)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug=slug
            form.save()
            return HttpResponseRedirect(reverse("listing-detail-page", args=[slug]))
        return render(request, "displays/new-listing.html", {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('/listings')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('/login/')
        context = {'form':form}
        return render(request, "displays/register.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/listings')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/listings')
            else: 
                messages.info(request,'Username OR password is incorrect')
        
        context = {}
        return render(request, "displays/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('/login/')