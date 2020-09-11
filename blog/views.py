from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html")
def about_redirect(*args, **kwargs):
    return redirect("/about/", *args, permanent=True, **kwargs)

def privacy_policy_view(request, *args, **kwargs):
    return render(request, "privacy_policy.html", {})
def privacy_policy_redirect():
    return redirect("/privacy_policy/", *args, permanent=True, **kwargs)

def all_recipes_view(request, *args, **kwargs):
    return render(request, "all_recipes.html", {})
def all_recipes_redirect():
    return redirect("/recipes/", *args, permanent=True, **kwargs)

def banana_bread_view(request, *args, **kwargs):
    name = "The Best Banana Bread"
    description = "You can't go wrong with this banana bread recipe."
    return render(request, "recipes/banana_bread.html", {'name':name, 'description':description})
def banana_bread_redirect():
    return redirect("/recipes/banana_bread/", *args, permanent=True, **kwargs)

def breakfast_sandwich_view(request, *args, **kwargs):
    name = "Deli-Style Breakfast Sandwich"
    description = "Bagel shop taste from the comfort of your own home."
    return render(request, "recipes/breakfast_sandwich.html", {'name':name, 'description':description})
def breakfast_sandwich_redirect():
    return redirect("/recipes/breakfast_sandwich/", *args, permanent=True, **kwargs)

def cookie_dough_cupcakes_view(request, *args, **kwargs):
    name = "Chocolate Chip Cookie Dough Cupcakes"
    description = "Vanilla cupcakes with a soft, cookie dough center."
    return render(request, "recipes/cookie_dough_cupcakes.html", {'name':name, 'description':description})
def cookie_dough_cupcakes_redirect():
    return redirect("/recipes/cookie_dough_cupcakes/", *args, permanent=True, **kwargs)

def lemon_chicken_view(request, *args, **kwargs):
    name = "Simple & Healthy Lemon Chicken"
    description = "The best 470 calorie dinner you'll have this week."
    return render(request, "recipes/lemon_chicken.html", {'name':name, 'description':description})
def lemon_chicken_redirect():
    return redirect("/recipes/lemon_chicken/", *args, permanent=True, **kwargs)

def sweet_cream_cold_brew_view(request, *args, **kwargs):
    name = "Vanilla Sweet Cream Cold Brew"
    description = "The closest you can get to Starbucks at home."
    return render(request, "recipes/sweet_cream_cold_brew.html", {'name':name, 'description':description})
def sweet_cream_cold_brew_redirect(request, *args, **kwargs):
    return redirect("/recipes/sweet_cream_cold_brew/", *args, permanent=True, **kwargs)

def experiments_view(request, *args, **kwargs):
    return render(request, "experiments.html", {})
def experiments_redirect(request, *args, **kwargs):
    return redirect("/experiments/", *args, permanent=True, **kwargs)

def edible_cookie_dough_view(request, *args, **kwargs):
    name = "Experiment #001: Edible Cookie Dough"
    description = "Can baking soda improve the taste of edible cookie dough?"
    return render(request, "experiments/edible_cookie_dough.html", {'name':name, 'description':description})
def edible_cookie_dough_redirect(request, *args, **kwargs):
    return redirect("/experiments/edible_cookie_dough/", *args, permanent=True, **kwargs)

def homemade_grape_jam_view(request, *args, **kwargs):
    name = "Experiment #002: Homemade Grape Jam"
    description = "Can grape jam be made at home without added pectin?"
    return render(request, "experiments/homemade_grape_jam.html", {'name':name, 'description':description})
def homemade_grape_jam_redirect(request, *args, **kwargs):
    return redirect("/experiments/homemade_grape_jam/", *args, permanent=True, **kwargs)

def page_not_found_view(request, *args, **kwargs):
    return render(request, 'errors/404.html', {})

def server_error_view(request, *args, **kwargs):
    return render(request, 'errors/500.html', {})

def site_map_view(request, *args, **kwargs):
    return render(request, 'sitemap.xml', {})

def robots_txt_view(request, *args, **kwargs):
    return render(request, 'robots.txt', {})
