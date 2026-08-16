from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ContactMessageForm


# Create your views here.

def contact(request):
    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

            return JsonResponse({
                'success': True,
                'message': 'پیام شما با موفقیت ارسال شد.'
            })

        return JsonResponse({
            'success': False,
            'errors': form.errors
        }, status=400)

    else:
        form = ContactMessageForm()

    return render(request, 'contact/contact.html', {
        'form': form
    })
