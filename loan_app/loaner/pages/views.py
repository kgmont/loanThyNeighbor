from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def borrow_view(request, *args, **kwargs):
    return render(request, "borrow.html", {})

def loan_view(request, *args, **kwargs):
    return render(request, "loan.html", {})

def profile_view(request, *args, **kwargs):
    return render(request, "profile.html", {})

def loanlist_view(request, *args, **kwargs):
    return render(request, "loanlist.html", {})

def borrowlist_view(request, *args, **kwargs):
    return render(request, "borrowlist.html", {})

def search_view(request, *args, **kwargs):
    return render(request, "search.html", {})