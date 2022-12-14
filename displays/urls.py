from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register-page"),
    path("login/", views.loginPage, name="login-page"),
    path("logout/", views.logoutUser, name="logout-page"),
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("listings", views.AllListingsView.as_view(), name="listings-page"),
    path("listings/new", views.NewListingView.as_view(), name="new-listing-page"),
    path("listings/<slug:slug>", views.SingleListingView.as_view(),
         name="listing-detail-page"),
    path("listings/edit/<slug:slug>", views.UpdateListingView.as_view(), name='edit-listing-page'),
    path("listings/<slug:slug>/delete", views.DeleteListingView.as_view(), name='delete-listing-page'),
    path("inbox/", views.ListThreads.as_view(), name='inbox-page'),
    path("inbox/new", views.CreateThread.as_view(), name='create-thread-page'),
    path("inbox/<int:pk>", views.ThreadView.as_view(), name='thread-page'),
    path("inbox/<int:pk>/create-message", views.CreateMessage.as_view(), name='create-message-page')
]
