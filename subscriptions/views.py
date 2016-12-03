from django.shortcuts import render
from .models import Subscription


def main(request):
    return render(request, 'subscriptions/main.html', {})


def photos_list(request):
    return render(request, 'subscriptions/photos_list.html', {})


def photo_big(request):
    return render(request, 'subscriptions/photo_big.html', {})


def send_photo(request):
    return render(request, 'subscriptions/send_photo.html', {})


def subs_list(request):
    username = None
    if request.user.is_authenticated():
        user = request.user
    subscriptions = Subscription.objects.filter(user=user, is_active=True).order_by('created_date')
    return render(request, 'subscriptions/subs_list.html', {'user_subscriptions_list' : subscriptions})


def subs_new(request):
    return render(request, 'subscriptions/subs_new.html', {})


def subs_edit(request):
    return render(request, 'subscriptions/subs_edit.html', {})


def login(request):
    return render(request, 'subscriptions/login.html', {})


def logout(request):
    return render(request, 'subscriptions/logout.html', {})

