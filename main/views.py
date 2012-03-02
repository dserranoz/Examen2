from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from django.template import RequestContext
from main.models import Tweet
from main.forms import TweetForm
from main.models import Zombie
from main.forms import ZombieForm


#@cache_page(60 + 15)
def home(request):
    zombies = Zombie.objects.all()
    return render_to_response('home.html', {
        'zombies': zombies,
    })


#@cache_page(60 + 15)
def show_tweet(request, pk):
    zombiess = get_object_or_404(Zombie, pk=pk)
    return render_to_response('show_tweet.html', {
         'zombiess':     zombiess
    })


#cache_page(60 + 15)
def add_zombie(request):
    form = ZombieForm()
    if request.method == 'POST':
        form = ZombieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_zombie.html', {
        'form': form,
    }, RequestContext(request))


@cache_page(60 + 15)
def add_tweet(request):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_tweet.html', {
        'form': form,
    }, RequestContext(request))


#Para editar el articulo creamos este metodo y en urls.py
def edit_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    form = TweetForm(instance=tweet)
    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_tweet.html', {
        'form': form,
    }, RequestContext(request))


def edit_zombie(request, pk):
    zombie = get_object_or_404(Zombie, pk=pk)
    form = ZombieForm(instance=zombie)
    if request.method == 'POST':
        form = ZombieForm(request.POST, instance=zombie)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_zombie.html', {
        'form': form,
    }, RequestContext(request))


def delete_zombie(request, pk):
    #article = get_object_or_404(Article,pk=pk)
    #article.delete()
    Zombie.objects.filter(pk=pk).delete()
    return redirect('home')


def delete_tweet(request, pk):
    #article = get_object_or_404(Article,pk=pk)
    #article.delete()
    Tweet.objects.filter(pk=pk).delete()
    return redirect('home')
