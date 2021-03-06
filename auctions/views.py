from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewListingForm
from .models import Listing, User


@login_required(login_url="login")
def index(request):
    print(f"listings {Listing.objects.all()}")
    return render(request, "auctions/index.html", {
        "listings" : Listing.objects.all() 
    })


@login_required(login_url="login")
def categories(request):
    return render(request, "auctions/categories.html")


@login_required(login_url="login")
def watchlist(request):
    return render(request, "auctions/watchlist.html")


@login_required(login_url="login")
def create_listing(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            listing = Listing()
            listing.title = form.cleaned_data["title"]
            listing.description = form.cleaned_data["description"]
            listing.startingBid = form.cleaned_data["startingBid"]
            listing.imageUrl = form.cleaned_data["imageUrl"]
            listing.category = form.cleaned_data["category"]
            listing.save()
            return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create_listing.html", {
        "form" : NewListingForm(),   
    })

def show_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
