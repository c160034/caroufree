from queue import Empty
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.models import User

from .models import Listing, Thread, Message, Notification
from .forms import ListingForm, CreateUserForm, ThreadForm, MessageForm


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

class UpdateListingView(UpdateView):
    model = Listing
    fields = ['title', 'image', 'description']
    template_name = "displays/edit.html"

class DeleteListingView(DeleteView):
    model = Listing
    template_name = "displays/partials/delete.html"
    success_url = reverse_lazy("listings-page")

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
                messages.warning(request,'Username OR password is incorrect')
        
        context = {}
        return render(request, "displays/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('/login/')

class ListThreads(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if Notification.objects.filter(to_user=request.user).exclude(user_has_seen=True):
                notification = Notification.objects.filter(to_user=request.user).exclude(user_has_seen=True)[0]
                notification.user_has_seen = True
                notification.save()
            threads = Thread.objects.filter(Q(user=request.user) | Q(receiver=request.user))
            context = {
                'threads': threads
            }
            return render(request, 'displays/inbox.html', context)
        else: 
            messages.warning(request,'You need to be logged in first!')
            return redirect('login-page')
    
class CreateThread(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = ThreadForm()
            context = {
                'form': form
            }
            return render(request, 'displays/create-thread.html', context)
        else: 
            messages.warning(request,'You need to be logged in first!')
            return redirect('login-page')

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)
        username = request.POST.get('username')
        try:
            receiver = User.objects.get(username=username)
            if request.user != receiver:
                if Thread.objects.filter(user=request.user, receiver=receiver).exists():
                    thread =  Thread.objects.filter(user=request.user, receiver=receiver)[0]
                    return redirect('thread-page', pk=thread.pk)
                elif Thread.objects.filter(user=receiver, receiver=request.user).exists():
                    thread =  Thread.objects.filter(user=receiver, receiver=request.user)[0]
                    return redirect('thread-page', pk=thread.pk)  
                if form.is_valid():
                    thread = Thread(
                        user=request.user,
                        receiver=receiver
                    )
                    thread.save()
                    return redirect('thread-page', pk=thread.pk)
            else: 
                messages.warning(request,'You cannot send message to yourself')
                return redirect('create-thread-page')
        # except Exception as e:
            # print(e)
        except:
                return redirect('login-page')

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = Thread.objects.get(pk=pk)
        messages = Message.objects.filter(thread__pk__contains=pk)
        dates = messages.values_list("date__date", flat=True).distinct()
        context = {
            'thread': thread,
            'form': form,
            'messages': messages,
            'dates': dates
        }
        return render(request, 'displays/thread.html', context)

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = Thread.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver
        
        message = Message(
            thread = thread,
            sender = request.user,
            receiver = receiver,
            body = request.POST.get('message'),
            image = request.FILES.get('image')
        ) 
        message.save()
        print(Notification.objects.filter(to_user=receiver).exclude(user_has_seen=True))
        if Notification.objects.filter(to_user=receiver).exclude(user_has_seen=True).count() == 0:
            notification = Notification.objects.create(
                to_user=receiver,
            )
            notification.save()
        return redirect('thread-page', pk=pk)
