from django.shortcuts import render

def home_view(request):
    context = {
        'page_name': 'Home Page',
        'year': 2025,
        'fruits': ['Apple', 'Banana', 'Cherry']
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    context = {
        'page_name': 'About Page',
        'year': 2025
    }
    return render(request, 'core/about.html', context)
