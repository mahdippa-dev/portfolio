from django.shortcuts import render
from .models import AboutPage
# Create your views here.

def about(request):

        about_page = AboutPage.objects.first()

        return render(request, 'about/about.html', {
            'about_page': about_page,
        })